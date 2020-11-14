import numpy as np
from math import log
import pandas as pd
#coding:utf-8
#导入matplotlib.pyplot,如果显示mo module,请自行安装
import matplotlib.pyplot as plt

#定义文本框和箭头格式
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

#获取叶节点数
def getNumLeafs(myTree):
    numLeafs = 0
    #如果使用的是python2，用注释掉的一行
    # firstStr = myTree.keys()[0]


    #LZ使用的是python3
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes
            numLeafs += getNumLeafs(secondDict[key])
        else:   numLeafs +=1
    return numLeafs

#获取树的层数
def getTreeDepth(myTree):
    maxDepth = 0
    #python2的用法
    # firstStr = myTree.keys()[0]

    #python3使用下面两行
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]

    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:   thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth

#绘制带箭头的注解
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )

#在父子节点填充文本信息
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)

#plotTree函数
def plotTree(myTree, parentPt, nodeTxt):#if the first key tells you what feat was split on
    numLeafs = getNumLeafs(myTree)  #this determines the x width of this tree
    depth = getTreeDepth(myTree)
    #python2
    # firstStr = myTree.keys()[0]     #the text label for this node should be this
    #python3
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes
            plotTree(secondDict[key],cntrPt,str(key))        #recursion
        else:   #it's a leaf node print the leaf node
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD
#if you do get a dictonary you know it's a tree, and the first element will be another dict

def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    #no ticks
    #createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
    plotTree(inTree, (0.5,1.0), '')
    plt.show()

#def createPlot():
#    fig = plt.figure(1, facecolor='white')
#    fig.clf()
#    createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
#    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
#    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
#    plt.show()

def retrieveTree(i):
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]

#createPlot(thisTree)

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

    #dataset = pd.read_csv('credit.csv').values.tolist()

    labels = ['outlook', 'temperature','humidity','windy']
    #labels = ["checking_balance","months_loan_duration","credit_history","purpose","amount","savings_balance","employment_length","installment_rate","personal_status","other_debtors","residence_history","property","age","installment_plan","housing","existing_credits","job","dependents","telephone","foreign_worker"]
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
    bestfeature = -1
    bestinfogainrage = 0.0
    for i in range(numfeature):
        featlist = [exm[i] for exm in dataset]
        uniquevals = set(featlist)
        newentropy = 0.0
        for value in uniquevals:
            subdataset = splitDataSet(dataset,i,value)
            prob = len(subdataset)/float(len(dataset))
            newentropy += prob*dataset_entropy(subdataset)
        splitinfo  = dataset_entropy(dataset)
        infogain = baseentropy - newentropy
        infogainrate = infogain/splitinfo
        #print(splitinfo,baseentropy)
        if(infogainrate>bestinfogainrage):
            bestinfogainrage = infogainrate
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
    print(labels)
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
    print(tree)
    createPlot(tree)