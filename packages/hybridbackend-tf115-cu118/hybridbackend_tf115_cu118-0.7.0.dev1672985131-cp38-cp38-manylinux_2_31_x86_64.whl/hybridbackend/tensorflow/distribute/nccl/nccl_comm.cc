/* Copyright 2021 Alibaba Group Holding Limited. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#if HYBRIDBACKEND_TENSORFLOW

#include <mutex>
#include <vector>

#include <absl/strings/str_cat.h>

#include <tensorflow/core/framework/common_shape_fns.h>
#include <tensorflow/core/framework/op_kernel.h>
#include <tensorflow/core/framework/shape_inference.h>

#if GOOGLE_CUDA
#include <tensorflow/stream_executor/cuda/cuda_activation.h>

#include "hybridbackend/common/profiler.h"
#include "hybridbackend/tensorflow/distribute/nccl/comm.h"
#endif

namespace tensorflow {
namespace hybridbackend {

#if HYBRIDBACKEND_NCCL
#if GOOGLE_CUDA

NcclComm::NcclComm() : stream_(new Stream) {}

NcclComm::~NcclComm() {
  std::unique_lock<std::mutex> lock(mu_);
  if (created_) {
    Destroy();
  }
}

Status NcclComm::Initialize(OpKernelContext* ctx, const string& shared_name,
                            int size, int rank) {
  if (!TF_PREDICT_TRUE(0 <= rank && rank < size)) {
    return errors::InvalidArgument(
        absl::StrCat("NCCL rank ", rank, " or size ", size, " is invalid."));
  }

  std::unique_lock<std::mutex> lock(mu_);
  world_size_ = size;
  rank_ = rank;

  stream_->Initialize(ctx, absl::StrCat("nccl_comm_", shared_name, "_threads"),
                      3 /* num_threads */);

  debug_string_ = absl::StrCat("NcclComm(name=", shared_name, ", size=", size,
                               ", rank=", rank, ")");

  return Status::OK();
}

Status NcclComm::Create(const string& id) {
  std::unique_lock<std::mutex> lock(mu_);
  if (!TF_PREDICT_TRUE(id.size() == NCCL_UNIQUE_ID_BYTES)) {
    return errors::InvalidArgument(
        absl::StrCat("NCCL ID ", id.c_str(), " is invalid."));
  }

  ncclUniqueId nccl_id;
  memcpy(nccl_id.internal, &id[0], NCCL_UNIQUE_ID_BYTES);
  TF_RETURN_IF_ERROR(
      NcclErrorToStatus(ncclCommInitRank(&comm_, world_size_, nccl_id, rank_)));
  created_ = true;
  return Status::OK();
}

Status NcclComm::Destroy() {
  std::unique_lock<std::mutex> lock(mu_);
  created_ = false;
  TF_RETURN_IF_ERROR(NcclErrorToStatus(ncclCommDestroy(comm_)));
  delete stream_;
  return Status::OK();
}

Status NcclComm::CheckAsyncErrors() {
  std::unique_lock<std::mutex> lock(mu_);
  if (TF_PREDICT_FALSE(!created_)) {
    return Status::OK();
  }
  ncclResult_t async_error;
  TF_RETURN_IF_ERROR(
      NcclErrorToStatus(ncclCommGetAsyncError(comm_, &async_error)));
  if (TF_PREDICT_TRUE(async_error == ncclSuccess)) {
    return Status::OK();
  }

  LOG(ERROR) << "NCCL communication aborted: "
             << ncclGetErrorString(async_error);
  TF_RETURN_IF_ERROR(NcclErrorToStatus(ncclCommAbort(comm_)));
  return NcclErrorToStatus(async_error);
}

Status NcclComm::UserRank(int* rank) {
  std::unique_lock<std::mutex> lock(mu_);
  return NcclErrorToStatus(ncclCommUserRank(comm_, rank));
}

