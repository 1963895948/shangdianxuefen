import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor,Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def model(a, b, x):#函数模型
    return a*x*x + b

def cost_function(a, b, x, y):#损失率
    n = 5
    return 0.5/n * (np.square(y-a*x*x-b)).sum()

def optimize(a,b,x,y):
    n = 5
    alpha = 1e-1 #学习率0.1
    y_hat = model(a,b,x)
    da = (1.0/n) * ((y_hat-y)*2*x).sum()
    db = (1.0/n) * ((y_hat-y).sum())
    a = a - alpha*da
    b = b - alpha*db
    return a, b


def iterate(a,b,x,y,times):
    for i in range(times):
        a,b = optimize(a,b,x,y)

    y_hat=model(a,b,x)
    cost = cost_function(a, b, x, y)
    print(a,b,cost)
    plt.scatter(x,y)
    plt.plot(x,y_hat)
    plt.show()
    return a,b


if __name__ == '__main__':
    # x = [13854, 12213, 11009, 10655, 9503]  # 程序员工资，顺序为北京，上海，杭州，深圳，广州
    # x = np.reshape(x, newshape=(5, 1)) / 10000.0
    # y = [21332, 20162, 19138, 18621, 18016]  # 算法工程师，顺序和上面一致
    # y = np.reshape(y, newshape=(5, 1)) / 10000.0
    x = [1,2,3,4,5]
    x = np.reshape(x, newshape=(5, 1))
    y = [1,4,9,16,25]
    y = np.reshape(y, newshape=(5, 1))
    a,b = iterate(0,0,x,y,1)
    a, b = iterate(a, b, x, y, 2)
    a, b = iterate(a, b, x, y, 5)
    a, b = iterate(a, b, x, y, 200)
    a, b = iterate(a, b, x, y, 500)
    # a, b = iterate(a, b, x, y, 1000)
    # a, b = iterate(a, b, x, y, 10000)
    # sgd = SGDRegressor()
    # sgd.fit(x, y)
    # print(sgd.coef_)