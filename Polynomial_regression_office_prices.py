import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def read_input():
    train, test = list(), list()

    F, N = map(int, input().split(' '))
    [train.append(input().split(' ')) for _ in range(N)]
    T = int(input())
    [test.append(input().split(' ')) for _ in range(T)]

    train = np.array(train, dtype=np.float64)
    test = np.array(test, dtype=np.float64)
    x_train = train[:, 0:F]
    y_train = train[:, -1]
    return x_train, y_train, test

x_train, y_train, x_test = read_input()
model = make_pipeline(PolynomialFeatures(degree=3), LinearRegression(fit_intercept=False))
model.fit(x_train, y_train)
predictions = model.predict(x_test)

for pred in predictions:
    print(pred)
