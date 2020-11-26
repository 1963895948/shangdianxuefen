# # coding:utf-8
# with open('g.txt',mode='a+') as f:
#     f.write('qqq\n')
#     f.write('aaa1\n')

def outter(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        print(111)
        return res
    return wrapper

@outter
def a(x=1,y=2,z=3):
    print(x,y,z)
    if(x==1):
        return 222

@outter
def b(x=1,y=2,z=3):
    print(x,y,z)


c = a(1,3,2)
print(c)
b()