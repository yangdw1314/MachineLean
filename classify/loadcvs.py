#coding=utf-8
import csv
from numpy import *
import operator
#加载cvs文件并转换为矩阵
def loadtraindata(filename):
    arraydata=[]
    arrayline=csv.reader(file(filename,'rb'))
    for line in arrayline:
        arraydata.append(line)
    arraydata.remove(arraydata[0])
    arraydata=array(arraydata)
    label=arraydata[:,0]
    data=arraydata[:,1:]
    data=toint(data)
    #data=nomalizing(data)
    label=toint(label)
    return data,label
def toint(arrdata):
    arrdata=mat(arrdata)
    m,n=shape(arrdata)
    matdata=zeros((m,n))
    for i in range(m):
        for j in range(n):
            matdata[i,j]=int(arrdata[i,j])
    return matdata

#数值归一化（此处处理图像仅进行至二值化）
def nomalizing(data):
    m,n=shape(data)
    for i in range(m):
        for j in range(n):
            if data[i,j]!=0:
                data[i,j]=1
    return data