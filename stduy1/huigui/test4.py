a = [1,2,3,4,5]

b= []
for i in range(len(a)):
    print(i)
    b.append(a.pop(i))
    print(b)