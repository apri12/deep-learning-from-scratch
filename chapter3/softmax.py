import numpy as np

def softmax(x):
    c = np.max(x)
    return np.exp(x-c) / np.sum(np.exp(x-c))
