#coding=utf-8
from recommend import *
def loadMovie(moviename,ratingname):
    movie={}
    for line in open(moviename):
        (id,title)=line.split('::')[0:2]
        movie[id]=title
    prefs={}
    for line in open(ratingname):
        (user,movieid,rating)=line.split('::')[0:3]
        prefs.setdefault(user,{})
        prefs[user][movie[movieid]]=float(rating)
        
    return prefs
if __name__ == "__main__":  
    prefs=loadMovie('movies.dat','ratings.dat')
    #prefs=transPrefs(prefs)
    #re=similarItem(prefs,n=10)
    #re=sim_pearson(prefs,'Sabrina (1995)','Lamerica (1994)')
   # re=topMatch(prefs,'Sabrina (1995)',n=5)
    #re=getRecommend(prefs,'10')
    re=getRecommend(prefs,'10')[0:10]
    print re
    