x = [[1,0,3],[1,1,3],[1,2,3],[1,3,2],[1,4,4]]
y = [95,97,75,60,49]
#y=a*x1+b*x2+c*x3
threshold = 0.000001#阈值
cost = 0#损失值
newcost = 0
alpha = 0.0001#学习率
a,b,c=0,0,0
d = 0
count = 0
while True:
    dif = [0, 0, 0]
    num = len(x)
    for i in range(num):
        dif[0] = (y[i]-(a * x[i][0]+b * x[i][1]+c * x[i][2])) * x[i][0]
        dif[1] = (y[i]-(a * x[i][0]+b * x[i][1]+c * x[i][2])) * x[i][1]
        dif[2] = (y[i]-(a * x[i][0]+b * x[i][1]+c * x[i][2])) * x[i][2]
        a = a + dif[0]/num * alpha
        b = b + dif[1]/num * alpha
        c = c + dif[2]/num * alpha
    for i in range(num):
        newcost += ((y[i]-a*x[i][0]-b*x[i][1]-c*x[i][2]))**2
    newcost /=num
    count+=1
    if(abs(cost-newcost)<threshold):
        break
    else:
        cost = newcost


print(a,b,c)
print(count)
#1049140