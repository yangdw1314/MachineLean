#coding=utf-8
from recommend import *
import MySQLdb
def loadMovie(moviename):
    movie={}
    conn=MySQLdb.connect(host='localhost',user='root',passwd='ydw',port=3306,charset='utf8')
    cur=conn.cursor()
    cur.execute('use movingdat')
    cur.execute('create table movnam(movingid varchar(10) ,movingname varchar(50))')
    
    for line in open(moviename):
        (id,title)=line.split('::')[0:2]
        movie[id]=title
        value=[id,title]
        cur.execute('insert into movnam values(%s,%s)',value)
    conn.commit()
    cur.close()
    conn.close()  
def loadrating(ratingname):
    conn=MySQLdb.connect(host='localhost',user='root',passwd='ydw',port=3306,charset='utf8')
    cur=conn.cursor()
    cur.execute('use movingdat')
    cur.execute('create table movrat(userid varchar(10) ,movid varchar(10),rating varchar(10))')
    for line in open(ratingname):
        (user,movieid,rating)=line.split('::')[0:3]
        value=[user,movieid,rating]
        cur.execute('insert into movrat values(%s,%s,%s)',value)
        #prefs.setdefault(user,{})
        #prefs[user][movie[movieid]]=float(rating)
    conn.commit()
    cur.close()
    conn.close()  
if __name__ == "__main__":  
    #loadMovie('movies.dat')
    #loadrating('ratings.dat')
    conn=MySQLdb.connect(host='localhost',user='root',passwd='ydw',port=3306,charset='utf8')
    cur=conn.cursor()
    cur.execute('use movingdat')
    prefs={}
    cur.execute('select * from movrat')
    selectdata=cur.fetchall();
    for line in selectdata:
        prefs.setdefault(line[0],{})
        prefs[line[0]][line[1]]=float(line[2])
        print prefs
   
    #prefs=transPrefs(prefs)
    conn.commit()
    cur.close()
    conn.close()  
    #re=sim_pearson(prefs,'Sabrina (1995)','Lamerica (1994)')
   # re=topMatch(prefs,'Sabrina (1995)',n=5)
    #re=getRecmmend(prefs,'10')
  re=getRecommend(prefs,'10')[0:10]
    print re
    