import math
import time
import matplotlib.pyplot as plt

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

def knn():#相当于聚类
    data = get_data()
    class_count = []#类别
    while( len(data)!= 0):
        class_count_index = []
        print(data[0])
        print('第%d类'%len(class_count),class_count_index)
        class_count_index.append(data.pop(0))
        index = 0
        while(index != len(class_count_index)):
            for data_cell in data:
                #print(distance(data[i][0],class_count_index[index][0],data[i][1],class_count_index[index][1]))
                if(distance(data_cell[0],class_count_index[index][0],data_cell[1],class_count_index[index][1])< 50):
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


start = time.perf_counter()
knn()
elapsed = (time.perf_counter() - start)
print("Time used:",elapsed)






