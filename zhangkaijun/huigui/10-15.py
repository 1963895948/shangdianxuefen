import numpy as np
import pandas as pd


def cost_function(a, b, x, y):#损失率
    n = 5
    return 0.5/n * (np.square(y-a*x-b)).sum()


def liner():
    x = [13854, 12213, 11009, 10655, 9503]  # 程序员工资，顺序为北京，上海，杭州，深圳，广州
    x = np.reshape(x, newshape=(5, 1)) / 10000.0
    print('x:',x)
    y = [21332, 20162, 19138, 18621, 18016]  # 算法工程师，顺序和上面一致
    y = np.reshape(y, newshape=(5, 1)) / 10000.0

    xt = np.transpose(x)#矩阵转置
    print('xt:',xt)

    tow_multi = np.dot(xt,x)#矩阵乘法
    print(tow_multi)

    inv  = np.linalg.inv(tow_multi)#矩阵的逆

    t = np.dot(inv,xt)
    t = np.dot(t,y)
    print('w:',t)
    return None

def data():
    x_test = pd.read_csv('forestfires.csv', usecols=[0, 4, 5, 6, 7, 8, 9, 10])
    y_test = pd.read_csv('forestfires.csv', usecols=[1])
    print(x_test[0:int(len(x_test)*0.75)])



    #将文字特征转化为数字

    #分割数据比例为3比1
    #x_train, x_test, y_train, y_test =

    #线性预测

    return None


if __name__ == '__main__':
    #data()
    liner()