Status NcclComm::Allreduce(const Tensor& input, const ncclRedOp_t reduce_op,
                           Tensor* output) {
  const void* sendbuf = input.tensor_data().data();
  void* recvbuf = const_cast<char*>(output->tensor_data().data());
  const size_t count = input.NumElements();
  if (TF_PREDICT_FALSE(count < 1)) {
    return Status::OK();
  }
  ncclDataType_t nccl_dtype(ncclFloat);
  TF_RETURN_IF_ERROR(EnumToNcclEnum(input.dtype(), &nccl_dtype));

  std::unique_lock<std::mutex> lock(mu_);
  return NcclErrorToStatus(ncclAllReduce(sendbuf, recvbuf, count, nccl_dtype,
                                         reduce_op, comm_, *(stream_->get())));
}

Status NcclComm::AllreduceN(const std::vector<Tensor>& n_input,
                            const ncclRedOp_t reduce_op,
                            std::vector<Tensor*>* n_output) {
  std::unique_lock<std::mutex> lock(mu_);
  ncclGroupStart();
  for (size_t idx = 0; idx < n_input.size(); ++idx) {
    const void* sendbuf = n_input[idx].tensor_data().data();
    void* recvbuf = const_cast<char*>(n_output->at(idx)->tensor_data().data());
    const size_t count = n_input[idx].NumElements();
    if (TF_PREDICT_FALSE(count < 1)) {
      continue;
    }
    ncclDataType_t nccl_dtype(ncclFloat);
    TF_RETURN_IF_ERROR(EnumToNcclEnum(n_input[idx].dtype(), &nccl_dtype));

    TF_RETURN_IF_ERROR(
        NcclErrorToStatus(ncclAllReduce(sendbuf, recvbuf, count, nccl_dtype,
                                        reduce_op, comm_, *(stream_->get()))));
  }
  ncclGroupEnd();
  return Status::OK();
}

Status NcclComm::Alltoall(const Tensor& input, Tensor* output) {
  const size_t count = input.NumElements();
  if (TF_PREDICT_FALSE(count == 0)) {
    return Status::OK();
  }
  if (TF_PREDICT_FALSE(count % world_size_ != 0)) {
    return errors::InvalidArgument("Number of elements in input (", count,
                                   ") must can be divided into ", world_size_,
                                   " partitions");
  }

#if NCCL_VERSION_CODE >= 2700
  const char* sendbuf = input.tensor_data().data();
  char* recvbuf = const_cast<char*>(output->tensor_data().data());
  const size_t partition_size = count / world_size_;
  ncclDataType_t nccl_dtype(ncclFloat);
  TF_RETURN_IF_ERROR(EnumToNcclEnum(input.dtype(), &nccl_dtype));
  const size_t dtype_size = DataTypeSize(input.dtype());

  std::unique_lock<std::mutex> lock(mu_);
  ncclGroupStart();
  for (int rank = 0; rank < world_size_; ++rank) {
    const size_t partition_bytes = rank * partition_size * dtype_size;
    TF_RETURN_IF_ERROR(NcclErrorToStatus(
        ncclSend(sendbuf + partition_bytes, partition_size, nccl_dtype, rank,
                 comm_, *(stream_->get()))));
    TF_RETURN_IF_ERROR(NcclErrorToStatus(
        ncclRecv(recvbuf + partition_bytes, partition_size, nccl_dtype, rank,
                 comm_, *(stream_->get()))));
  }
  ncclGroupEnd();
  return Status::OK();
#else
  return errors::Unimplemented("Alltoall not supported in NCCL < 2.7");
#endif
}

