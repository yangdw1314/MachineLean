#coding=utf-8
#返回P1，P2的皮尔逊相关系数
from math import *
def sim_pearson(prefs,p1,p2):#prefs为评分数据集；p1,p2为评分比较id
    si={}
    for item in prefs[p1]:#得到双方评价过得物品列表
        if item in prefs[p2]:
            si[item]=1
    #得到列表元素个数
    n=len(si)
    if n==0:
        return 1
    #对所有偏好求和
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    sum1sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2sq=sum([pow(prefs[p2][it],2) for it in si])
    psum =sum([prefs[p1][it]*prefs[p2][it] for it in si])
    #计算皮尔逊评价值
    num=psum-(sum1*sum2/n)
    den=sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
    if den==0:
        return 0
    r=num/den
    return r
#返回最相似的前n个值
def topMatch(prefs,item,n=3):
    scores=[(sim_pearson(prefs, item, other),other)  for other in prefs  if other!=item]
    scores.sort()
    scores.reverse()
    return scores[0:n]
#转换物品与人物数据集
def transPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            result[item][person]=prefs[person][item]
    return result
#为每个物品构造一个最相近物品数据集
def similarItem(prefs,n=3):
   
    result={}
    itemprefs=transPrefs(prefs)
    for item in itemprefs:
        scores=topMatch(itemprefs, item, n)
        result[item]=scores
    return result
#获取推荐
def getRecommend(prefs,user):#评分列表，相似物品数据集，当前用户id
    itemmatch=similarItem(prefs,n=3)
    userrat=prefs[user]
    scores={}
    totalsim={}
    #循环遍历当前用户评分物品
    for (item,rating) in userrat.items():
        for (similar,item2) in itemmatch[item]:
            if item2 in userrat:
                continue
            scores.setdefault(item2,0)
            scores[item2]+=similar*rating
            totalsim.setdefault(item2,0)
            totalsim[item2]+=similar
    rank=[(score/totalsim[item],item) for (item,score) in scores.items()]
    rank.sort()
    rank.reverse()
    return rank
    
    







    
    

    
    
    
    
    
    
    