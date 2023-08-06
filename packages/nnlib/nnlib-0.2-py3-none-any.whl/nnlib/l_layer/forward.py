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


def linear_forward_activation(A_prev, W, b, activation_func, keep_prob):
    """
    Implement forward propagation

    Arguments:

    A_prev -- activation from previous layer or input data

    W -- weight matrix

    b -- bias vector

    activation_func -- activation function (from utils)
    keep_prob -- dropout probability

    keep_prob -- dropout probability

    keep_prob -- dropout probability

    Returns:

    A -- output of activation function

    Z -- cached pre activation matrix
    """

    Z = linear_forward(A_prev, W, b)
    A = activation_func(Z)
    D = np.random.rand(A.shape[0], A.shape[1]) < keep_prob
    A *= D
    A /= keep_prob

    return A, D, Z


def model_forward(X, parameters, keep_prob):
    """
    Implement forward propagation sequence

    Arguments:

    X -- input data

    parameters -- initial weights

    keep_prob -- probability of keeping a node for dropout

    Returns:

    AL -- last post-activation value

    caches -- dictionary of dictionaries containing values computed in the forward pass
    {A: activation, D: mask, Z: pre-activation}
    """

    caches = dict(A={}, D={}, Z={})
    A = X
    L = len(parameters["W"])
    caches['A'][0] = X
    caches['D'][0] = 1  # this ensures there is a value of D for every value of A

    for l in range(1, L):

        A_prev = A
        Wl = parameters["W"][l]
        bl = parameters["b"][l]
        A, D, Z = linear_forward_activation(A_prev, Wl, bl, relu, keep_prob)
        caches["A"][l] = A
        caches["D"][l] = D
        caches["Z"][l] = Z

    AL, _, ZL = linear_forward_activation(A, parameters["W"][L], parameters["b"][L], sigmoid, keep_prob=1)
    caches["A"][L] = AL
    caches["Z"][L] = ZL

    return AL, caches
