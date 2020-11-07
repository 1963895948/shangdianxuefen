import numpy as np
import xlrd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def data_pro():#数据处理
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
    return data_x

def datay():
    readxls = xlrd.open_workbook("exchange.xlsx")  # 读取文件，建立工作铺
    names = readxls.sheet_names()  # 输出工作铺中的表
    # print(names)

    worksheet = readxls.sheet_by_index(0)  # 打开第一个表
    return worksheet.col_values(13)[1:]

def aic():#这里没有理解完，那个sse不知道会不会变化，暂时留着
    aic_vlaue = 0
    return aic_vlaue

def get_sse():#获取sse，但是不知道会不会随着进入模型的变量而改变
    data_y = datay()
    data_y = np.array(data_y).reshape(-1, 1)
    sse = 0
    data = data_pro()
    for i in range(len(data)):#每一个变量做线性回归
        x = np.array(data[i]).reshape(-1, 1)
        lr = LinearRegression()
        lr.fit(x, data_y)
        sse = sse +mean_squared_error(lr.predict(x),data_y)#sse
    return sse

def get_ssr(data,data_x):#求ssr
    data_y = datay()
    vga_y = float(sum(data_y))/len(data_y)
    data_y = np.array(data_y).reshape(-1, 1)

    ssr = 0
    for i in range(len(data)):
        x = []
        for j in range(len(data_x)):
            x.append(data_x[j])
        x.append(data[i])
        x = np.array(x)#.reshape(-1,len(data_x)+1)#.reshape(-1, 1)
        x = np.transpose(x)
        #print(x)
        lr = LinearRegression()
        #print(x.shape)
        #print(data_y.shape)
        lr.fit(x, data_y)
        #print(lr.coef_)
        #print(lr.predict(x))
        ssr = ssr + sum((lr.predict(x)-vga_y)**2)  # sse
    #print(ssr)
    return float(ssr)


def ftest(data,data_x,sse):#回归系数显著检验 ，F检验
    ssr = get_ssr(data,data_x)

    list_ssr = []
    for i in range(len(data)):
        data_test = []
        for j in range(len(data)):
            if(i != j):
                data_test.append(data[j])
        #print(data_test)
        list_ssr.append(get_ssr(data_test,data_x))
    #print(ssr)
    #print(list_ssr)

    for i in range(len(list_ssr)):
        t = sse/(31-len(data)-1)
        list_ssr[i] = (ssr - list_ssr[i]) / t
    print('F检验值:',list_ssr)

    index = list_ssr.index(max(list_ssr))#求f测试值最大的变量位置

    print('剔除',index+1)

    data_x.append(data[index])
    data_test = []
    for i in range(len(data)):
        if(i != index):
            data_test.append(data[i])
    data = data_test
    return data,data_x

def head(data):
    #print(data)
    sse = get_sse()
    data_x = []  # 已经选取的x
    for i in  range(len(data)):
        data ,data_x = ftest(data,data_x,sse)
        #这里时aic，但现在不会
    return None

def lear():
    return None

def huigui():
    return None


data = data_pro()
head(data)
#get_sse()