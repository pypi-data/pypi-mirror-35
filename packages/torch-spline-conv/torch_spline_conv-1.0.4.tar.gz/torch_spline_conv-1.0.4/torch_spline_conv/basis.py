import torch
import basis_cpu

if torch.cuda.is_available():
    import basis_cuda

implemented_degrees = {1: 'linear', 2: 'quadratic', 3: 'cubic'}


def get_func(name, tensor):
    module = basis_cuda if tensor.is_cuda else basis_cpu
    return getattr(module, name)


class SplineBasis(torch.autograd.Function):
    @staticmethod
    def forward(ctx, pseudo, kernel_size, is_open_spline, degree):
        ctx.save_for_backward(pseudo)
        ctx.kernel_size, ctx.is_open_spline = kernel_size, is_open_spline
        ctx.degree = degree

        op = get_func('{}_fw'.format(implemented_degrees[degree]), pseudo)
        basis, weight_index = op(pseudo, kernel_size, is_open_spline)

        return basis, weight_index

    @staticmethod
    def backward(ctx, grad_basis, grad_weight_index):
        pseudo, = ctx.saved_tensors
        kernel_size, is_open_spline = ctx.kernel_size, ctx.is_open_spline
        degree = ctx.degree
        grad_pseudo = None

        if ctx.needs_input_grad[0]:
            op = get_func('{}_bw'.format(implemented_degrees[degree]), pseudo)
            grad_pseudo = op(grad_basis, pseudo, kernel_size, is_open_spline)

        return grad_pseudo, None, None, None
