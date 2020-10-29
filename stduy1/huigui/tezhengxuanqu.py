import numpy as np
import xlrd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def data_pro():
    readxls  = xlrd.open_workbook("exchange.xlsx")#读取文件，建立工作铺
    names = readxls.sheet_names()#输出工作铺中的表
    #print(names)

    worksheet = readxls.sheet_by_index(0)#打开第一个表
    #print(worksheet)

    nrows = worksheet.nrows #读取行数
    #print(nrows)
    ncols = worksheet.ncols#读取列数
    #print(ncols)


    data_x = []
    for i in range(ncols-2):
        data_x.append(worksheet.col_values(i)[1:])

    # print(data_x)
    # print(data_x.pop(11))
    # print(data_x)


    return data_x

def datay():
    readxls = xlrd.open_workbook("exchange.xlsx")  # 读取文件，建立工作铺
    names = readxls.sheet_names()  # 输出工作铺中的表
    # print(names)

    worksheet = readxls.sheet_by_index(0)  # 打开第一个表
    return worksheet.col_values(13)[1:]

def aic():
    aic_vlaue = 0
    return aic_vlaue


def ftest(data):#回归系数显著检验 ，F检验
    data_y = datay()
    data_y = np.array(data_y).reshape(-1, 1)

    for i in range(len(data)):
        x = np.array(data[i]).reshape(-1, 1)
        lr = LinearRegression()
        lr.fit(x, data_y)
        #print(lr.coef_)
        #print(mean_squared_error(lr.predict(x),data_y))#sse
        print(x)



    return None

def head(data):
    #print(data)
    ftest(data)



    return None

def lear():
    return None

def huigui():
    return None


data = data_pro()
head(data)
