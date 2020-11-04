import math
import time
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np

def get_data():
    data_value = []
    with open("data.txt", "r") as f:
        for line in f.readlines():
            data_value_1 = []
            #line = line.strip('\n')  #去掉列表中每一个元素的换行符
            line = line.split()
            #print(line[0],line[1])
            data_value_1.append(line[0])
            data_value_1.append(line[1])
            #print(data_value_1)
            data_value.append(data_value_1)
    return data_value

def distance(x1,x2,y1,y2):
    a = (float(x1)-float(x2))**2+(float(y1)-float(y2))**2
    return math.sqrt(a)

def knn():#相当于聚类，每有一个可划分数据就拿掉
    data = get_data()
    class_count = []#类别
    while( len(data)!= 0):
        class_count_index = []
        print(data[0])
        print('第%d类'%len(class_count))
        class_count_index.append(data.pop(0))
        index = 0
        while(index != len(class_count_index)):
            for data_cell in data:
                #print(distance(data[i][0],class_count_index[index][0],data[i][1],class_count_index[index][1]))
                if(distance(data_cell[0],class_count_index[index][0],data_cell[1],class_count_index[index][1])< 20):
                    class_count_index.append(data.pop(data.index(data_cell)))
                    #print(len(data))
            index = index+1
        print(class_count_index)
        class_count.append(class_count_index)

    #print(class_count)
    return class_count


def huatu():
    data = get_data()
    for i in data[0:10]:
        print(i)
        plt.scatter(i[0], i[1])
    plt.show()


def dbscan():#用标记做
    data = get_data()
    n = len(data)
    cluster = [-1]*n
    k = -1
    for i in range(n):
        print(i)
        if(cluster[i] != -1):
            continue
        subdataset = [j for j in range(n) if(distance(data[j][0],data[i][0],data[j][1],data[i][1])<=50)]
        k+=1
        cluster[i]= k
        print(subdataset)
        for j in subdataset:
            cluster[j] = k
            if(j>i):
                sub = [item for item in range(i,n) if(distance(data[j][0],data[item][0],data[j][1],data[item][1])<=50)]
                for t in sub:
                    if(t not in subdataset):
                        subdataset.append(t)
        #         print(sub)
        print(subdataset)
    return cluster

def dbscan_1():#用机器学习的包
    data = np.loadtxt("/Users/yuanxiaoguo/PycharmProjects/shangdianxuefen/stduy1/pyrhonsunyuan/data.txt")
    db =DBSCAN(eps=20,min_samples=1).fit(data)
    labels = db.labels_
    print(max(labels)+1)
    return None

# start = time.perf_counter()
# knn()
# elapsed = (time.perf_counter() - start)
# print("Time used:",elapsed)


#
# start = time.perf_counter()
# cluster = dbscan()
# print(cluster)
# print(max(cluster))
# elapsed = (time.perf_counter() - start)
# print("Time used:",elapsed)

start = time.perf_counter()
dbscan_1()
elapsed = (time.perf_counter() - start)
print("Time used:",elapsed)