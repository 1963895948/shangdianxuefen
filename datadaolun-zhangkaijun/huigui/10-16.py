import datetime
import numpy as np
import pandas as pd
import time
from sklearn.datasets import load_boston
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import random

def data():
    x_data = pd.read_csv('forestfires.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10]).values
    print(x_data)
    y_data = pd.read_csv('forestfires.csv', usecols=[12]).values
    #print(x_data[0:int(len(x_data)*0.75)])
    time_str = pd.read_csv('forestfires.csv', usecols=[2,3])
    # 将文字特征转化为数字
    for i in range(len(x_data)):
        #print(x_test.values[i])
        str2 = ','.join(time_str.values[i])
        time_format = datetime.datetime.strptime(str2, '%b,%a')
        #print(time_format.month)  # 求月份
        #print(time_format)
        lis = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', ]
        #print(lis.index(time_str.values[i][1])+1)#求周几
        #print(x_test.values[i][2])
        x_data[i][2] = time_format.month
        #print(x_data[i][2])
        x_data[i][3] = lis.index(x_data[i][3])+1
    print(x_data)

    x_train, x_test, y_train, y_test = x_data[0:int(len(x_data)*0.75)],x_data[int(len(x_data)*0.75):len(x_data)],y_data[0:int(len(y_data)*0.75)],y_data[int(len(y_data)*0.75):len(y_data)]
    #print(x_train, x_test, y_train, y_test)
    std_x = StandardScaler()  # 标准化
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    print(x_train)

    print(y_train)
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))  # 二维数组
    y_test = std_y.transform(y_test.reshape(-1, 1))
    print(y_train)

    lr = LinearRegression()  # 线性回归
    lr.fit(x_train, y_train)
    print(lr.coef_)
    y_predict = std_y.inverse_transform(lr.predict(x_test))  # 预测
    print(y_predict)
    print(mean_squared_error(std_y.inverse_transform(y_test), y_predict))
    print(lr.score(x_test, y_test))

    # 梯度下降
    sgd = SGDRegressor()
    sgd.fit(x_train, y_train)
    print(sgd.coef_)

    sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    print("梯度下降：", sgd_predict)
    print(mean_squared_error(std_y.inverse_transform(y_test), sgd_predict))
    print(sgd.score(x_test, y_test))

    return None

def fires_plus():
    x_data = pd.read_csv('forestfires.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10]).values
    #print(x_data)
    y_data = pd.read_csv('forestfires.csv', usecols=[12]).values
    #print(x_data[0:int(len(x_data)*0.75)])
    time_str = pd.read_csv('forestfires.csv', usecols=[2,3])
    # 将文字特征转化为数字
    for i in range(len(x_data)):
        #print(x_test.values[i])
        str2 = ','.join(time_str.values[i])
        time_format = datetime.datetime.strptime(str2, '%b,%a')
        #print(time_format.month)  # 求月份
        #print(time_format)
        lis = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', ]
        #print(lis.index(time_str.values[i][1])+1)#求周几
        #print(x_test.values[i][2])
        x_data[i][2] = time_format.month
        #print(x_data[i][2])
        x_data[i][3] = lis.index(x_data[i][3])+1
    #print(x_data)
    print(x_data)
    #print(y_data)
    # x_test1 = x_data.copy()
    # print(x_test1)
    randnum = random.randint(0, len(x_data))#随机选取，打乱
    random.seed(randnum)
    random.shuffle(x_data)
    random.seed(randnum)
    random.shuffle(y_data)
    print(x_data)
    #print(y_data)


    x_train, x_test, y_train, y_test = x_data[0:int(len(x_data)*0.75)],x_data[int(len(x_data)*0.75):len(x_data)],y_data[0:int(len(y_data)*0.75)],y_data[int(len(y_data)*0.75):len(y_data)],
    #print(x_train, x_test, y_train, y_test)

    std_x = StandardScaler()  # 标准化
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    print(x_train)


    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))  # 二维数组
    y_test = std_y.transform(y_test.reshape(-1, 1))
    print(y_train)

    lr = LinearRegression()  # 线性回归
    lr.fit(x_train, y_train)
    print(lr.coef_)
    y_predict = std_y.inverse_transform(lr.predict(x_test))  # 预测
    print(y_predict)
    print(mean_squared_error(std_y.inverse_transform(y_test), y_predict))
    print(lr.score(x_test,y_test))

    # 梯度下降
    sgd = SGDRegressor()
    sgd.fit(x_train, y_train)
    print(sgd.coef_)


    sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    print("梯度下降：", sgd_predict)
    print(mean_squared_error(std_y.inverse_transform(y_test), sgd_predict))
    print(lr.score(x_test, y_test))



    return None

def fires_plus_1():
    x_data = pd.read_csv('forestfires.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10]).values
    #print(x_data)
    y_data = pd.read_csv('forestfires.csv', usecols=[12]).values
    #print(x_data[0:int(len(x_data)*0.75)])
    time_str = pd.read_csv('forestfires.csv', usecols=[2,3])
    # 将文字特征转化为数字
    for i in range(len(x_data)):
        #print(x_test.values[i])
        str2 = ','.join(time_str.values[i])
        time_format = datetime.datetime.strptime(str2, '%b,%a')
        #print(time_format.month)  # 求月份
        #print(time_format)
        lis = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', ]
        #print(lis.index(time_str.values[i][1])+1)#求周几
        #print(x_test.values[i][2])
        x_data[i][2] = time_format.month
        #print(x_data[i][2])
        x_data[i][3] = lis.index(x_data[i][3])+1
    #print(x_data)
    print(x_data)
    #print(y_data)
    # x_test1 = x_data.copy()
    # print(x_test1)

    randnum = random.randint(0, len(x_data))#随机选取，打乱
    random.seed(randnum)
    random.shuffle(x_data)
    random.seed(randnum)
    random.shuffle(y_data)
    print(x_data)
    #print(y_data)


    x_train, x_test, y_train, y_test = x_data[0:int(len(x_data)*0.75)],x_data[int(len(x_data)*0.75):len(x_data)],y_data[0:int(len(y_data)*0.75)],y_data[int(len(y_data)*0.75):len(y_data)],
    #print(x_train, x_test, y_train, y_test)

    # std_x = StandardScaler()  # 标准化
    # x_train = std_x.fit_transform(x_train)
    # x_test = std_x.transform(x_test)
    # print(x_train)
    #
    #
    # std_y = StandardScaler()
    # y_train = std_y.fit_transform(y_train.reshape(-1, 1))  # 二维数组
    # y_test = std_y.transform(y_test.reshape(-1, 1))
    # print(y_train)

    lr = LinearRegression()  # 线性回归
    lr.fit(x_train, y_train)
    print(lr.coef_)
    y_predict = lr.predict(x_test)  # 预测
    print(y_predict)
    print(mean_squared_error(y_test, y_predict))
    print(lr.score(x_test,y_test))

    # 梯度下降
    sgd = SGDRegressor()
    sgd.fit(x_train, y_train)
    print(sgd.coef_)




    return None





if __name__ == '__main__':
    data()
    #fires_plus_1()