import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
tf.compat.v1.disable_eager_execution()
# 随机生成1000个点，围绕在y=0.1x+0.3的直线周围
num_points = 1000
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])

# 生成一些样本,x_data为第1个分量，y_data为第2个分量
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

print(np.array(vectors_set).shape)
print(np.array(x_data).shape)
print(np.array(y_data).shape)

plt.scatter(x_data,y_data,c='orange',s=5)#画散点图
plt.show()

# 生成1维的W矩阵，取值是[-1,1]之间的随机数
W = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name='W')#注意是random.uniform
# 生成1维的b矩阵，初始值是0
b = tf.Variable(tf.zeros([1]), name='b')
# 经过计算得出预估值y
y = W * x_data + b

# 以预估值y和实际值y_data之间的均方误差作为损失
loss = tf.reduce_mean(tf.square(y - y_data))
# 采用梯度下降法来优化参数
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)
# 训练的过程就是最小化这个误差值
tf.compat.v1.disable_eager_execution()
train = optimizer.minimize(loss,name='train')
sess = tf.compat.v1.Session()
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

# 初始化的W和b是多少
print ("W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss))
# 执行20次训练
for step in range(20):
    sess.run(train)
    # 输出训练好的W和b
    print ("W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss))
writer = tf.compat.v1.summary.FileWriter("./tmp", sess.graph)

plt.scatter(x_data,y_data,c='orange',s=5)
plt.plot(x_data,sess.run(W)*x_data+sess.run(b))
plt.show()











