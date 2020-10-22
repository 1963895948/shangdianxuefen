import xlrd
from sklearn.preprocessing import MinMaxScaler
#DictVectorizer one-hot编码
#CountVectorizer 计算词频
#TfidfVectorizer 除了考量某一词汇在当前文本中出现的频率 TF（Term Frequency）之外，同时关注包含这个词汇的所有文本条数的倒数，即逆文本频率指数 IDF（Inverse Document Frequency)，这样可以削减一些高频大众词汇对分类决策的干扰（它们对文本特点刻画的贡献很小）。文本条目越多，Tfid的优势越显著。

texts=["dog cat fish","dog cat cat","fish bird", 'bird']
str = '如何从这些英文中抽取情感态度而进行分类呢？最直观的做法就是抽取单词。通常认为，很多关键词能够反映说话者的态度。比如上面这个简单的数据集，很容易发现，凡是说了“shit”的，就一定属于neg类。当然，上面数据集是为了方便描述而简单设计的。现实中一个词经常会有穆棱两可的态度。但是仍然有理由相信，某个单词在neg类中出现的越多，那么他表示neg态度的概率越大。'
#cv = DictVectorizer(sparse = False)

# data = cv.fit_transform([{'city':'北京','temperature':100},{'city':'上海','temperature':20},{'city':'广州','temperature':140}])
# print(cv.get_feature_names())
# print(data)

# cv = CountVectorizer()
# con = jieba.cut(str)
# con = list(con)
# print(con)
# con = ' '.join(con)
# print(con)
# data = cv.fit_transform([con])
# print(cv.get_feature_names())
# print(data)

# cv = CountVectorizer()
# cv_fit = cv.fit_transform(texts)
# print(cv_fit)
# print(cv.get_feature_names())
# print(cv.vocabulary_)

readxls  = xlrd.open_workbook("Concrete_Data.xls")#读取文件，建立工作铺
names = readxls.sheet_names()
print(names)

worksheet = readxls.sheet_by_index(0)#打开第一个表
print(worksheet)
col_data = worksheet.col_values(0)
print(col_data)
col_data1 = worksheet.col_values(1)
print(col_data1)

col_data = col_data[1:-1]
col_data1 = col_data1[1:-1]

arr = []
for i in range(len(col_data)):
    a = []
    a.append(col_data[i])
    a.append(col_data1[i])
    arr.append(a)

print(arr)
mm = MinMaxScaler()
data = mm.fit_transform(arr)
for i in range(len(data)):
    print(data[i])