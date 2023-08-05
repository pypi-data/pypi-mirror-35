import numpy as np

from nnlib.utils.initialize import initialize_parameters
from nnlib.utils.update import update_parameters
from nnlib.utils.cost import cross_entropy
from nnlib.l_layer.forward import model_forward
from nnlib.l_layer.backward import model_backward


class LLayer:
    """
    Simple model of arbitrary depth and complexity
    """

    def fit_params(self, X, Y, layers_dims, num_iterations, learning_rate=0.0075, verbose=True):
        self.X = X
        self.Y = Y
        self.layers_dims = layers_dims
        self.parameters = initialize_parameters(layers_dims)
        self.costs = []

        for i in range(0, num_iterations):
            AL, caches = model_forward(self.X, self.parameters)
            grads = model_backward(AL, self.Y, self.parameters, caches)
            self.parameters = update_parameters(self.parameters, grads, learning_rate)
            cost = cross_entropy(AL, self.Y)
            if verbose and i % 100 == 0:
                print(str(i) + ' iterations: ' + str(cost))
                self.costs.append(cost)

    def verify_cost(self, X_test, Y_test):
        AL, caches = model_forward(X_test, self.parameters)
        cost = cross_entropy(AL, Y_test)

        return cost

    def predict(self, X):
        AL, caches = model_forward(X, self.parameters)
        AL[AL > 0.5] = 1
        AL[AL <= 0.5] = 0

        return AL

    def verify_accuracy(self, X_test, Y_test):
        m = X_test.shape[1]
        p = self.predict(X_test)
        accuracy = np.sum((p == Y_test)/m)

        return accuracy
