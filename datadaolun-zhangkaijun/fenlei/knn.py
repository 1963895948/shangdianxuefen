import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics




breast_cancer = pd.read_csv("wisc_bc_data.csv")
print (breast_cancer.shape)
del breast_cancer["id"]
print(breast_cancer)

dignosis_dict = {"B":0,"M":1}
breast_cancer["diagnosis"] = breast_cancer["diagnosis"].map(dignosis_dict)
print(breast_cancer)

print(breast_cancer[["radius_mean","area_mean","smoothness_mean"]].describe())


def min_max_normalize(x):
    return (x-x.min())/(x.max() - x.min())

for col in breast_cancer.columns[1:31]:
    breast_cancer[col] = min_max_normalize(breast_cancer[col])

print(breast_cancer.iloc[:,1:].describe())

y = breast_cancer["diagnosis"]
del breast_cancer["diagnosis"]
X = breast_cancer
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

print(y_train.value_counts()/len(y_train))
print(y_test.value_counts()/len(y_test))

for k in [1,5,9,11,15,21]:
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(x_train,y_train)
    print("K为：",k)
    print("\t正确率：",knn_model.score(x_test,y_test))
    print("\t假阴性：",metrics.confusion_matrix(y_test,knn_model.predict(x_test))[0,1])
    print("\t假阳性：", metrics.confusion_matrix(y_test, knn_model.predict(x_test))[1, 0])



from sklearn import preprocessing
breast_cancer_zscore = pd.DataFrame(preprocessing.scale(breast_cancer),columns = breast_cancer.columns)

breast_cancer_zscore_train, breast_cancer_zscore_test,\
breast_cancer_train_labels, breast_cancer_test_labels \
= train_test_split(breast_cancer_zscore, y, test_size=0.3, random_state=0)

#模型训练
knn_model_z = KNeighborsClassifier(n_neighbors = 5)
knn_model_z.fit(breast_cancer_zscore_train, breast_cancer_train_labels)
#模型预测
breast_cancer_test_pred_z = knn_model_z.predict(breast_cancer_zscore_test)
#性能评估
accuracy_z = metrics.accuracy_score(breast_cancer_test_labels, breast_cancer_test_pred_z)
confusion_mat_z = metrics.confusion_matrix(breast_cancer_test_labels, breast_cancer_test_pred_z)

print ("k = 5")
print("\t正确率: ", '%.2f'%(accuracy_z*100) + "%")
print ("\t假阴性：",confusion_mat_z[0,1])
print ("","\t假阳性：",confusion_mat_z[1,0])