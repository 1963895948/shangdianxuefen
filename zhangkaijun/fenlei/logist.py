import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
data = pd.read_csv('wisc_bc_data.csv')
del data["id"]
y = data["diagnosis"]
y.replace('M',0,inplace=True)
y.replace('B',1,inplace=True)
del data["diagnosis"]
X = data


# dignosis_dict = {"B":0,"M":1}
# breast_cancer["diagnosis"] = breast_cancer["diagnosis"].map(dignosis_dict)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

std = StandardScaler()
X_train = std.fit_transform(X_train)
X_test = std.transform(X_test)

lg = LogisticRegression()
lg.fit(X_train, y_train)
print(lg.score(X_test, y_test))
print(lg.predict(X_test))


from sklearn.cluster import KMeans
km = KMeans(n_clusters=2)
km.fit(X_train)
print(km.cluster_centers_)
print(km.labels_)
a = list(y_train)
b = km.labels_
count = 0

for i in range(len(km.labels_)):
    if(a[i] == b[i]):
        count+=1

print(count/len(km.labels_))