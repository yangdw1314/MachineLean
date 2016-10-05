#coding=utf-8
from numpy import *
import operator
from loadcvs import *



def classify(inx,dataset,label,k):
    datasize=dataset.shape[0]
    diffmat=tile(inx,(datasize,1))-dataset
    sqdiffmat=diffmat**2
    sqdistance=sqdiffmat.sum(axis=1)
    distance=sqdistance**0.5
    sortdistance=distance.argsort()
    distsum=0
    for i in range(k):#距离加权算法
        distsum+=distance[sortdistance[i]]
    classcount={}
    for i in range(k):
        votelabel=label[0,sortdistance[i]]
        classcount[votelabel]=classcount.get(votelabel,0)+(1-(distance[sortdistance[i]]/distsum))
    sortclass=sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortclass[0][0]
def test(dataset,label,k):#测试2000个数k取5错79
    errorcount=0
    for i in range(40001,41999):
        result= classify(dataset[i,:784],dataset[:40000,:784],label[:40000],k)
      # print "the result:%d,the real answer:%d"%(result,label[0,i])
        if(result!=label[0,i]):
            print "the result:%d,the real answer:%d"%(result,label[0,i])
            errorcount+=1
    return errorcount
if __name__ == "__main__":  
     data,label=loadtraindata('train.csv')
    # print "the result:%d,the real answer:%d"(data,label)
     ecount=test(data,label,7)
     print ecount
#说明;1,对数据归一化:测试2000个数k取5错79
#     2,不对数据归一化：测试2000k值取5错63;测试2000k值取10错77
#      3,不对数据归一化，且有距离加权算法：测试2000k值取5错63;测试2000k值取10错71