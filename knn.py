import numpy as np
from collections import Counter

import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.datasets import make_regression

from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score


x_train , y_train = make_moons(100, noise=0.05, random_state=1)
x_test , y_test = make_moons(50, noise=0.12, random_state=1)

# plt.scatter(x_train[y_train==0][:, 0], x_train[y_train==0][:, 1], c='violet')
# plt.scatter(x_train[y_train==1][:, 0], x_train[y_train==1][:, 1], c='yellow')

# plt.scatter(x_test[y_test==0][:, 0], x_test[y_test==0][:, 1], c='indigo')
# plt.scatter(x_test[y_test==1][:, 0], x_test[y_test==1][:, 1], c='goldenrod')
# plt.show()

class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

knn = KNNClassifier(3)

print(knn.k)