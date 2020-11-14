'''
data.txt中是多个点的坐标集合S，
每个点的坐标都是一个二维数组，每一行代表一个点的二维坐标，二维数组的第一个列表代表横坐标，第二个列表代表纵坐标。
现有如下想法，大致内容如下:
设置一个正的常数值d=50，对于集合S中任意两个点，只要它们两个之间的欧式距离不超过d，那么这两点就归为一类。
请尝试自行编写python代码实现上述想法，并显示代码运行时间和最后S被划分成了多少个类。
 '''

__author__='洪浩腾'
import  os
import  math
import datetime




# 将文本内容转换为数组
def get_arr ():
    # 项目根目录
    root_dir = os.path.dirname(os.path.abspath(__file__))
    # data文本目录
    text_dir = os.path.join(root_dir, 'data.txt')
    list=[]
    list_x=[]
    list_y=[]
    # 读取文本信息
    data = open(text_dir)
    lines = data.readlines()
    for line in lines:
         str=line.replace("\n","").split("\t")
         # 构造存储点数据的列表
         list_x.append(float(str[0]))
         list_y.append(float(str[1]))
    data.close()
    list.append(list_x)
    list.append(list_y)
    return list

# 计算欧式距离
def calculate_distance(x1,y1,x2,y2):
    print(math.sqrt(
        sum(
            [math.pow((x1-x2),2), math.pow((y1-y2),2)]
        )))
    return math.sqrt(
        sum(
            [math.pow((x1-x2),2), math.pow((y1-y2),2)]
        )
    )

# 计算点的类别
def divide():
    # 开始执行时间
    starttime = datetime.datetime.now()
    list=get_arr()
    list_x=list[0]
    list_y=list[1]
    n = len(list_x)
    count=0
    cluster = [-1] * n
    k = -1
    for index_x1 in range(n):
        if(cluster[index_x1] != -1):
            continue
        x1 =list_x[index_x1]
        y1 =list_y[index_x1]
        subdataset = [j for j in range(n) if (calculate_distance(x1, y1, list_x[j], list_y[j])<=50)]
        k += 1
        cluster[index_x1] = k
        print(subdataset)
        for j in subdataset:
            cluster[j] = k
            if(j>index_x1):
                print('距离',calculate_distance(list_x[index_x1],list_y[index_x1],list_x[j],list_y[j]))
                sub = [item for item in range(index_x1,n) if(calculate_distance(list_x[index_x1],list_y[index_x1],list_x[j],list_y[j])<=50)]
                print(sub)
                for t in sub:
                    if(t not in subdataset):
                        subdataset.append(t)
        print(subdataset)
        # for index_x2,index_y2 in zip(range(index_x1+1,len(list_x)),range(index_y1+1,len(list_y))):#本身没有问题，但是时间复杂度为n**n
        #     x2 = list_x[index_x2]
        #     y2 = list_y[index_y2]
        #     distance = calculate_distance(float(x1),float(y1),float(x2),float(y2))
        #     if(distance<=50):
        #        count=count+1
        #        print("点("+x1+","+y1+"),("+x2+","+y2+")配对成功")

    # 结束执行时间
    print(len(set(cluster)))
    endtime = datetime.datetime.now()
    time=(endtime - starttime).seconds
    print("运行时间="+str(time)+"，共计"+str(count)+"个点配对")





divide()



