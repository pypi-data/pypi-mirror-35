import numpy as np

from nnlib.utils.derivative import relu_backward, sigmoid_backward


def linear_backward(dZ, cache, alpha, keep_prob):
    """
    Implement the linear portion of backward propagation

    Arguments:

    dZ -- Gradients of cost with respect to linear output of current layer l

    cache -- Tuple of values (A_prev, D_prev, W) coming from forward prop in current layer

    alpha -- l2 regularization term

    keep_prob -- dropout probability

    Returns:

    dA_prev -- Gradient of cost with respect to activation of previous layer (l-1)

    dW -- Gradient of cost with respect to W (current layer l)

    db -- Gradientof cost with respect to b (current layer l)

    keep_prob -- dropout probability
    """

    A_prev, D_prev, W = cache
    m = A_prev.shape[1]

    dW = np.matmul(dZ, A_prev.T)/m + alpha/m * W
    db = np.sum(dZ, axis=1, keepdims=True)/m
    dA_prev = np.matmul(W.T, dZ) * D_prev / keep_prob

    return dA_prev, dW, db


def linear_backward_activation(dA, cache, backward_func, alpha, keep_prob):
    """
    Implement backward propagation of entire layer

    Arguments:

    dA -- post-activation gradient for current layer l

    cache -- tuple ((A_prev, D_prev, W), (Z, A))

    backward_func -- calculates derivative of activation

    alpha -- l2 regularization term

    keep_prob -- dropout probability
    """

    linear_cache, activation_cache = cache
    dZ = backward_func(dA, activation_cache)
    dA_prev, dW, db = linear_backward(dZ, linear_cache, alpha, keep_prob)

    return dA_prev, dW, db


def model_backward(AL, Y, parameters, caches, alpha, keep_prob):
    """
    Implement backward propgation of arbitrary model

    Arguments:

    Al -- output of forward prop

    Y -- labels for data

    parameters -- dictionary of weights W, b

    caches -- dictionary of forward propagation values {A, D, Z}

    alpha -- l2 regularization term
    keep_prob -- dropout probability

    keep_prob -- dropout probability

    keep_prob -- dropout probability

    Returns:

    grads -- dictionary of lists for gradients of each layer
    """

    grads = dict(dA={}, dW={}, db={})
    L = len(caches["Z"])
    Y = Y.reshape(AL.shape)

    dAL = - (np.divide(Y, AL) - np.divide(1-Y, 1-AL))
    grads["dA"][L] = dAL
    dA_prev, dWL, dbL = linear_backward_activation(
            dAL,
            ((caches["A"][L-1], caches["D"][L-1], parameters["W"][L]), (caches["Z"][L], caches["A"][L])),
            sigmoid_backward,
            alpha,
            keep_prob
            )
    grads["dA"][L-1] = dA_prev
    grads["dW"][L] = dWL
    grads["db"][L] = dbL

    for l in reversed(range(L-1)):
        dA_prev, dWl, dbl = linear_backward_activation(
                grads["dA"][l+1],
                ((caches["A"][l], caches["D"][l], parameters["W"][l+1]), (caches["Z"][l+1], caches["A"][l+1])),
                relu_backward,
                alpha,
                keep_prob
                )
        grads["dA"][l] = dA_prev
        grads["dW"][l+1] = dWl
        grads["db"][l+1] = dbl

    return grads
