import math

import xlrd
import xlwt

readxls  = xlrd.open_workbook("Concrete_Data.xls")#读取文件，建立工作铺
names = readxls.sheet_names()#输出工作铺中的表
print(names)

worksheet = readxls.sheet_by_index(0)#打开第一个表
print(worksheet)

nrows = worksheet.nrows #读取行数
print(nrows)
ncols = worksheet.ncols#读取列数
print(ncols)

col_data = worksheet.col_values(0)#读取第一列
print(col_data)

def Z_score(col_data):
    nrows = len(col_data)
    average = float(sum(col_data))/nrows  #均值

    total = 0
    for value in col_data:
        total += (value - average)**2

    stddev = math.sqrt(total/nrows)
    return [(x-average)/stddev for x in col_data]

print(Z_score(col_data[1:-1]))

def max_min(data):
    return [(x-min(data))/(max(data)-min(data)) for x in data]
print(max_min(col_data[1:-1]))


def decimal_scaling(data):
    n = len(str(int(max(map(abs,data)))))
    return [(x/(10**n)) for x in data]

print(decimal_scaling(col_data[1:-1]))


def logistic(data):#取值应该在0附近，越远差值越大
    return [ (1/(1+math.exp(-x))) for x in data]

print(logistic(col_data[1:-1]))


#将处理后的数据保存，可以不看
book = xlwt.Workbook(encoding="utf_8")

sheet = book.add_sheet('Z_score',cell_overwrite_ok=True)
for j in range(worksheet.ncols):
        col_data = worksheet.col_values(j)
        for k in range(0,len(Z_score(col_data[1:-1]))):
            sheet.write(k+1,j,Z_score(col_data[1:-1])[k])
        name_list = worksheet.row_values(0)
        for l in range(0, len(name_list)):
            sheet.write(0, l, name_list[l])

sheet1 = book.add_sheet('max_min',cell_overwrite_ok=True)
for j in range(worksheet.ncols):
        col_data = worksheet.col_values(j)
        list1 = max_min(col_data[1:-1])
        for k in range(0,len(list1)):
            sheet1.write(k+1,j,list1[k])

        name_list = worksheet.row_values(0)
        for l in range(0, len(name_list)):
            sheet1.write(0, l, name_list[l])

sheet2 = book.add_sheet('decimal_scaling',cell_overwrite_ok=True)
for j in range(worksheet.ncols):
        col_data = worksheet.col_values(j)
        for k in range(0,len(decimal_scaling(col_data[1:-1]))):
            sheet2.write(k+1,j,decimal_scaling(col_data[1:-1])[k])
        name_list = worksheet.row_values(0)
        for l in range(0, len(name_list)):
            sheet2.write(0, l, name_list[l])

sheet3 = book.add_sheet('logistic',cell_overwrite_ok=True)
for j in range(worksheet.ncols):
        col_data = worksheet.col_values(j)
        for k in range(0,len(logistic(col_data[1:-1]))):
            sheet3.write(k+1,j,logistic(col_data[1:-1])[k])
        name_list = worksheet.row_values(0)
        for l in range(0, len(name_list)):
            sheet3.write(0, l, name_list[l])
book.save('data-processing.xls')
'''
liat_name=['Z_score','max_min','decimal_scaling','logistic']

for i in range(4):#保存
    book = xlwt.Workbook(encoding="utf_8")
    sheet = book.add_sheet(liat_name[i],cell_overwrite_ok=True)
    print(liat_name[i])

    for j in range(worksheet.ncols):
        col_data = worksheet.col_values(j)
        for k in range(len(max_min(col_data[1:-1]))):
            print(max_min(col_data[1:-1]))
            sheet.write(k+1,j,max_min(col_data[1:-1])[k])

    name_list = worksheet.row_values(0)
    for l in range(0,len(name_list)):
        sheet.write(0,l,name_list[l])
    book.save('data-processing.xls')
'''
