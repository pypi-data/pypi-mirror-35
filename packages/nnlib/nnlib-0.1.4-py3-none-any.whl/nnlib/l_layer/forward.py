import numpy as np

from nnlib.utils.activation import relu, sigmoid


def linear_forward(A_prev, W, b):
    """
    Implement linear part of forward propagation

    Arguments:
    A_prev -- activations from previous layer or input data
    W -- weight matrix
    b -- bias vector

    Returns:
    Z -- input for activation function
    """

    Z = np.matmul(W, A_prev) + b

    return Z


def linear_forward_activation(A_prev, W, b, activation_func):
    """
    Implement forward propagation
    Arguments:
    A_prev -- activation from previous layer or input data
    W -- weight matrix
    b -- bias vector
    activation_func -- activation function (from utils)

    Returns:
    A -- output of activation function
    Z -- cached pre activation matrix
    """

    Z = linear_forward(A_prev, W, b)
    A = activation_func(Z)

    return A, Z


def model_forward(X, parameters):
    """
    Implement forward propagation sequence

    Arguments:
    X -- input data
    parameters -- initial weights

    Returns:
    AL -- last post-activation value
    caches -- dictionary of lists containing values computed in the forward pass
    """
    caches = dict(A={}, Z={})
    A = X
    L = len(parameters["W"])
    caches['A'][0] = X

    for l in range(1, L):
        A_prev = A
        Wl = parameters["W"][l]
        bl = parameters["b"][l]
        A, Z = linear_forward_activation(A_prev, Wl, bl, relu)
        caches["A"][l] = A
        caches["Z"][l] = Z

    AL, ZL = linear_forward_activation(A, parameters["W"][L], parameters["b"][L], sigmoid)
    caches["A"][L] = AL
    caches["Z"][L] = ZL

    return AL, caches
