#coding=utf-8
from numpy import *
import operator
mulweight={}#存0-9个数字分别对应的权重
#阶跃函数
def sigmoid(inx):
    return 1.0/(1+exp(-inx))

#优化a值，得出权重w
def gradascent(data,label,k,numiter=150):
    m,n=shape(data)
    weight=ones(n)
    classlabel=label
    for j in range(numiter):
        dataindex=range(m)
        for i in range(m):
            alpha=4/(1.0+j+i)+0.1
            randindex=int(random.uniform(0,len(dataindex)))
            h=sigmoid(sum(data[randindex]*weight))
            if classlabel[0,randindex]==k:
                classlabel[0,randindex]=1
            else:classlabel[0,randindex]=0
            error=classlabel[0,randindex]-h
            weight=weight+alpha*error*data[randindex]
            del(dataindex[randindex])
    return weight

#编写多分类
def multiclass(data,label,numiter=150):
    for k in range(10):
        mulweight[k]=gradascent(data,label,k)

#对数据集测试
def test(data,label,numiter=150):
    m,n=shape(data)
    maxh=0
    errorcount=0
    retclass=inf
    for i in range(m):
        for k in range(10):
            weights=mulweight[k]
            h=sigmoid(sum(data[i]*weights))
            if h>maxh:
                maxh=h
                retclass=k
        if(retclass!=label[0,i]):
           print "the result:%d,the real answer:%d"%(retclass,label[0,i])
           errorcount+=1
    return errorcount


