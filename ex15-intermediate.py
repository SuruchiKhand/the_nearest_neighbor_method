import numpy as np


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi) ** 2
    return np.sqrt(sum)


a = [14, 3, 0.8]
b = [2, 6, 0.8]

print("Option A Output:", dist(a, b))
