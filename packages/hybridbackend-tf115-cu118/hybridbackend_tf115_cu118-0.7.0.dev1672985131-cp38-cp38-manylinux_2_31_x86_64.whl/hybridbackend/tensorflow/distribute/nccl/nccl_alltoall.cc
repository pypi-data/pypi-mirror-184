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

#include <tensorflow/core/framework/common_shape_fns.h>
#include <tensorflow/core/framework/op_kernel.h>
#include <tensorflow/core/framework/shape_inference.h>

#include <vector>

#include "hybridbackend/tensorflow/common/cast.h"
#include "hybridbackend/tensorflow/distribute/nccl/comm.h"

namespace tensorflow {
namespace hybridbackend {

#if HYBRIDBACKEND_NCCL

#if GOOGLE_CUDA
namespace functor {
template <typename DTYPE, typename WIRE_DTYPE>
struct NcclAlltoallCall {
  Status operator()(const Tensor& input, Tensor* output, Tensor* comm_input,
                    Tensor* comm_output, OpKernelContext* ctx, NcclComm* comm,
                    NcclCommAsyncOp* comm_op) {
    comm->stream()->ThenWaitUntilComputeDone(ctx);
    VLOG(1) << comm->DebugString() << " [" << comm_op->name() << "] [Alltoall]";
    TF_RETURN_IF_ERROR(comm->Alltoall(input, output));
    return Status::OK();
  }
};

template <>
struct NcclAlltoallCall<float, Eigen::half> {
  Status operator()(const Tensor& input, Tensor* output, Tensor* comm_input,
                    Tensor* comm_output, OpKernelContext* ctx, NcclComm* comm,
                    NcclCommAsyncOp* comm_op) {
    TF_RETURN_IF_ERROR(ctx->allocate_temp(DT_HALF, input.shape(), comm_input));
    TF_RETURN_IF_ERROR(
        ctx->allocate_temp(DT_HALF, output->shape(), comm_output));
    comm->stream()->ThenWaitUntilComputeDone(ctx);
    VLOG(1) << comm->DebugString() << " [" << comm_op->name() << "] [CastIn]";
    functor::Cast<float, Eigen::half>()(input, comm_input, ctx,
                                        comm->stream()->get());
    VLOG(1) << comm->DebugString() << " [" << comm_op->name() << "] [Alltoall]";
    TF_RETURN_IF_ERROR(comm->Alltoall(*comm_input, comm_output));
    VLOG(1) << comm->DebugString() << " [" << comm_op->name() << "] [CastOut]";
    functor::Cast<Eigen::half, float>()(*output, comm_output, ctx,
                                        comm->stream()->get());
    return Status::OK();
  }
};

template <typename DTYPE, typename WIRE_DTYPE>
struct NcclAlltoallNCall {
  Status operator()(const std::vector<Tensor>& n_input,
                    std::vector<Tensor*>* n_output,
                    std::vector<Tensor*>* n_comm_input,
                    std::vector<Tensor*>* n_comm_output, OpKernelContext* ctx,
                    NcclComm* comm, NcclCommAsyncOp* comm_op) {
    comm->stream()->ThenWaitUntilComputeDone(ctx);
    VLOG(1) << comm->DebugString() << " [" << comm_op->name()
            << "] [AlltoallN]";
    TF_RETURN_IF_ERROR(comm->AlltoallN(n_input, n_output));
    return Status::OK();
  }
};

template <>
struct NcclAlltoallNCall<float, Eigen::half> {
  Status operator()(const std::vector<Tensor>& n_input,
                    std::vector<Tensor*>* n_output,
                    std::vector<Tensor*>* n_comm_input,
                    std::vector<Tensor*>* n_comm_output, OpKernelContext* ctx,
                    NcclComm* comm, NcclCommAsyncOp* comm_op) {
    for (int idx = 0; idx < n_input.size(); ++idx) {
      TF_RETURN_IF_ERROR(ctx->allocate_temp(DT_HALF, n_input[idx].shape(),
                                            n_comm_input->at(idx),
                                            ctx->input_alloc_attr(idx)));
      TF_RETURN_IF_ERROR(ctx->allocate_temp(DT_HALF, n_output->at(idx)->shape(),
                                            n_comm_output->at(idx),
                                            ctx->output_alloc_attr(idx)));
    }
    comm->stream()->ThenWaitUntilComputeDone(ctx);
    VLOG(1) << comm->DebugString() << " [" << comm_op->name() << "] [CastIn]";
    functor::CastN<float, Eigen::half>()(n_input, n_comm_input, ctx,
                                         comm->stream()->get());
    VLOG(1) << comm->DebugString() << " [" << comm_op->name()
            << "] [AlltoallN]";
    TF_RETURN_IF_ERROR(comm->AlltoallN(*n_comm_input, n_comm_output));
    VLOG(1) << comm->DebugString() << " [" << comm_op->name() << "] [CastOut]";
    functor::CastN<Eigen::half, float>()(*n_comm_output, n_output, ctx,
                                         comm->stream()->get());
    return Status::OK();
  }
};
}  // namespace functor
#endif  // GOOGLE_CUDA

REGISTER_OP("HbNcclAlltoall")
    .Output("output: dtype")
    .Input("handle: resource")
    .Input("input: dtype")
    .Attr("dtype: {" TF_OP_NCCL_DTYPE_LIST "}")
    .Attr("wire_dtype: {" TF_OP_NCCL_WIRE_DTYPE_LIST "}")
    .SetIsStateful()
    .SetShapeFn([](shape_inference::InferenceContext* c) {
      c->set_output(0, c->input(1));
      return Status::OK();
    })
    .Doc(R"doc(
AllToAll using a NCCL communicator.

output: Exchanged tensor.
handle: Handle of a NCCL communicator.
input: Tensor to exchange.
)doc");

#if GOOGLE_CUDA
template <typename DTYPE, typename WIRE_DTYPE>
class NcclAlltoallOp : public NcclCommAsyncOp {
 public:
  explicit NcclAlltoallOp(OpKernelConstruction* ctx) : NcclCommAsyncOp(ctx) {}

