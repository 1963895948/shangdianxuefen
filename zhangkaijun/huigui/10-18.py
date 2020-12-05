import datetime
import numpy as np
import pandas as pd
import time
from sklearn.datasets import load_boston
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression, SGDRegressor,Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import random



def bike():
    x_data = pd.read_csv('hour.csv', usecols=[8, 10, 11, 12]).values
    y_data = pd.read_csv('hour.csv', usecols=[15]).values
    # print(x_data)
    # print(y_data)


    x_train, x_test, y_train, y_test = x_data[0:int(len(x_data)*0.75)],x_data[int(len(x_data)*0.75):len(x_data)],y_data[0:int(len(y_data)*0.75)],y_data[int(len(y_data)*0.75):len(y_data)]
    for i in range(len(x_train)):
        print(x_train[i],y_train[i])

    # x已经标准化，现在对y标准化
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))  # 二维数组
    y_test = std_y.transform(y_test.reshape(-1, 1))
    print(y_train)

    lr = LinearRegression()  # 线性回归
    lr.fit(x_train, y_train)
    print(lr.coef_)

    # y_predict = lr.predict(x_test)  # 预测
    # for i in range(len(y_predict)):
    #     print(y_predict[i], y_test[i])
    # print(mean_squared_error(y_test, y_predict))
    # print(lr.score(x_test, y_test))


    y_predict = std_y.inverse_transform(lr.predict(x_test))  # 预测
    for i in range(len(y_predict)):
        print(y_predict[i],std_y.inverse_transform(y_test)[i])
    print(mean_squared_error(std_y.inverse_transform(y_test), y_predict))
    print(lr.score(x_test, y_test))

    rd = Ridge(alpha=1.0)
    rd.fit(x_train, y_train)
    print('岭回归:',rd.coef_)
    print(rd.score(x_test, y_test))

    # 梯度下降
    sgd = SGDRegressor()
    sgd.fit(x_train, y_train)
    print('梯度下降',sgd.coef_)

    sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    #print("梯度下降：", sgd_predict)
    print(mean_squared_error(std_y.inverse_transform(y_test), sgd_predict))
    print(sgd.score(x_test, y_test))
    for i in range(len(sgd_predict)):
        print(sgd_predict[i],std_y.inverse_transform(y_test)[i])

    # lr = LinearRegression()  # 线性回归 对原来训练集测试
    # lr.fit(x_train, y_train)
    # print(lr.coef_)
    # print(lr.score(x_train, y_train))
    # y_predict = std_y.inverse_transform(lr.predict(x_train))
    # for i in range(len(y_predict)):
    #     print(y_predict[i],std_y.inverse_transform(y_train)[i])




if __name__ == '__main__':
    bike()