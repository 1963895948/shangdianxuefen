#coding=utf-8
import numpy as np
from sklearn.decomposition import PCA
import numpy as np
import xlrd
from sklearn.linear_model import Ridge,Lasso,SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
X = np.array([[-1,2,66,-1], [-2,6,58,-1], [-3,8,45,-2], [1,9,36,1], [2,10,62,1], [3,5,83,2]])  #导入数据，维度为4
pca = PCA(n_components=2)   #降到2维
newX=pca.fit_transform(X)   #降维后的数据
# PCA(copy=True, n_components=2, whiten=False)
print(pca.explained_variance_ratio_)  #输出贡献率
print(newX)                  #输出降维后的数据

X = np.array([[1,2,3], [2,3,4], [4,5,6]])
Y = np.array([6,9,15])
pca = PCA(n_components=2)   #降到2维
newX=pca.fit_transform(X)
print(newX)
rd = Ridge()
rd.fit(newX,Y)
print(rd.coef_)
print(rd.score(newX,Y))
