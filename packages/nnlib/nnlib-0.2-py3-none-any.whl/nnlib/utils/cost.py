import numpy as np


def cross_entropy(AL, Y, parameters, alpha):
    """
    Implement cross-entropy loss function with l2 regularization

    Arguments:

    AL -- probability vector corresponding to label predictions

    Y -- result vector

    parameters -- self explanatory

    alpha -- l2 regularization parameter

    parameters -- self explanatory

    alpha -- l2 regularization parameter

    Returns:

    cost -- cross-entropy cost with l2 regularization
    """

    m = Y.shape[1]
    cost = np.squeeze(-np.sum(Y * np.log(AL) + (1-Y) * np.log(1-AL), keepdims=True)/m)
    cost += alpha/(2*m) * sum((np.sum(np.square(parameters['W'][Wl])) for Wl in parameters['W']))

    return cost
