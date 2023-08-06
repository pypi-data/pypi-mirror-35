def update_parameters(parameters, grads, learning_rate):
    """
    Update parameters using gradient descent

    Arguments:

    parameters -- python dictionary of parameters

    grads -- python dictionary containing gradients

    learning_rate -- hyperperameter to be tuned

    Returns:

    parameters -- python dictionary containing updated parameters
    """

    L = len(parameters["W"])

    for l in range(L):
        parameters["W"][l+1] = parameters["W"][l+1] - learning_rate*grads["dW"][l+1]
        parameters["b"][l+1] = parameters["b"][l+1] - learning_rate*grads["db"][l+1]

    return parameters
