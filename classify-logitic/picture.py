#coding=utf-8
from numpy import *
import operator
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
def index_all(x,y):#x为要检索的值，y为列表
    return[a for a in range(len(y)) if y[a] == x]#返回检索位置
def plot(matric,labels):#二维散点图
    fig=plt.figure()
    ax=fig.add_subplot(111)#建立一个图片
       # labels=array(labels)
    index_1=index_all(1,labels)
    p1=ax.scatter(matric[index_1,1],matric[index_1,0],color='m')#往图像上描绘点
    index_2=index_all(2,labels)
    p2=ax.scatter(matric[index_2,1],matric[index_2,0],color='r')
    index_3=index_all(3,labels)
    p3=ax.scatter(matric[index_3,1],matric[index_3,0],color='c')
    index_4=index_all(4,labels)
    p4=ax.scatter(matric[index_4,1],matric[index_4,0],color='m')#往图像上描绘点
    index_5=index_all(5,labels)
    p5=ax.scatter(matric[index_5,1],matric[index_5,0],color='r')
    index_6=index_all(6,labels)
    p6=ax.scatter(matric[index_6,1],matric[index_6,0],color='c')
    index_7=index_all(7,labels)
    p7=ax.scatter(matric[index_7,1],matric[index_7,0],color='m')#往图像上描绘点
    index_8=index_all(8,labels)
    p8=ax.scatter(matric[index_8,1],matric[index_8,0],color='r')
    index_9=index_all(9,labels)
    p9=ax.scatter(matric[index_9,1],matric[index_9,0],color='c')
    index_0=index_all(9,labels)
    p0=ax.scatter(matric[index_0,1],matric[index_0,0],color='c')
    plt.show
def plot_3d(matric,labels):#三维散点图，输入数据域，标签
    matric=array(matric)
    fig = plt.figure()
    ax3D = fig.add_subplot(111, projection='3d')
    index_1=index_all('Iris-setosa',labels)
    ax3D.scatter(matric[index_1,1].T,matric[index_1,0].T,matric[index_1,2].T,s=10,color='m')
    index_2=index_all('Iris-versicolor',labels)
    ax3D.scatter(matric[index_2,1].T,matric[index_2,0].T,matric[index_2,2].T,s=10,color='r')
    index_3=index_all('Iris-virginica',labels)
    ax3D.scatter(matric[index_3,1].T,matric[index_3,0].T,matric[index_3,2].T,s=10,color='c')
    ax3D.set_xlabel("x")
    ax3D.set_ylabel("y")
    ax3D.set_zlabel("z")
    plt.show()

