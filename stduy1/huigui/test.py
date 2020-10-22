import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor,Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd



def jianhang():
    x_data = pd.read_csv('hour.csv',usecols=[0,1,2,3,4,5]).values#读取数据 ,usecols为指定读取列数
    y_data = pd.read_csv('insurance.csv',usecols=[6]).values

    print(x_data)

    #

    # y_predict = lr.predict(x_test)  # 预测
    # print(y_predict)
    #print(mean_squared_error(std.inverse_transform(y_test), y_predict))



if __name__ == '__main__':
    jianhang()