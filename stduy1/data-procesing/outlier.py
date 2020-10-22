import math

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def z_sorce_out():
    csv_data = pd.read_csv('accord_sedan_testing.csv', usecols=[1])
    col_data = []
    for i in csv_data.values:
        col_data.append(i[0])
    print(col_data)

    nrows = len(col_data)
    average = float(sum(col_data))/nrows  #均值
    total = 0
    for value in col_data:
        total += (value - average)**2
    stddev = math.sqrt(total/nrows)

    csv_data = pd.read_csv('accord_sedan_training.csv', usecols=[1])
    col_data1 = []
    for i in csv_data.values:
        col_data1.append(i[0])
    print(col_data1)

    a = [(x-average)/stddev for x in col_data1]
    print(a)
    for i in a:
        if(i>=3 or i<=-3):
            print(1000)


def data_deal(str):
    csv_data = pd.read_csv(str, usecols=[0,1])#读取特征数据数据
    return csv_data.values

def calc_distance(train,test):
    distance = []
    for i in range(len(test)):
        distance_value = []
        for j in range(len(train)):
            temp = np.subtract(train[j],test[i]) #对应元素相减
            temp = np.power(temp,2) #对应元素分别平方
            distance_value.append(np.sqrt(temp.sum())) #现求和再开平方
        distance.append(distance_value)
    return distance






def knn():
    train = data_deal('accord_sedan_training.csv')
    test = data_deal('accord_sedan_testing.csv')
    distance = calc_distance(train,test)
    # distance = distance[0]
    # k_list =sorted(distance)[0:5]
    # print(test[0])
    # for i in range(len(distance)):
    #     if(distance[i] in k_list):
    #         print(train[i])
    # print(sorted(distance)[0:5])

    a = []
    for i in range(len(distance)):
        a.append(max(distance[i]))
    print(max(a),a.index(max(a)))
    count = 0
    for i in range(len(distance)):
        k_list = sorted(distance[i])[0:5]
        if(sum(k_list)>4000):
            print(i)
            count+=1
            print(k_list)
    print(count)

def matlp():
    train = data_deal('accord_sedan_training.csv')
    test = data_deal('accord_sedan_testing.csv')
    print(train)
    x1 = []
    y1 = []
    for i in range(len(train)):
        x1.append(train[i][0])
        y1.append(train[i][1])

    print(len(x1),len(y1))
    x2 = []
    y2 = []
    for i in range(len(test)):
        x2.append(test[i][0])
        y2.append(test[i][1])

    print(len(x2), len(y2))
    plt.figure()

    plt.scatter(x1,y1)
    plt.scatter(x2,y2)

    plt.show()






#z_sorce_out()
#knn()
matlp()