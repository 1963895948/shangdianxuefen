import numpy as np
import xlrd
from sklearn.linear_model import Ridge,Lasso,SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


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
    data_x.append(worksheet.col_values(i)[1:])#获取x数据

readxls = xlrd.open_workbook("exchange.xlsx")  # 读取文件，建立工作铺
names = readxls.sheet_names()  # 输出工作铺中的表
# print(names)
worksheet = readxls.sheet_by_index(0)  # 打开第一个表
data_y = worksheet.col_values(13)[1:]#获取y的数据

#print(data_x)
#训练集和测试集
x_train , x_test = [],[]
for i in range(len(data_x)):
    x_train.append(data_x[i][:22])
    x_test.append(data_x[i][22:])
#print(x_test)
x_train = list(  zip(*x_train) )#转置
x_test = list(  zip(*x_test) )
print(x_train)
y_train , y_test = np.array(data_y[:22]).reshape(-1,1),np.array(data_y[22:]).reshape(-1,1)
print(y_test)


#数据标准化
std_x = StandardScaler()
x_train = std_x.fit_transform(x_train)
x_test = std_x.transform(x_test)
#print(x_train)

std_y = StandardScaler()
y_train = std_y.fit_transform(y_train)
y_test = std_y.transform(y_test)
#print(y_train)

# print(x_train,y_train)
#岭回归
rd = Ridge()
rd.fit(x_train, y_train)
print('岭回归系数',rd.coef_)
print('预测值',std_y.inverse_transform(rd.predict(x_test)))
print('预测率',rd.score(x_test,y_test))
print('方差',mean_squared_error(std_y.inverse_transform(y_test),std_y.inverse_transform(rd.predict(x_test))))

# sgd = SGDRegressor()
# sgd.fit(x_train, y_train)
# print(sgd.coef_)
# print(std_y.inverse_transform(sgd.predict(x_test)))
# print(sgd.score(x_test,y_test))
# print(mean_squared_error(std_y.inverse_transform(y_test),std_y.inverse_transform(sgd.predict(x_test))))

# x_train = list(  zip(*data_x) )#转置
# y_train = np.array(data_y).reshape(-1,1)
# std_x = StandardScaler()
# x_train = std_x.fit_transform(x_train)
# std_y = StandardScaler()
# y_train = std_y.fit_transform(y_train)

# rd1 = Ridge(alpha=1.0)
# rd1.fit(x_train, y_train)
# print('岭回归系数',rd1.coef_)
# print('准确率',rd1.score(x_train,y_train))


X = list(  zip(*data_x) )
X = np.array(X)
print(X)
pca = PCA(n_components=8)#pca降维
newX=pca.fit_transform(X)
print('数据降维',newX)

y_train = np.array(data_y).reshape(-1,1)
rd1 = Ridge()
rd.fit(newX, y_train)
print('岭回归系数',rd.coef_)


x_train = list(  zip(*data_x) )
x_train = np.array(x_train)
y_train = np.array(data_y).reshape(-1,1)
la = Lasso()
la.fit(x_train,y_train)
print('Lasso回归系数',la.coef_)
print(la.score(x_train,y_train))

