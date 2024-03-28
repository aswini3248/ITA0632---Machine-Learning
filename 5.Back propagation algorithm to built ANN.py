import numpy as np
class NeuralNetwork:
    def __init__(self, i, h, o):
        self.w_ih = np.random.randn(i, h)
        self.w_ho = np.random.randn(h, o)
        self.b_h = np.zeros((1, h))
        self.b_o = np.zeros((1, o))
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def forward(self, x):
        self.h = self.sigmoid(np.dot(x, self.w_ih) + self.b_h)
        return self.sigmoid(np.dot(self.h, self.w_ho) + self.b_o)
    def backward(self, x, y, lr):
        e = y - self.o
        d_o = e * self.o * (1 - self.o)
        d_h = np.dot(d_o, self.w_ho.T) * self.h * (1 - self.h)
        self.w_ho += np.dot(self.h.T, d_o) * lr
        self.w_ih += np.dot(x.T, d_h) * lr
        self.b_o += np.sum(d_o, axis=0) * lr
        self.b_h += np.sum(d_h, axis=0) * lr
    def train(self, x, y, e, lr):
        for _ in range(e):
            self.o = self.forward(x)
            self.backward(x, y, lr)
            if _ % 1000 == 0:
                print(f'Epoch {_}, Loss: {np.mean(np.square(y - self.o))}')
X, y = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]), np.array([[0], [1], [1], [0]])
nn = NeuralNetwork(2, 3, 1)
nn.train(X, y, 10000, 0.1)
print("Predicted Output:")
print(nn.forward(X))
