import matplotlib.pyplot as plt
x = [[1],[2],[3],[4],[5]]
y = [3,8.9,19.1,32.9,51]
#y=a*x1+b*x2+c*x3
threshold = 0.0000001#阈值
cost = 0#损失值
newcost = 0
alpha = 0.0001#学习率
a =0
c = 0
while True:
    dif = [0, 0, 0]
    num = len(x)
    for i in range(num):
        dif[0] += (y[i]-(a * x[i][0]* x[i][0] +c)) * x[i][0]
        dif[1] += (y[i]-(a * x[i][0]* x[i][0] + c))
    a = a + dif[0]/num  * alpha
    c = c + dif[1]/num * alpha
    for i in range(num):
        newcost += ((y[i]-a*x[i][0]*x[i][0] - c))**2
    newcost /=num
    if(abs(cost-newcost)<threshold):
        break
    else:
        cost = newcost

x = [1,2,3,4,5]
print(a,c)
plt.scatter(x,y)
y = [ a*i*i+c for i in y]
plt.plot(x,y)
plt.show()