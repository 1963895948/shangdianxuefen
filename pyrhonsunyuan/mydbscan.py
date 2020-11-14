import math
import time

def get_data():#获取数据，生成一个二维列表，每一个坐标点为一个列表
    data_value = []
    with open("data.txt", "r") as f:
        for line in f.readlines():
            data_value_1 = []
            line = line.split()
            data_value_1.append(float(line[0]))
            data_value_1.append(float(line[1]))
            data_value.append(data_value_1)

    data_value = sorted(data_value, key=(lambda x: x[0]))#按横坐标排序
    #data_value = data_value[1:1000]
    return data_value

def distance(x1,x2,y1,y2):
    a = (float(x1)-float(x2))**2+(float(y1)-float(y2))**2
    return math.sqrt(a)


def my_2(r):#用标记做，
    """
    思路为先给每个位置做标记，处理过的就标号，下次直接跳过
    让后从第一个节点开始，将与他距离50以内的点收入列表
    然后在对列表读取，每一个节点又判断与之相关的点，置入列表
    知道列表读取完，就表明一类已经读取了
    :return:
    """
    data = get_data()
    n = len(data)
    cluster = [-1]*n
    k = -1
    for i in range(n):
        if(cluster[i] != -1):
            continue
        for index_data in range(i,n):#由于数据太大，先找到与该数据横坐标相聚50以内的点
            if((data[i][0]-data[index_data][0]+50)>0):
                index_f = index_data
            else:
                break
        for index_data in range(i,-1,-1):
            if((data[i][0]-data[index_data][0]-50)<0):
                index_h = index_data
            else:
                break
        print(index_h,index_f)
        subdataset = [j for j in range(index_h,index_f+1) if
                      (distance(data[j][0], data[i][0], data[j][1], data[i][1]) < r)]

        k+=1
        cluster[i]= k
        #print(subdataset)
        for j in subdataset:
            cluster[j] = k
            for index_data in range(j + 1, n):
                if ((data[j][0] - data[index_data][0] + 50) > 0):
                    index_f = index_data
                else:
                    break
            for index_data in range(i, -1, -1):
                if ((data[i][0] - data[index_data][0] - 50) < 0):
                    index_h = index_data
                else:
                    break
            sub = [item for item in range(index_h,index_f+1) if(distance(data[j][0],data[item][0],data[j][1],data[item][1])<r)]
            for t in sub:
                if(t not in subdataset):
                    subdataset.append(t)
        print(subdataset)
    return cluster


start = time.perf_counter()
cluster = my_2(50)
print(cluster)
print(max(cluster)+1)
elapsed = (time.perf_counter() - start)
print("Time used:",elapsed)