import numpy as np


def he_initialization(layers_dims, layer):
    """
    Arguments:

    layer_dims -- python list containing tuples of dimensions of each layer in the network

    layer -- layer number of current layer

    Returns:

    constant -- numerical constant used to scale the initialized weights
    """
    return np.sqrt(np.divide(2, layers_dims[layer-1]))


def initialize_parameters(layers_dims, initialization_func=he_initialization):
    """
    Arguments:

    layer_dims -- python list containing tuples of dimensions of each layer in the network

    Returns:

    parameters -- python dictionary containing dictionary of Weights "W[]" and dictionary of bias vectors "b[]"
    """

    parameters = dict(W={}, b={})
    L = len(layers_dims)

    for l in range(1, L):
        parameters["W"][l] = np.random.randn(layers_dims[l], layers_dims[l-1])*initialization_func(layers_dims, l)
        parameters["b"][l] = np.zeros((layers_dims[l], 1))

    return parameters