  virtual void ComputeAsyncWithComm(NcclComm* comm, OpKernelContext* ctx,
                                    DoneCallback done) override {
    Tensor* comm_input = new Tensor();
    Tensor* comm_output = new Tensor();
    auto done_ = [comm_input, comm_output, done]() {
      delete comm_input;
      delete comm_output;
      done();
    };

    const Tensor* input;
    OP_REQUIRES_OK_ASYNC(ctx, ctx->input("input", &input), done_);
    Tensor* output;
    OP_REQUIRES_OK_ASYNC(ctx, ctx->allocate_output(0, input->shape(), &output),
                         done_);
    comm->stream()->LaunchUntilComputeDone(ctx, [input, output, comm_input,
                                                 comm_output, ctx, comm, this,
                                                 done_]() {
      auto call = functor::NcclAlltoallCall<DTYPE, WIRE_DTYPE>();
      OP_REQUIRES_OK_ASYNC(
          ctx, call(*input, output, comm_input, comm_output, ctx, comm, this),
          done_);
      comm->stream()->BlockComputeUntilDone(ctx, done_);
    });
  }
};

#define REGISTER_KERNEL(DTYPE, WIRE_DTYPE)                               \
  REGISTER_KERNEL_BUILDER(Name("HbNcclAlltoall")                         \
                              .Device(DEVICE_GPU)                        \
                              .TypeConstraint<DTYPE>("dtype")            \
                              .TypeConstraint<WIRE_DTYPE>("wire_dtype"), \
                          NcclAlltoallOp<DTYPE, WIRE_DTYPE>);
TF_CALL_NCCL_CAST_TYPES(REGISTER_KERNEL);
#undef REGISTER_KERNEL
#endif  // GOOGLE_CUDA

REGISTER_OP("HbNcclAlltoallN")
    .Output("n_output: N * dtype")
    .Input("handle: resource")
    .Input("n_input: N * dtype")
    .Attr("dtype: {" TF_OP_NCCL_DTYPE_LIST "}")
    .Attr("wire_dtype: {" TF_OP_NCCL_WIRE_DTYPE_LIST "}")
    .Attr("N: int >= 1 = 1")
    .SetIsStateful()
    .SetShapeFn([](shape_inference::InferenceContext* c) {
      int64 N;
      TF_RETURN_IF_ERROR(c->GetAttr("N", &N));
      for (int64 n = 0; n < N; ++n) {
        c->set_output(n, c->input(1 + n));
      }
      return Status::OK();
    })
    .Doc(R"doc(
Packed AllToAll using a NCCL communicator.

n_output: N exchanged tensors.
handle: Handle of a NCCL communicator.
n_input: N tensors to exchange.
)doc");

#if GOOGLE_CUDA
template <typename DTYPE, typename WIRE_DTYPE>
class NcclAlltoallNOp : public NcclCommAsyncOp {
 public:
  explicit NcclAlltoallNOp(OpKernelConstruction* ctx) : NcclCommAsyncOp(ctx) {
    OP_REQUIRES_OK(ctx, ctx->GetAttr("N", &N_));
  }

