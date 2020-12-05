import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor,Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import random


def jianhang():
    x_data = pd.read_csv('insurance.csv', usecols=[0, 2]).values#读取数据 ,usecols为指定读取列数
    y_data = pd.read_csv('insurance.csv', usecols=[6]).values

    randnum = random.randint(0, len(x_data))  # 随机选取，打乱
    random.seed(randnum)
    random.shuffle(x_data)
    random.seed(randnum)
    random.shuffle(y_data)
    x_train, x_test, y_train, y_test = x_data[0:int(len(x_data)*0.75)],x_data[int(len(x_data)*0.75):len(x_data)],y_data[0:int(len(y_data)*0.75)],y_data[int(len(y_data)*0.75):len(y_data)]

    std_x = StandardScaler()  # 标准化
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    print(x_train)

    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))  # 二维数组
    y_test = std_y.transform(y_test.reshape(-1, 1))
    print(y_train)


    lr = LinearRegression()
    lr.fit(x_train,y_train)
    print(lr.coef_)
    y_predict = lr.predict(x_test)  # 预测
    print(y_predict)
    print(mean_squared_error(y_test, y_predict))
    print(lr.score(x_test, y_test))



if __name__ == '__main__':
    jianhang()
    print('ceshi')