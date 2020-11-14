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
    data_value = sorted(data_value)
    #print(data_value)
    # data_value = data_value[0:1000]
    return data_value

def distance(x1,x2,y1,y2):
    a = (float(x1)-float(x2))**2+(float(y1)-float(y2))**2
    if(math.sqrt(a)<50):
        return 1
    else:
        return 0

def fenlei():
    data = get_data()
    n = len(data)
    cluster = [-1]*n
    print(cluster)
    for i in range(n):
        print(1)
    return None

start = time.perf_counter()
fenlei()
elapsed = (time.perf_counter() - start)
print("Time used:",elapsed)

