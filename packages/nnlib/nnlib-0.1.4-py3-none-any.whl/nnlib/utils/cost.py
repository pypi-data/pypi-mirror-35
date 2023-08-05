import numpy as np


def cross_entropy(AL, Y):
    """
    Implement cross-entropy loss function

    Arguments:
    AL -- probability vector corresponding to label predictions
    Y -- result vector

    Returns:
    cost -- cross-entropy cost
    """

    m = Y.shape[1]
    cost = np.squeeze(-np.sum(Y * (np.log(AL)) + (1-Y) * (np.log(1-AL)), keepdims=True)/m)

    return cost
