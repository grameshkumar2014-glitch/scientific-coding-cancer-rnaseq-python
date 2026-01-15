import numpy as np

def permutation_test(matrix, labels, n_permutations=1000):
    observed = matrix[:, labels == "tumor"].mean(axis=1) - \
               matrix[:, labels == "normal"].mean(axis=1)

    null_dist = []
    for _ in range(n_permutations):
        permuted = np.random.permutation(labels)
        stat = matrix[:, permuted == "tumor"].mean(axis=1) - \
               matrix[:, permuted == "normal"].mean(axis=1)
        null_dist.append(stat)

    return observed, np.array(null_dist)