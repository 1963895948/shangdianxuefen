from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import pydotplus
from six import StringIO

def descion():
    train_data = pd.read_csv("train.csv")
    # PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    x_train = train_data[['Pclass', 'Age', 'Sex']]
    y_train = train_data['Survived']
    test_data = pd.read_csv("test.csv")
    # PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    x_test = test_data[['Pclass', 'Age', 'Sex']]

    print(x_train['Age'])
    # 缺失值处理
    x_train['Age'].fillna(x_train['Age'].mean(),inplace=True)
    print(x_train['Age'])
    #one-hat编码
    dict = DictVectorizer(sparse=False)
    x_train = dict.fit_transform(x_train.to_dict(orient="records"))#将每一行提取出来形成字典
    x_test = dict.transform(x_test.to_dict(orient="records"))
    print(x_train)
    dectree = DecisionTreeClassifier()
    dectree.fit(x_train,y_train)
    print('准确率:',dectree.score(x_train,y_train))

    #export_graphviz(dectree,out_file='./tree.dot',feature_names=['年龄','Pclass1','Pclass2','Pclass3','sex1','sex2'])

    dot_data = export_graphviz(dectree, out_file=None,
                                    feature_names=['年龄','Pclass1','sex1','sur'],
                                    class_names=['no default','default'],
                                    filled=True, rounded=True,
                                    special_characters=True)

    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf('titanic.pdf')
descion()