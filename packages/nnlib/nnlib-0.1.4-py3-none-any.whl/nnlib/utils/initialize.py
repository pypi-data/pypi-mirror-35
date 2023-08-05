import numpy as np


def initialize_parameters(layers_dims):
    """
    Arguments:
    layer_dims -- python list containing tuples of dimensions of each layer in the network

    Returns:
    parameters -- python dictionary containing dictionary of Weights "W[]" and dictionary of bias vectors "b[]"
    """

    parameters = dict(W={}, b={})
    L = len(layers_dims)

    for l in range(1, L):
        parameters["W"][l] = np.random.randn(layers_dims[l], layers_dims[l-1])*0.01
        parameters["b"][l] = np.zeros((layers_dims[l], 1))

    return parameters
