import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from six import StringIO

import graphviz
import pydotplus
from sklearn import tree
from IPython.display import Image
import os

credit = pd.read_csv("credit.csv")
# print(credit.head(10))
# print(credit.checking_balance.value_counts())
#
#
# print(credit[["months_loan_duration","amount"]].describe())

col_dicts = {}
cols = ['checking_balance', 'credit_history', 'purpose', 'savings_balance', 'employment_length', 'personal_status',
        'other_debtors', 'property', 'installment_plan', 'housing', 'job', 'telephone', 'foreign_worker']

col_dicts = {'checking_balance': {'1 - 200 DM': 2,
                                  '< 0 DM': 1,
                                  '> 200 DM': 3,
                                  'unknown': 0},
             'credit_history': {'critical': 0,
                                'delayed': 2,
                                'fully repaid': 3,
                                'fully repaid this bank': 4,
                                'repaid': 1},
             'employment_length': {'0 - 1 yrs': 1,
                                   '1 - 4 yrs': 2,
                                   '4 - 7 yrs': 3,
                                   '> 7 yrs': 4,
                                   'unemployed': 0},
             'foreign_worker': {'no': 1, 'yes': 0},
             'housing': {'for free': 1, 'own': 0, 'rent': 2},
             'installment_plan': {'bank': 1, 'none': 0, 'stores': 2},
             'job': {'mangement self-employed': 3,
                     'skilled employee': 2,
                     'unemployed non-resident': 0,
                     'unskilled resident': 1},
             'other_debtors': {'co-applicant': 2, 'guarantor': 1, 'none': 0},
             'personal_status': {'divorced male': 2,
                                 'female': 1,
                                 'married male': 3,
                                 'single male': 0},
             'property': {'building society savings': 1,
                          'other': 3,
                          'real estate': 0,
                          'unknown/none': 2},
             'purpose': {'business': 5,
                         'car (new)': 3,
                         'car (used)': 4,
                         'domestic appliances': 6,
                         'education': 1,
                         'furniture': 2,
                         'others': 8,
                         'radio/tv': 0,
                         'repairs': 7,
                         'retraining': 9},
             'savings_balance': {'101 - 500 DM': 2,
                                 '501 - 1000 DM': 3,
                                 '< 100 DM': 1,
                                 '> 1000 DM': 4,
                                 'unknown': 0},
             'telephone': {'none': 1, 'yes': 0}}

for col in cols:
    credit[col] = credit[col].map(col_dicts[col])

print(credit.head(10))

from sklearn.model_selection import train_test_split

y = credit['default']
del credit['default']
X  = credit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(y_train.value_counts()/len(y_train))
print(y_test.value_counts()/len(y_test))


credit_model = DecisionTreeClassifier(max_depth=5)
credit_model.fit(X_train, y_train)
print(credit_model.score(X_test,y_test))

dot_data = export_graphviz(credit_model, out_file=None,
                                    feature_names=X_train.columns,
                                    class_names=['no default','default'],
                                    filled=True, rounded=True,
                                    special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('credit.pdf')

#
# def get_enorgini():
#     criterion = ["gini","entropy"]
#     for i in criterion:
#         credit_model = DecisionTreeClassifier(criterion=i)#默认gini
#         credit_model.fit(X_train, y_train)
#         print(i,credit_model.score(X_test, y_test))
#         print(i, credit_model.score(X_train, y_train))
#
#
# def get_dep():
#     criterion = 20
#     dep = []
#     for i in range(1,criterion):
#         credit_model = DecisionTreeClassifier(max_depth=i)
#         credit_model.fit(X_train, y_train)
#         print(i,credit_model.score(X_test, y_test))
#         dep.append(credit_model.score(X_test, y_test))
#     plt.plot(range(1,criterion),dep)
#     plt.show()
#
#
# if __name__ == "__main__":
#     get_enorgini()
#     get_dep()