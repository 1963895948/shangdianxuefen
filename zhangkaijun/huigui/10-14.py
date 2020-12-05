import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor,Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def myliner():#线性回归预测房价
    lb = load_boston()#加载数据
    x_train, x_test, y_train, y_test = train_test_split(lb.data,lb.target,test_size=0.25)
    print(x_train.shape)
    print(len(x_train))
    print(x_train[0])
    print(y_train.shape)
    std_x = StandardScaler()#标准化
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)


    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1,1))#二维数组
    y_test = std_y.transform(y_test.reshape(-1,1))
    print(y_test.shape)

    print(len(x_train[0]))
    lr = LinearRegression()#线性回归
    lr.fit(x_train,y_train)
    print(lr.coef_)

    y_predict = std_y.inverse_transform(lr.predict(x_test))#预测

    #print(y_predict)
    print(mean_squared_error(std_y.inverse_transform(y_test),y_predict))
    print(lr.score(x_test, y_test))



    rd = Ridge(alpha=1.0)
    rd.fit(x_train,y_train)
    print(rd.coef_)
    print('岭回归:',lr.score(x_test, y_test))


    #梯度下降
    sgd = SGDRegressor()
    sgd.fit(x_train,y_train)
    print(sgd.coef_)

    sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    print("梯度下降：",sgd_predict)
    print(mean_squared_error(std_y.inverse_transform(y_test),sgd_predict))
    print(sgd.score(x_test,y_test))
    print(type(x_test))



def model(a, b, x):#函数模型
    return a*x + b

def cost_function(a, b, x, y):#损失率
    n = 5
    return 0.5/n * (np.square(y-a*x-b)).sum()

def optimize(a,b,x,y):
    n = 5
    alpha = 1e-1 #学习率0.1
    y_hat = model(a,b,x)
    da = (1.0/n) * ((y_hat-y)*x).sum()
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
    #myliner()
    x = [13854, 12213, 11009, 10655, 9503]  # 程序员工资，顺序为北京，上海，杭州，深圳，广州
    x = np.reshape(x, newshape=(5, 1)) / 10000.0
    y = [21332, 20162, 19138, 18621, 18016]  # 算法工程师，顺序和上面一致
    y = np.reshape(y, newshape=(5, 1)) / 10000.0
    a,b = iterate(0,0,x,y,1)
    a, b = iterate(a, b, x, y, 2)
    a, b = iterate(a, b, x, y, 5)
    a, b = iterate(a, b, x, y, 200)
    a, b = iterate(a, b, x, y, 500)
    a, b = iterate(a, b, x, y, 1000)
    a, b = iterate(a, b, x, y, 10000)
    sgd = SGDRegressor()
    sgd.fit(x, y)
    print(sgd.coef_)