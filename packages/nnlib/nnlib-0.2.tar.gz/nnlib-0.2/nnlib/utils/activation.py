import numpy as np


def sigmoid(Z):
    """
    sigmoid activation function

    Arguments:

    Z -- numpy array

    Returns:

    A -- output of sigmoid(Z)

    cache -- Z, useful for back propagation
    """

    A = 1/(1+np.exp(-Z))

    return A


def relu(Z):
    """
    RELU activation function

    Arguments:

    Z -- numpy array

    Returns:

    A -- output of rulu(Z)

    cache -- Z, useful for back propagation
    """

    A = np.maximum(0, Z)

    return A
