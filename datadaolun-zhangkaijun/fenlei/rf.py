# coding:utf-8
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz

from sklearn.feature_extraction import DictVectorizer

credit = pd.read_csv("credit.csv")

y = credit['default']
del credit['default']
X = credit
dict = DictVectorizer(sparse=False)
credit = dict.fit_transform(X.to_dict(orient="records"))  # 将每一行提取出来形成字典
print(credit[0])

# y = credit[-1]
# del credit[-1]
# X = credit
#
print(credit)
X_train, X_test, y_train, y_test = train_test_split(credit, y, test_size=0.3)
print(y_test)

credit_model = DecisionTreeClassifier()
credit_model.fit(X_train, y_train)
print('准确率', credit_model.score(X_test, y_test))
print(credit_model.predict(X_test))

forest = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)
forest.fit(X_train, y_train)
print('准确率:', forest.score(X_test, y_test))
# export_graphviz(dectree,out_file='./tree.dot',feature_names=['年龄','Pclass1','Pclass2','Pclass3','sex1','sex2'])

# dot_data = export_graphviz(dectree, out_file=None,
#                            feature_names=['年龄', 'Pclass1', 'sex1', 'sur'],
#                            class_names=['no default', 'default'],
#                            filled=True, rounded=True,
#                            special_characters=True)
#
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf('titanic.pdf')
