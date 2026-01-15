import numpy as np

def log2_normalize(counts):
    return np.log2(counts + 1)