Status NcclComm::AlltoallN(const std::vector<Tensor>& n_input,
                           std::vector<Tensor*>* n_output) {
  if (TF_PREDICT_FALSE(n_output->size() != n_input.size())) {
    return errors::InvalidArgument(
        "Inputs and outputs of AlltoallN must have same length");
  }

#if NCCL_VERSION_CODE >= 2700
  std::unique_lock<std::mutex> lock(mu_);
  ncclGroupStart();
  for (size_t idx = 0; idx < n_input.size(); ++idx) {
    const size_t count = n_input[idx].NumElements();
    if (TF_PREDICT_FALSE(count == 0)) {
      continue;
    }
    if (TF_PREDICT_FALSE(count % world_size_ != 0)) {
      return errors::InvalidArgument("Number of elements in input (", count,
                                     ") must can be divided into ", world_size_,
                                     " partitions");
    }
    const char* sendbuf = n_input[idx].tensor_data().data();
    char* recvbuf = const_cast<char*>(n_output->at(idx)->tensor_data().data());
    const size_t partition_size = count / world_size_;
    ncclDataType_t nccl_dtype(ncclFloat);
    TF_RETURN_IF_ERROR(EnumToNcclEnum(n_input[idx].dtype(), &nccl_dtype));
    const size_t dtype_size = DataTypeSize(n_input[idx].dtype());

    for (int rank = 0; rank < world_size_; ++rank) {
      const size_t partition_bytes = rank * partition_size * dtype_size;
      TF_RETURN_IF_ERROR(NcclErrorToStatus(
          ncclSend(sendbuf + partition_bytes, partition_size, nccl_dtype, rank,
                   comm_, *(stream_->get()))));
      TF_RETURN_IF_ERROR(NcclErrorToStatus(
          ncclRecv(recvbuf + partition_bytes, partition_size, nccl_dtype, rank,
                   comm_, *(stream_->get()))));
    }
  }
  ncclGroupEnd();
  return Status::OK();
#else
  return errors::Unimplemented("AlltoallN not supported in NCCL < 2.7");
#endif
}

Status NcclComm::AlltoallN(const std::vector<Tensor*>& n_input,
                           std::vector<Tensor*>* n_output) {
  if (TF_PREDICT_FALSE(n_output->size() != n_input.size())) {
    return errors::InvalidArgument(
        "Inputs and outputs of AlltoallN must have same length");
  }

#if NCCL_VERSION_CODE >= 2700
  std::unique_lock<std::mutex> lock(mu_);
  ncclGroupStart();
  for (size_t idx = 0; idx < n_input.size(); ++idx) {
    const size_t count = n_input[idx]->NumElements();
    if (TF_PREDICT_FALSE(count == 0)) {
      continue;
    }
    if (TF_PREDICT_FALSE(count % world_size_ != 0)) {
      return errors::InvalidArgument("Number of elements in input (", count,
                                     ") must can be divided into ", world_size_,
                                     " partitions");
    }
    const char* sendbuf = n_input[idx]->tensor_data().data();
    char* recvbuf = const_cast<char*>(n_output->at(idx)->tensor_data().data());
    const size_t partition_size = count / world_size_;
    ncclDataType_t nccl_dtype(ncclFloat);
    TF_RETURN_IF_ERROR(EnumToNcclEnum(n_input[idx]->dtype(), &nccl_dtype));
    const size_t dtype_size = DataTypeSize(n_input[idx]->dtype());
    ncclGroupStart();
    for (int rank = 0; rank < world_size_; ++rank) {
      const size_t partition_bytes = rank * partition_size * dtype_size;
      TF_RETURN_IF_ERROR(NcclErrorToStatus(
          ncclSend(sendbuf + partition_bytes, partition_size, nccl_dtype, rank,
                   comm_, *(stream_->get()))));
      TF_RETURN_IF_ERROR(NcclErrorToStatus(
          ncclRecv(recvbuf + partition_bytes, partition_size, nccl_dtype, rank,
                   comm_, *(stream_->get()))));
    }
    ncclGroupEnd();
  }
  ncclGroupEnd();
  return Status::OK();
#else
  return errors::Unimplemented("AlltoallN not supported in NCCL < 2.7");
#endif
}

Status NcclComm::Alltoallv(const Tensor& input, const int32* send_sizes,
                           const int32* recv_sizes, const int64 common_size,
                           Tensor* output) {
#if NCCL_VERSION_CODE >= 2700
  const char* sendbuf = input.tensor_data().data();
  char* recvbuf = const_cast<char*>(output->tensor_data().data());
  ncclDataType_t nccl_dtype(ncclFloat);
  TF_RETURN_IF_ERROR(EnumToNcclEnum(input.dtype(), &nccl_dtype));
  const int32 dtype_size = static_cast<int32>(DataTypeSize(input.dtype()));

  int32 sendoffset = 0;
  int32 recvoffset = 0;
  std::unique_lock<std::mutex> lock(mu_);
  ncclGroupStart();
  for (int rank = 0; rank < world_size_; ++rank) {
    const int32 sendsize = send_sizes[rank] * common_size;
    const int32 recvsize = recv_sizes[rank] * common_size;
    if (TF_PREDICT_TRUE(sendsize > 0)) {
      TF_RETURN_IF_ERROR(
          NcclErrorToStatus(ncclSend(sendbuf + sendoffset, sendsize, nccl_dtype,
                                     rank, comm_, *(stream_->get()))));
    }
    if (TF_PREDICT_TRUE(recvsize > 0)) {
      TF_RETURN_IF_ERROR(
          NcclErrorToStatus(ncclRecv(recvbuf + recvoffset, recvsize, nccl_dtype,
                                     rank, comm_, *(stream_->get()))));
    }
    sendoffset += sendsize * dtype_size;
    recvoffset += recvsize * dtype_size;
  }
  ncclGroupEnd();
  return Status::OK();
#else
  return errors::Unimplemented("Alltoallv not supported in NCCL < 2.7");
#endif
}