  virtual void ComputeAsyncWithComm(NcclComm* comm, OpKernelContext* ctx,
                                    DoneCallback done) override {
    std::vector<Tensor>* n_input = new std::vector<Tensor>();
    std::vector<Tensor*>* n_comm_input = new std::vector<Tensor*>();
    std::vector<Tensor*>* n_comm_output = new std::vector<Tensor*>();
    for (int idx = 0; idx < N_; ++idx) {
      n_comm_input->push_back(new Tensor());
      n_comm_output->push_back(new Tensor());
    }
    std::vector<Tensor*>* n_output = new std::vector<Tensor*>();

    auto done_ = [this, n_input, n_output, n_comm_input, n_comm_output,
                  done]() {
      delete n_input;
      delete n_output;
      for (int idx = 0; idx < N_; ++idx) {
        delete n_comm_input->at(idx);
        delete n_comm_output->at(idx);
      }
      delete n_comm_input;
      delete n_comm_output;
      done();
    };

    OpInputList n_input_list;
    OP_REQUIRES_OK_ASYNC(ctx, ctx->input_list("n_input", &n_input_list), done_);
    for (int idx = 0; idx < N_; ++idx) {
      n_input->push_back(n_input_list[idx]);
      Tensor* output;
      OP_REQUIRES_OK_ASYNC(
          ctx, ctx->allocate_output(idx, n_input_list[idx].shape(), &output),
          done_);
      n_output->push_back(output);
    }

    comm->stream()->LaunchUntilComputeDone(
        ctx, [n_input, n_output, n_comm_input, n_comm_output, ctx, comm, this,
              done_]() {
          auto call = functor::NcclAlltoallNCall<DTYPE, WIRE_DTYPE>();
          OP_REQUIRES_OK_ASYNC(ctx,
                               call(*n_input, n_output, n_comm_input,
                                    n_comm_output, ctx, comm, this),
                               done_);
          comm->stream()->BlockComputeUntilDone(ctx, done_);
        });
  }

 private:
  int64 N_;
};

#define REGISTER_KERNEL(DTYPE, WIRE_DTYPE)                               \
  REGISTER_KERNEL_BUILDER(Name("HbNcclAlltoallN")                        \
                              .Device(DEVICE_GPU)                        \
                              .TypeConstraint<DTYPE>("dtype")            \
                              .TypeConstraint<WIRE_DTYPE>("wire_dtype"), \
                          NcclAlltoallNOp<DTYPE, WIRE_DTYPE>);
TF_CALL_NCCL_CAST_TYPES(REGISTER_KERNEL);
#undef REGISTER_KERNEL
#endif  // GOOGLE_CUDA

REGISTER_OP("HbNcclAlltoallMergedN")
    .Output("n_output: N * dtype")
    .Input("handle: resource")
    .Input("n_input: N * dtype")
    .Attr("dtype: {" TF_OP_NCCL_DTYPE_LIST "}")
    .Attr("wire_dtype: {" TF_OP_NCCL_WIRE_DTYPE_LIST "}")
    .Attr("N: int >= 1 = 1")
    .SetIsStateful()
    .SetShapeFn([](shape_inference::InferenceContext* c) {
      int64 N;
      TF_RETURN_IF_ERROR(c->GetAttr("N", &N));
      for (int64 n = 0; n < N; ++n) {
        c->set_output(n, c->input(1 + n));
      }
      return Status::OK();
    })
    .Doc(R"doc(
Packed merged AllToAll using a NCCL communicator.

n_output: N exchanged tensors.
handle: Handle of a NCCL communicator.
n_input: N tensors to exchange.
)doc");

#if GOOGLE_CUDA
template <typename DTYPE, typename WIRE_DTYPE>
class NcclAlltoallMergedNOp : public NcclCommAsyncOp {
 public:
  explicit NcclAlltoallMergedNOp(OpKernelConstruction* ctx)
      : NcclCommAsyncOp(ctx) {
    OP_REQUIRES_OK(ctx, ctx->GetAttr("N", &N_));
  }

