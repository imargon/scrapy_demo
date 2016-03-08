#-*-coding:UTF-8-*-#
'''
Created on 2015年3月27日

@author: nimrob
'''
from numpy import  *
import operator


def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['a','a','b','b']
    return group,labels

g,l = createDataSet()
# print g
# print l

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    print classCount
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    print sortedClassCount
    return sortedClassCount[0][0]
    
print classify0([0.65,0.68],g,l,3)

cc =( tile([1,0],(4,1)) - g )**2
print cc
dd = cc.sum(axis=1)
print dd



dd = dd ** 0.5

print dd
dd = dd.argsort()
print dd
    