Status NcclComm::AlltoallvN(const std::vector<Tensor>& n_input,
                            const std::vector<int32*>& n_send_sizes,
                            const std::vector<int32*>& n_recv_sizes,
                            const std::vector<int64>& n_common_size,
                            std::vector<Tensor*>* n_output) {
  if (TF_PREDICT_FALSE(n_output->size() != n_input.size())) {
    return errors::InvalidArgument(
        "Inputs and outputs of AlltoallvN must have same length");
  }

#if NCCL_VERSION_CODE >= 2700
  std::unique_lock<std::mutex> lock(mu_);
  ncclGroupStart();
  for (size_t idx = 0; idx < n_input.size(); ++idx) {
    const char* sendbuf = n_input[idx].tensor_data().data();
    char* recvbuf = const_cast<char*>(n_output->at(idx)->tensor_data().data());
    ncclDataType_t nccl_dtype(ncclFloat);
    TF_RETURN_IF_ERROR(EnumToNcclEnum(n_input[idx].dtype(), &nccl_dtype));
    const int32 dtype_size =
        static_cast<int32>(DataTypeSize(n_input[idx].dtype()));

    int32 sendoffset = 0;
    int32 recvoffset = 0;
    ncclGroupStart();
    for (int rank = 0; rank < world_size_; ++rank) {
      const int32 sendsize = n_send_sizes[idx][rank] * n_common_size[idx];
      const int32 recvsize = n_recv_sizes[idx][rank] * n_common_size[idx];
      TF_RETURN_IF_ERROR(
          NcclErrorToStatus(ncclSend(sendbuf + sendoffset, sendsize, nccl_dtype,
                                     rank, comm_, *(stream_->get()))));
      TF_RETURN_IF_ERROR(
          NcclErrorToStatus(ncclRecv(recvbuf + recvoffset, recvsize, nccl_dtype,
                                     rank, comm_, *(stream_->get()))));
      sendoffset += sendsize * dtype_size;
      recvoffset += recvsize * dtype_size;
    }
    ncclGroupEnd();
  }
  ncclGroupEnd();
  return Status::OK();
#else
  return errors::Unimplemented("AlltoallvN not supported in NCCL < 2.7");
#endif
}