  virtual void ComputeAsyncWithComm(NcclComm* comm, OpKernelContext* ctx,
                                    DoneCallback done) override {
    std::vector<int64>* input_bytes_vec = new std::vector<int64>(N_, 0);
    std::vector<Tensor*>* n_output = new std::vector<Tensor*>(N_, nullptr);
    Tensor* buffer_input = new Tensor();
    Tensor* buffer_output = new Tensor();
    Tensor* buffer_comm_input = new Tensor();
    Tensor* buffer_comm_output = new Tensor();
    auto done_ = [input_bytes_vec, n_output, buffer_input, buffer_output,
                  buffer_comm_input, buffer_comm_output, done]() {
      delete input_bytes_vec;
      delete n_output;
      delete buffer_input;
      delete buffer_output;
      delete buffer_comm_input;
      delete buffer_comm_output;
      done();
    };

    OpInputList n_input_list;
    OP_REQUIRES_OK_ASYNC(ctx, ctx->input_list("n_input", &n_input_list), done_);
    int64 total_bytes = 0;
    for (int idx = 0; idx < N_; ++idx) {
      const auto input_bytes = DataTypeSize(n_input_list[idx].dtype()) *
                               n_input_list[idx].NumElements();
      total_bytes += input_bytes;
      input_bytes_vec->at(idx) = input_bytes;
    }
    OP_REQUIRES_OK_ASYNC(
        ctx, ctx->allocate_temp(DT_INT8, {total_bytes}, buffer_input), done_);
    OP_REQUIRES_OK_ASYNC(
        ctx, ctx->allocate_temp(DT_INT8, {total_bytes}, buffer_output), done_);
    int64 offset_bytes = 0;
    for (int64 idx = 0; idx < N_; ++idx) {
      OP_REQUIRES_OK_ASYNC(ctx,
                           ctx->allocate_output(idx, n_input_list[idx].shape(),
                                                &(n_output->at(idx))),
                           done_);

      se::DeviceMemoryBase dst_ptr(
          const_cast<char*>(buffer_input->tensor_data().data()) + offset_bytes,
          input_bytes_vec->at(idx));
      ctx->op_device_context()->stream()->ThenMemcpy(
          &dst_ptr,
          se::DeviceMemoryBase(
              const_cast<char*>(n_input_list[idx].tensor_data().data()),
              input_bytes_vec->at(idx)),
          input_bytes_vec->at(idx));
      offset_bytes += input_bytes_vec->at(idx);
    }

    comm->stream()->LaunchUntilComputeDone(
        ctx, [input_bytes_vec, n_output, buffer_input, buffer_output,
              buffer_comm_input, buffer_comm_output, ctx, comm, this, done_]() {
          auto call = functor::NcclAlltoallCall<DTYPE, WIRE_DTYPE>();
          OP_REQUIRES_OK_ASYNC(
              ctx,
              call(*buffer_input, buffer_output, buffer_comm_input,
                   buffer_comm_output, ctx, comm, this),
              done_);
          int64 offset_bytes = 0;
          for (int idx = 0; idx < N_; ++idx) {
            se::DeviceMemoryBase dst_ptr(
                const_cast<char*>(n_output->at(idx)->tensor_data().data()),
                input_bytes_vec->at(idx));
            comm->stream()->ThenMemcpy(
                &dst_ptr,
                se::DeviceMemoryBase(
                    const_cast<char*>(buffer_output->tensor_data().data()) +
                        offset_bytes,
                    input_bytes_vec->at(idx)),
                input_bytes_vec->at(idx));
            offset_bytes += input_bytes_vec->at(idx);
          }
          comm->stream()->BlockComputeUntilDone(ctx, done_);
        });
  }

 private:
  int64 N_;
};

#define REGISTER_KERNEL(DTYPE, WIRE_DTYPE)                               \
  REGISTER_KERNEL_BUILDER(Name("HbNcclAlltoallMergedN")                  \
                              .Device(DEVICE_GPU)                        \
                              .TypeConstraint<DTYPE>("dtype")            \
                              .TypeConstraint<WIRE_DTYPE>("wire_dtype"), \
                          NcclAlltoallMergedNOp<DTYPE, WIRE_DTYPE>);
TF_CALL_NCCL_CAST_TYPES(REGISTER_KERNEL);
#undef REGISTER_KERNEL
#endif  // GOOGLE_CUDA

#endif

}  // namespace hybridbackend
}  // namespace tensorflow

#endif  // HYBRIDBACKEND_TENSORFLOW
