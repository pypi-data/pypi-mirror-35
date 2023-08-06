import numpy as np


def sigmoid_backward(dA, cache):
    """
    partial derivative of single SIGMOID unit

    Arguments:

    dA -- post-activation gradient

    cache -- (Z, A), the pre/post-activation matrix

    Returns:

    dZ -- gradient of cost with respect to Z
    """

    A = cache[1]
    dZ = dA * A * (1-A)

    return dZ


def relu_backward(dA, cache):
    """
    partial derivative of single RELU unit

    Arguments:

    dA -- post-activation gradient

    cache -- (Z, A), the pre/post-activation matrix

    Returns:

    dZ -- gradient of cost with respect to Z
    """

    Z = cache[0]
    dZ = np.array(dA, copy=True)
    dZ[Z <= 0] = 0

    return dZ