Status NcclComm::AlltoallvN(const std::vector<Tensor*>& n_input,
                            const std::vector<int32*>& n_send_sizes,
                            const std::vector<int32*>& n_recv_sizes,
                            const std::vector<int64>& n_common_size,
                            std::vector<Tensor*>* n_output) {
  if (TF_PREDICT_FALSE(n_output->size() != n_input.size())) {
    return errors::InvalidArgument(
        "Inputs and outputs of AlltoallvN must have same length");
  }

#if NCCL_VERSION_CODE >= 2700
  std::unique_lock<std::mutex> lock(mu_);
  ncclGroupStart();
  for (size_t idx = 0; idx < n_input.size(); ++idx) {
    const char* sendbuf = n_input[idx]->tensor_data().data();
    char* recvbuf = const_cast<char*>(n_output->at(idx)->tensor_data().data());
    ncclDataType_t nccl_dtype(ncclFloat);
    TF_RETURN_IF_ERROR(EnumToNcclEnum(n_input[idx]->dtype(), &nccl_dtype));
    const int32 dtype_size =
        static_cast<int32>(DataTypeSize(n_input[idx]->dtype()));

    int32 sendoffset = 0;
    int32 recvoffset = 0;
    ncclGroupStart();
    for (int rank = 0; rank < world_size_; ++rank) {
      const int32 sendsize = n_send_sizes[idx][rank] * n_common_size[idx];
      const int32 recvsize = n_recv_sizes[idx][rank] * n_common_size[idx];
      TF_RETURN_IF_ERROR(
          NcclErrorToStatus(ncclSend(sendbuf + sendoffset, sendsize, nccl_dtype,
                                     rank, comm_, *(stream_->get()))));
      TF_RETURN_IF_ERROR(
          NcclErrorToStatus(ncclRecv(recvbuf + recvoffset, recvsize, nccl_dtype,
                                     rank, comm_, *(stream_->get()))));
      sendoffset += sendsize * dtype_size;
      recvoffset += recvsize * dtype_size;
    }
    ncclGroupEnd();
  }
  ncclGroupEnd();
  return Status::OK();
#else
  return errors::Unimplemented("AlltoallvN not supported in NCCL < 2.7");
#endif
}

Status NcclComm::Broadcast(const Tensor& input, const int root_rank,
                           Tensor* output) {
  const void* sendbuf = input.tensor_data().data();
  void* recvbuf = const_cast<char*>(output->tensor_data().data());
  const size_t count = input.NumElements();
  ncclDataType_t nccl_dtype(ncclFloat);
  TF_RETURN_IF_ERROR(EnumToNcclEnum(input.dtype(), &nccl_dtype));

  std::unique_lock<std::mutex> lock(mu_);
  return NcclErrorToStatus(ncclBroadcast(sendbuf, recvbuf, count, nccl_dtype,
                                         root_rank, comm_, *(stream_->get())));
}

Status NcclComm::Allgather(const Tensor& input, Tensor* output) {
  const void* sendbuf = input.tensor_data().data();
  void* recvbuf = const_cast<char*>(output->tensor_data().data());
  const size_t count = input.NumElements();
  ncclDataType_t nccl_dtype(ncclFloat);
  TF_RETURN_IF_ERROR(EnumToNcclEnum(input.dtype(), &nccl_dtype));

  std::unique_lock<std::mutex> lock(mu_);
  return NcclErrorToStatus(ncclAllGather(sendbuf, recvbuf, count, nccl_dtype,
                                         comm_, *(stream_->get())));
}

Status NcclComm::Allgatherv(const Tensor& input, const Tensor& host_sizes,
                            Tensor* output) {
  const void* sendbuf = input.tensor_data().data();
  char* recvbuf = const_cast<char*>(output->tensor_data().data());
  const int32* sendcounts = host_sizes.flat<int32>().data();
  ncclDataType_t nccl_dtype(ncclFloat);
  TF_RETURN_IF_ERROR(EnumToNcclEnum(input.dtype(), &nccl_dtype));
  const size_t dtype_size = DataTypeSize(input.dtype());
  size_t offset = 0;

  std::unique_lock<std::mutex> lock(mu_);
  ncclGroupStart();
  for (int rank = 0; rank < world_size_; ++rank) {
    TF_RETURN_IF_ERROR(NcclErrorToStatus(
        ncclBroadcast(sendbuf, recvbuf + offset, sendcounts[rank], nccl_dtype,
                      rank, comm_, *(stream_->get()))));
    offset += sendcounts[rank] * dtype_size;
  }
  ncclGroupEnd();

  return Status::OK();
}

NcclCommAsyncOp::NcclCommAsyncOp(OpKernelConstruction* ctx)
    : AsyncOpKernel(ctx) {}

void NcclCommAsyncOp::ComputeAsync(OpKernelContext* ctx,
                                   AsyncOpKernel::DoneCallback done) {
  NcclComm* comm = nullptr;
  OP_REQUIRES_OK_ASYNC(ctx, LookupResource(ctx, HandleFromInput(ctx, 0), &comm),
                       done);
  ComputeAsyncWithComm(comm, ctx, done);
};

#endif
#endif

}  // namespace hybridbackend
}  // namespace tensorflow

#endif  // HYBRIDBACKEND_TENSORFLOW
