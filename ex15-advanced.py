import numpy as np

x_train = np.random.rand(10, 3)  # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi) ** 2
    return np.sqrt(sum)


def nearest(x_train, x_test):
    nearest_index = -1  # clearly means not found yet
    min_distance = np.Inf

    for i in range(len(x_train)):
        current_distance = dist(x_train[i], x_test)

        # if this distance is smaller than the minimum found so far, update the smallest distance found so far and the index of the training vector
        if current_distance < min_distance:
            min_distance = current_distance
            nearest_index = i
    print(nearest_index)


nearest(x_train, x_test)
