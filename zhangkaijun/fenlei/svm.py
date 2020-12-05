from sklearn.svm import SVC
import numpy as np

x = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
model = SVC(C=10, gamma=0.1)  # C是惩罚因子，ganma是松弛度
model.fit(x, y)
print(model.predict([[-1.2, -1.2]]))
