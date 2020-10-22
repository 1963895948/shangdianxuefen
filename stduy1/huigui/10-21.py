import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor,Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd


def dummycoding(dataframe):
    dataframe_age = dataframe['age']
    dataframe_bmi = dataframe['bmi']
    dataframe_children = dataframe['children']
    dataframe_charges = dataframe['charges']
    dataframe_1 = dataframe.drop(['age'], axis=1)#去掉列名为age的列，默认为行，当axis为1时，去列
    dataframe_2 = dataframe_1.drop(['bmi'], axis=1)#这里可以只用dataframe_new
    dataframe_3 = dataframe_2.drop(['children'], axis=1)
    dataframe_new = dataframe_3.drop(['charges'], axis=1)

    dataframe_new = pd.get_dummies(dataframe_new, prefix=dataframe_new.columns).astype(int)
    #当无关列删掉时，就可以进行虚拟编码
    dataframe_new['age'] = dataframe_age#将之前删掉的列重新加入数据框
    dataframe_new['bmi'] = dataframe_bmi
    dataframe_new['children'] = dataframe_children
    dataframe_new['charges'] =dataframe_charges
    return dataframe_new

def jianhang():
    x_data = pd.read_csv('insurance.csv')#读取数据 ,usecols为指定读取列数
    print('费用',x_data["charges"].describe())#特征分析
    # plt.hist(x_data["charges"])
    # plt.xlabel('charges')
    # plt.show()

    print('\n性别信息\n',x_data["sex"].describe())
    print('\n是否吸烟信息\n',x_data["smoker"].describe())
    print('\n地区分布信息\n',x_data["region"].describe())
    print('\n分布状况\n',x_data.region.value_counts())

    print(x_data[['age','bmi','children','charges']].corr())#相关系数矩阵
    insurance_lm = dummycoding(x_data)

    lr = LinearRegression()#进行线性回归api

    dataframe_charges = insurance_lm['charges']
    insurance_lm = insurance_lm.drop(['charges'], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(insurance_lm,dataframe_charges,test_size=0.25)

    x_train =x_train.values
    x_test =x_test.values
    y_train = y_train.values.reshape(-1, 1)
    y_test = y_test.values.reshape(-1, 1)
    print(y_test)

    print(y_test.shape)

    std_x = StandardScaler()#标准化
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.fit(x_test)


    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train)
    y_test = std_y.fit(y_test)
    print(type(y_test))
    print(y_test)



    lr = LinearRegression()
    lr.fit(x_train,y_train)
    print(lr.coef_)

    # y_predict = lr.predict(x_test)  # 预测
    # print(y_predict)
    #print(mean_squared_error(std.inverse_transform(y_test), y_predict))



if __name__ == '__main__':
    jianhang()