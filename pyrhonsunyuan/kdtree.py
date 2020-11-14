import numpy as np
from math import sqrt
import time

def get_data():
    data_value = []
    with open("data.txt", "r") as f:
        for line in f.readlines():
            data_value_1 = []
            #line = line.strip('\n')  #去掉列表中每一个元素的换行符
            line = line.split()
            #print(line[0],line[1])
            data_value_1.append(float(line[0]))
            data_value_1.append(float(line[1]))
            #print(data_value_1)
            data_value.append(data_value_1)
    data_value = sorted(data_value)
    #print(data_value)
    # data_value = data_value[0:1000]
    print(data_value)
    return data_value

class KDNode(object):
    def __init__(self, value, split, left, right):
        # value=[x,y]
        self.value = value
        self.split = split
        self.right = right
        self.left = left


class KDTree(object):
    def __init__(self, data):
        # data=[[x1,y1],[x2,y2]...,]
        # 维度
        k = len(data[0])

        def CreateNode(split, data_set):
            if not data_set:
                return None
            data_set.sort(key=lambda x: x[split])
            # 整除2
            split_pos = len(data_set) // 2
            median = data_set[split_pos]
            split_next = (split + 1) % k
            return KDNode(median, split, CreateNode(split_next, data_set[: split_pos]),
                          CreateNode(split_next, data_set[split_pos + 1:]))

        self.root = CreateNode(0, data)

    def search(self, root, x, count=500):
        nearest = []
        for i in range(count):
            nearest.append([-1, None])
        self.nearest = np.array(nearest)
        def recurve(node):
            if node is not None:
                axis = node.split
                daxis = x[axis] - node.value[axis]
                if daxis < 0:
                    recurve(node.left)
                else:
                    recurve(node.right)
                dist = sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(x, node.value)))
                for i, d in enumerate(self.nearest):
                    if d[0] < 0 or dist < d[0]:  # 如果当前nearest内i处未标记（-1），或者新点与x距离更近
                        self.nearest = np.insert(self.nearest, i, [dist, node.value], axis=0)  # 插入比i处距离更小的
                        self.nearest = self.nearest[:-1]
                        break
                # 找到nearest集合里距离最大值的位置，为-1值的个数
                n = list(self.nearest[:, 0]).count(-1)
                # 切分轴的距离比nearest中最大的小（存在相交）
                if self.nearest[-n - 1, 0] > abs(daxis):
                    if daxis < 0:  # 相交，x[axis]< node.data[axis]时，去右边（左边已经遍历了）
                        recurve(node.right)
                    else:  # x[axis]> node.data[axis]时，去左边，（右边已经遍历了）
                        recurve(node.left)

        recurve(root)
        return self.nearest


def my_2():
    data = get_data()
    kd = KDTree(data)
    n = len(data)
    cluster = [-1]*n
    k = -1
    for i in range(n):
        print(i)
        if(cluster[i] != -1):
            continue
        sum_eps = kd.search(kd.root,[data[i][0],data[i][1]])
        subdataset = []
        for i in range(len(sum_eps)):
            if(sum_eps[i][0]<50):
                subdataset.append(data.index(sum_eps[i][1]))
        print(subdataset)
        k += 1
        cluster[i] = k
        for j in subdataset:
            cluster[j] = k
            if (j > i):
                sub = []
                sum_eps = kd.search(kd.root, [data[j][0], data[j][1]])
                for i in range(len(sum_eps)):
                    if (sum_eps[i][0] < 50):
                        sub.append(data.index(sum_eps[i][1]))
                for t in sub:
                    if (t not in subdataset):
                        subdataset.append(t)
    return cluster

#
# 最近坐标点、最近距离和访问过的节点数
# result = namedtuple("Result_tuple", "nearest_point nearest_dist nodes_visited")
start = time.perf_counter()
my_2()

#n = kd.search(kd.root, [13139.9,3026.9])
#print(n)
elapsed = (time.perf_counter() - start)
print("Time used:",elapsed)

