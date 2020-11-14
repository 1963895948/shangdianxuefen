import math
import time
from sklearn.cluster import DBSCAN
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
    #data_value = sorted(data_value)
    #print(data_value)
    # data_value = data_value[0:1000]
    return data_value

def distance(x1,x2,y1,y2):
    a = (float(x1)-float(x2))**2+(float(y1)-float(y2))**2
    return math.sqrt(a)

def knn():#相当于聚类，每有一个可划分数据就拿掉，用时340ms
    data = get_data()
    class_count = []#类别
    while( len(data)!= 0):
        class_count_index = []
        print('第%d类'%len(class_count))
        class_count_index.append(data.pop(0))
        index = 0
        while(index != len(class_count_index)):
            for data_cell in data:
                #print(distance(data[i][0],class_count_index[index][0],data[i][1],class_count_index[index][1]))
                if(distance(data_cell[0],class_count_index[index][0],data_cell[1],class_count_index[index][1])<= 50):
                    class_count_index.append(data.pop(data.index(data_cell)))
                    #print(len(data))
            index = index+1
        print(class_count_index)
        class_count.append(class_count_index)

    #print(class_count)
    return class_count



def my_2():#用标记做，用时720ms
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

def dbscan():#用机器学习的包，用时0.52ms
    data = np.loadtxt("data.txt")
    db =DBSCAN(eps=50,min_samples=0).fit(data[1:1000])
    labels = db.labels_
    print(max(labels)+1)

    return None


def merge_list(L):
    lenth = len(L)
    for i in range(0, lenth):
        for j in range(i):
            if L[i] == [-1] or L[j] == [-1]:
                continue
            x = list(set(L[i]+L[j]))
            y = len(L[i]) + len(L[j])
            if len(x) < y:
                L[i] = x
                L[j] = [-1]

    return [i for i in L if i != [-1]]

def my_3():#用标记做，倒转
    data = get_data()
    n = len(data)
    cluster = [-1]*n
    k = -1
    zhen = []
    fan = []
    for i in range(n):
        print(i)
        if(cluster[i] != -1):
            continue
        subdataset = [j for j in range(n) if(distance(data[j][0],data[i][0],data[j][1],data[i][1])<=50)]
        k+=1
        cluster[i]= k
        print(subdataset)
        zhen.append(subdataset)
        for j in subdataset:
            cluster[j] = k
        #         print(sub)

    data_rev = get_data()[::-1]
    cluster_rev = [-1] * n
    k = -1
    for i in range(n):
        print(i)
        if (cluster_rev[i] != -1):
            continue
        subdataset = [j for j in range(n) if (distance(data_rev[j][0], data_rev[i][0], data_rev[j][1], data_rev[i][1]) <= 50)]
        k += 1
        cluster_rev[i] = k

        for j in subdataset:
            cluster_rev[j] = k
        print(subdataset)
        for i in range(len(subdataset)):
            subdataset[i] = n - subdataset[i] - 1
        fan.append(subdataset)
        #         print(sub)
    hebin = zhen+fan
    hebin = merge_list(hebin)
    print(sorted(hebin))
    dic = list(set([tuple(t) for t in hebin]))
    hebin = [list(v) for v in dic]
    print(len(hebin))
    return None

# start = time.perf_counter()
# knn()
# elapsed = (time.perf_counter() - start)
# print("Time used:",elapsed)

#
# start = time.perf_counter()
# cluster = my_2()
# print(cluster)
# print(max(cluster))
# elapsed = (time.perf_counter() - start)
# print("Time used:",elapsed)

start = time.perf_counter()
dbscan()
elapsed = (time.perf_counter() - start)
print("Time used:",elapsed)


