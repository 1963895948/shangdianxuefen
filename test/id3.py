from math import log
from test import treehuatu
def createDataSet():
    dataset = [['sunny', 'hot', 'high', 'FALSE', 'no'],
               ['sunny', 'hot', 'high', 'TRUE', 'no'],
               ['overcast', 'hot', 'high', 'FALSE', 'yes'],
               ['rainy', 'mild', 'high', 'FALSE', 'yes'],
               ['rainy', 'cool', 'normal', 'FALSE', 'yes'],
               ['rainy', 'cool', 'normal', 'TRUE', 'no'],
               ['overcast', 'cool', 'normal', 'TRUE', 'yes'],
               ['sunny', 'mild', 'high', 'FALSE', 'no'],
               ['sunny', 'cool', 'normal', 'FALSE', 'yes'],
               ['rainy', 'mild', 'normal', 'FALSE', 'yes'],
               ['sunny', 'mild', 'normal', 'TRUE', 'yes'],
               ['overcast', 'mild', 'high', 'TRUE', 'yes'],
               ['overcast', 'hot', 'normal', 'FALSE', 'yes'],
               ['rainy', 'mild', 'high', 'TRUE', 'no'],

               ]
    labels = ['outlook', 'temperature','humidity','windy']
    # change to discrete values
    return dataset, labels


def dataset_entropy(dataset):
    numentries = len(dataset)
    labelcount = {}
    for i in dataset:
        currentlabel = i[-1]
        if(currentlabel not in labelcount.keys()):
            labelcount[currentlabel]=0
        labelcount[currentlabel]+=1
    shannonent = 0.0 #初始化信息墒
    for key in labelcount:
        prob = float(labelcount[key])/numentries
        shannonent -= prob * log(prob,2)

    #print(shannonent)
    return shannonent

def choosebestfeature(dataset):
    numfeature = len(dataset[0])-1 #特征数
    baseentropy = dataset_entropy(dataset)
    bestinfogain = 0.0
    bestfeature = -1
    for i in range(numfeature):
        featlist = [exm[i] for exm in dataset]
        uniquevals = set(featlist)
        newentropy = 0.0
        for value in uniquevals:
            subdataset = splitDataSet(dataset,i,value)
            prob = len(subdataset)/float(len(dataset))
            newentropy += prob*dataset_entropy(subdataset)
        infogain = baseentropy - newentropy
        if(infogain>bestinfogain):
            bestinfogain = infogain
            bestfeature = i
    return bestfeature

def majortyCnt(classLabel):#计算次数最多的分类
    dict_class = {}
    for i in classLabel:
        if(i not in dict_class.keys()):
            dict_class[i] = classLabel.count((i))
    #print(dict_class)
    max_index = max(zip(dict_class.values(),dict_class.keys()))
    #print(max_index[1])
    return max_index[1]

def splitDataSet(dataset, bestfeat, value):
    retdataset = []
    for featvec in dataset:
        if(featvec[bestfeat] == value):
            reducedFeatVec = featvec[:bestfeat]  # chop out axis used for splitting
            reducedFeatVec.extend(featvec[bestfeat + 1:])
            retdataset.append(reducedFeatVec)
    return retdataset

def createtree(dataset,labels):
    classLabel = [exm[-1] for exm in dataset]#当前数据集下标签列所有值
    if(classLabel.count(classLabel[0]) == len(classLabel)):
        return classLabel[0]#当类别相同时停止划分，返回该类标签
    if(len(dataset[0]) == 1):#如果还有特征
        return majortyCnt(classLabel)
    bestfeat = choosebestfeature(dataset)#获取最好的分类索引
    bestfeatlabel = labels[bestfeat]#获取该特征名字
    mytree = {bestfeatlabel:{}}#用字典来建立树，将当前最好的特征存储在bestfeat中
    del(labels[bestfeat])#删除已经选取的特征
    featvalues = [exm[bestfeat] for exm in dataset]
    #print(featvalues)
    uniquevals = set(featvalues)
    for value in uniquevals:
        sublabels = labels[:]
        mytree[bestfeatlabel][value] = createtree(splitDataSet(dataset, bestfeat, value),sublabels)
    return mytree


def predict(tree,labels,testdata):
    rootname = list(tree.keys())[0]
    rootvalue = tree[rootname]
    featureindex = labels.index(rootname)
    classlabel = None
    for key in rootvalue.keys():
        if(testdata[featureindex] == key):
            if(type(rootvalue[key]).__name__ == "dict"):
                classlabel = predict(rootvalue[key],labels,testdata)
            else:
                classlabel = rootvalue[key]
    return classlabel

if __name__ == '__main__':
    dataset ,labels= createDataSet()
    label = labels.copy()#由于函数参数设计有问题，在函数内部会修改labels的值
    tree = createtree(dataset,labels)
    testdata = ['sunny', 'cool', 'eqwe', 'FALSE']
    res = predict(tree,label,testdata)
    print(tree)
    print(res)
    treehuatu.createPlot(tree)
