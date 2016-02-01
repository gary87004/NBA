# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:33:35 2015

@author: User-PC
"""

import urllib
import linecache
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use("ggplot")
# from sklearn.cluster import KMeans


URI='http://www.nba.com/history/nba-season-recaps/index.html'
data=urllib.request.urlopen(URI).read()
data=data.decode('utf-8')

f = open('This time.txt', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
f.write(data)
year=str(input("請輸入年分(例:2013-14)\n"));

a=year+'</a>'
b='<'
position=data.find(a)
#f.seek(position)
#f.close()

for i in range(50):
    if data[position+38+i]!=b:
        pass
    else:
        break
print('The champion is'+data[position+38:position+38+i]+"\n")
index=position+38+i;


for j in range(50):
    if data[index+27+j]!=b:
        pass
    else:
        break
    
print('The runner up is '+data[index+27:index+27+j]+"\n")
runner=index+27+j;


for k in range(50):
    if data[runner+27+k]!=b:
        pass
    else:
        break
    
print('Result '+data[runner+27:runner+27+k]+"\n")
result=runner+27+k;


for g in range(50):
    if data[result+27+g]!=b:
        pass
    else:
        break
print('Season MVP '+data[result+27:result+27+g]+"\n")
smvp=result+27+g;

for s in range(50):
    if data[smvp+42+s]!=b:
        pass
    else:
        break
print('Final MVP '+data[smvp+42:smvp+42+s]+"\n\n\n")
f.close()

# print('The champion is'+data[position+38:position+38+i]+'\n','The runner up is '+data[index+27:index+27+j]+'\n',
#       'Result '+data[runner+27:runner+27+k],'Season MVP '+data[result+27:result+27+g],
#       'Final MVP '+data[smvp+42:smvp+42+s])
# print('The runner up is '+data[index+27:index+27+j]+"\n")
# print('Result '+data[runner+27:runner+27+k]+"\n")
# print('Season MVP '+data[result+27:result+27+g]+"\n")
# print('Final MVP '+data[smvp+42:smvp+42+s]+"\n")


w=[]
bb=[]
cc=[]
kk=[]
dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','"reb"','ast','stl','tov','pf']
standings=['html','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center']   #每年統計戰機不同



if year=='2003-04':
    '''
    import get0304
    get0304.test(bb,dic,standings,kk)
    
    dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','reb','ast','stl','tov','pf']
    standings=['html','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk']
    '''
    URI='http://www.nba.com/pistons/stats?season=2003-04&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0304statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)                                                              
    for l in range(13):                                                         #幾個球員
        s= linecache.getline("0304statistic.csv", 364+l)
        for io in range(len(dic)):
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    pass
                else:
                    break
            for p in range(20):
                if s[key+h+p]!='<':
                    pass
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[]]                                #幾種數據
         
    
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])                     #13樣數據
    
    f = open('0304statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')
    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()
    
    
    
    URI='http://www.basketball-reference.com/leagues/NBA_2004_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0304standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for team in range(29):                                                      #29隊
        for qq in range(21):                                                    #20種戰績
            s1= linecache.getline("0304standings.csv", 644+qq+24*team)
            position1=s1.find(standings[qq])
            for q in range(25):
                if s1[position1+q]!='>':
                    pass
                else:
                    break;
            for r in range(25):
                if s1[position1+q+r]!='<':
                    pass
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]    
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])                                 #21種戰績
    
    f = open('0304standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse MidWest div'+','+'Verse Pacific div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'OCT'+','+'NOV'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')
    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()
    
    overall=[]
    f = open('0304standings.csv', 'r')  
    for row in csv.reader(f):  
        print ('%-30s%-10s%-10s%-10s%-10s%-10s' %(row[0],row[1],row[2],row[3],row[4],row[5]))
        # print ('%-30s%-20s%-20s%-20s%-20s' %(row[0],row[6],row[7],row[8],row[9]))

        overall.append(row[1])
    f.close()


    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((29,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    # kmeans=KMeans(n_clusters=3)
    # kmeans.fit(X)
    #
    # centroids = kmeans.cluster_centers_
    # labels = kmeans.labels_
    #
    # print(centroids)
    # print(labels)
    #
    # colors =["g.","r.","b."]
    #
    # for i in range(len(X)):
    #     print("coordinate:",X[i],"label:",labels[i])
    #     plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    #
    # plt.scatter(centroids[:,0],centroids[:,1])
    #
    # plt.show()
    
    
if year=='2004-05':
    '''
    dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','reb','ast','stl','tov','pf']
    standings=['html','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk']   #每年統計戰機不同
    '''    
    #import get0405
    #get0405.test(bb,dic,standings,kk)
    URI='http://www.nba.com/spurs/stats?season=2004-05&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0405statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for l in range(14):
        s= linecache.getline("0405statistic.csv", 422+l)
        for io in range(len(dic)):
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    pass
                else:
                    break
            for p in range(20):
                if s[key+h+p]!='<':
                    pass
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]                            #長度為球員數目
         
    
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])                                       #13樣數據
    
    f = open('0405statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')

    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()
    
    
    
    URI='http://www.basketball-reference.com/leagues/NBA_2005_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0405standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    
    for team in range(30):                                                     #30隊
        for qq in range(22):                                                   #21種戰績
            s1= linecache.getline("0405standings.csv", 675+qq+25*team)
            position1=s1.find(standings[qq])
            for q in range(25):
                if s1[position1+q]!='>':
                    pass
                else:
                    break;
            for r in range(25):
                if s1[position1+q+r]!='<':
                    pass
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]    
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])
    
    f = open('0405standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse Southeast div'+','+'Verse Northeast div'+','+'Verse Pacific div'+','+'Verse Southwest div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'NOV'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')

    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()
    
    
    
    overall=[]
    f = open('0405standings.csv', 'r')  
    for row in csv.reader(f):
        print ('%-30s%-10s%-10s%-10s%-10s%-10s' %(row[0],row[1],row[2],row[3],row[4],row[5]))
        overall.append(row[1])
    f.close()  
    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((30,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    # kmeans=KMeans(n_clusters=3)
    # kmeans.fit(X)
    #
    # centroids = kmeans.cluster_centers_
    # labels = kmeans.labels_
    #
    # print(centroids)
    # print(labels)
    #
    # colors =["g.","r.","b."]
    #
    # for i in range(len(X)):
    #     print("coordinate:",X[i],"label:",labels[i])
    #     plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    #
    # plt.scatter(centroids[:,0],centroids[:,1])
    #
    # plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if year=='2005-06':
    '''
    dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','reb','ast','stl','tov','pf']
    standings=['html','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk','csk']   #每年統計戰機不同
    '''    
    URI='http://www.nba.com/heat/stats?season=2005-06&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0506statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for l in range(14):
        
       
        s= linecache.getline("0506statistic.csv", 412+l)
       
        
        for io in range(len(dic)):
         
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    pass
                else:
                    break
            for p in range(50):
                if s[key+h+p]!='<':
                    pass
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
         
    
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])
    
    f = open('0506statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')

    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()


    
    URI='http://www.basketball-reference.com/leagues/NBA_2006_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0506standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    
    for team in range(30):                                                     #30隊
        for qq in range(22):                                                   #21種戰績
            s1= linecache.getline("0506standings.csv", 675+qq+25*team)
            position1=s1.find(standings[qq])
            for q in range(25):
                if s1[position1+q]!='>':
                    pass
                else:
                    break;
            for r in range(25):
                if s1[position1+q+r]!='<':
                    pass
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]    
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])
    
    f = open('0506standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse Southeast div'+','+'Verse Northeast div'+','+'Verse Pacific div'+','+'Verse Southwest div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'NOV'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')

    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()


    overall=[]
    f = open('0506standings.csv', 'r')  
    for row in csv.reader(f):
        print ('%-30s%-10s%-10s%-10s%-10s%-10s' %(row[0],row[1],row[2],row[3],row[4],row[5]))
        overall.append(row[1])
    f.close()  
    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((30,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    # kmeans=KMeans(n_clusters=3)
    # kmeans.fit(X)
    #
    # centroids = kmeans.cluster_centers_
    # labels = kmeans.labels_
    #
    # print(centroids)
    # print(labels)
    #
    # colors =["g.","r.","b."]
    #
    # for i in range(len(X)):
    #     print("coordinate:",X[i],"label:",labels[i])
    #     plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    #
    # plt.scatter(centroids[:,0],centroids[:,1])
    #
    # plt.show()























if year=='2006-07':
    '''
    dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','reb','ast','stl','tov','pf']
    standings=['html','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center']   #每年統計戰機不同
    '''   
    URI='http://www.nba.com/spurs/stats?season=2006-07&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0607statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for l in range(15):
        s= linecache.getline("0607statistic.csv", 423+l)
        s=list(s)
        
        for io in range(len(dic)):
            s = ''.join(s)
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    h
                else:
                    break
            for p in range(20):
                if s[key+h+p]!='<':
                    p
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]                          #球員個數
         
    
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])
    
    f = open('0607statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')

    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()
    

    URI='http://www.basketball-reference.com/leagues/NBA_2007_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0607standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    
    for team in range(30):                                                     #30隊
        for qq in range(23):                                                   #22種戰績
            s1= linecache.getline("0607standings.csv", 676+qq+26*team)
            position1=s1.find(standings[qq])
            for q in range(50):
                if s1[position1+q]!='>':
                    q
                else:
                    break;
            for r in range(50):
                if s1[position1+q+r]!='<':
                    r
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]    
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])
    
    f = open('0607standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse Southeast div'+','+'Verse Northeast div'+','+'Verse Pacific div'+','+'Verse Southwest div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'OCT'+','+'NOV'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')

    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()


    overall=[]
    f = open('0607standings.csv', 'r')  
    for row in csv.reader(f):  
        overall.append(row[1])
    f.close()  
    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((30,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    kmeans=KMeans(n_clusters=3)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)

    colors =["g.","r.","b."]

    for i in range(len(X)):
        print("coordinate:",X[i],"label:",labels[i])
        plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    
    plt.scatter(centroids[:,0],centroids[:,1])

    plt.show()




























if year=='2007-08':
    '''
    dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','reb','ast','stl','tov','pf']
    standings=['html','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center']   #每年統計戰機不同
    '''
    URI='http://www.nba.com/celtics/stats?season=2007-08&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0708statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for l in range(15):
        s= linecache.getline("0708statistic.csv", 416+l)
        s=list(s)
        
        for io in range(len(dic)):
            s = ''.join(s)
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    h
                else:
                    break
            for p in range(20):
                if s[key+h+p]!='<':
                    p
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    
    
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]                          #球員個數
      
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])
    
    f = open('0708statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')

    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()


    URI='http://www.basketball-reference.com/leagues/NBA_2008_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0708standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    
    for team in range(30):                                                     #30隊
        for qq in range(23):                                                   #22種戰績
            s1= linecache.getline("0708standings.csv", 676+qq+26*team)
            position1=s1.find(standings[qq])
            for q in range(50):
                if s1[position1+q]!='>':
                    q
                else:
                    break;
            for r in range(50):
                if s1[position1+q+r]!='<':
                    r
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]  #30隊  
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])
    
    f = open('0708standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse Southeast div'+','+'Verse Northeast div'+','+'Verse Pacific div'+','+'Verse Southwest div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'OCT'+','+'NOV'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')

    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()




    overall=[]
    f = open('0708standings.csv', 'r')  
    for row in csv.reader(f):  
        overall.append(row[1])
    f.close()  
    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((30,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    kmeans=KMeans(n_clusters=3)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)

    colors =["g.","r.","b."]

    for i in range(len(X)):
        print("coordinate:",X[i],"label:",labels[i])
        plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    
    plt.scatter(centroids[:,0],centroids[:,1])

    plt.show()



















if year=='2008-09':
    '''
    dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','reb','ast','stl','tov','pf']
    standings=['html','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center']   #每年統計戰機不同
    '''
    URI='http://www.nba.com/lakers/stats/index.html?season=2008-09&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0809statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for l in range(14):
        s= linecache.getline("0809statistic.csv", 427+l)
        s=list(s)
        
        for io in range(len(dic)):
            s = ''.join(s)
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    h
                else:
                    break
            for p in range(20):
                if s[key+h+p]!='<':
                    p
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]                          #球員個數
      
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])
    
    f = open('0809statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')

    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()
    
    
    URI='http://www.basketball-reference.com/leagues/NBA_2009_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0809standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    
    for team in range(30):                                                     #30隊
        for qq in range(23):                                                   #22種戰績
            s1= linecache.getline("0809standings.csv", 676+qq+26*team)
            position1=s1.find(standings[qq])
            for q in range(50):
                if s1[position1+q]!='>':
                    q
                else:
                    break;
            for r in range(50):
                if s1[position1+q+r]!='<':
                    r
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]  #30隊  
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])
    
    f = open('0809standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse Southeast div'+','+'Verse Northeast div'+','+'Verse Pacific div'+','+'Verse Southwest div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'OCT'+','+'NOV'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')

    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()
    
    
    overall=[]
    f = open('0809standings.csv', 'r')  
    for row in csv.reader(f):  
        overall.append(row[1])
    f.close()  
    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((30,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    kmeans=KMeans(n_clusters=3)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)

    colors =["g.","r.","b."]

    for i in range(len(X)):
        print("coordinate:",X[i],"label:",labels[i])
        plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    
    plt.scatter(centroids[:,0],centroids[:,1])

    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if year=='2009-10':
    '''
    dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','reb','ast','stl','tov','pf']
    standings=['html','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center']   #每年統計戰機不同
    '''
    URI='http://www.nba.com/lakers/stats/index.html?season=2009-10&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0910statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for l in range(13):
        s= linecache.getline("0910statistic.csv", 426+l)
        s=list(s)
        
        for io in range(len(dic)):
            s = ''.join(s)
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    h
                else:
                    break
            for p in range(20):
                if s[key+h+p]!='<':
                    p
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[]]                          #球員個數
      
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])
    
    f = open('0910statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')

    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()
    
    
    URI='http://www.basketball-reference.com/leagues/NBA_2010_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('0910standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    
    for team in range(30):                                                     #30隊
        for qq in range(23):                                                   #22種戰績
            s1= linecache.getline("0910standings.csv", 676+qq+26*team)
            position1=s1.find(standings[qq])
            for q in range(50):
                if s1[position1+q]!='>':
                    q
                else:
                    break;
            for r in range(50):
                if s1[position1+q+r]!='<':
                    r
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]  #30隊  
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])
    
    f = open('0910standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse Southeast div'+','+'Verse Northeast div'+','+'Verse Pacific div'+','+'Verse Southwest div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'OCT'+','+'NOV'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')

    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()


    overall=[]
    f = open('0910standings.csv', 'r')  
    for row in csv.reader(f):  
        overall.append(row[1])
    f.close()  
    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((30,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    kmeans=KMeans(n_clusters=3)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)

    colors =["g.","r.","b."]

    for i in range(len(X)):
        print("coordinate:",X[i],"label:",labels[i])
        plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    
    plt.scatter(centroids[:,0],centroids[:,1])

    plt.show()



















if year=='2011-12':
    '''
   import get1112
   get1112.test(bb,dic)
   
    dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','reb','ast','stl','tov','pf']
    standings=['html','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center']   #每年統計戰機不同
    '''
    URI='http://www.nba.com/heat/stats?season=2011-12&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('1112statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for l in range(15):
        s= linecache.getline("1112statistic.csv", 413+l)
        s=list(s)
        
        for io in range(len(dic)):
            s = ''.join(s)
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    h
                else:
                    break
            for p in range(20):
                if s[key+h+p]!='<':
                    p
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]                          #球員個數
      
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])
    
    f = open('1112statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')

    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()
    
    
    
    URI='http://www.basketball-reference.com/leagues/NBA_2012_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('1112standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    
    for team in range(30):                                                     #30隊
        for qq in range(21):                                                   #22種戰績
            s1= linecache.getline("1112standings.csv", 674+qq+24*team)
            position1=s1.find(standings[qq])
            for q in range(50):
                if s1[position1+q]!='>':
                    q
                else:
                    break;
            for r in range(50):
                if s1[position1+q+r]!='<':
                    r
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]  #30隊  
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])
    
    f = open('1112standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse Southeast div'+','+'Verse Northeast div'+','+'Verse Pacific div'+','+'Verse Southwest div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')

    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()
    
    
    overall=[]
    f = open('1112standings.csv', 'r')  
    for row in csv.reader(f):  
        overall.append(row[1])
    f.close()  
    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((30,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    kmeans=KMeans(n_clusters=3)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)

    colors =["g.","r.","b."]

    for i in range(len(X)):
        print("coordinate:",X[i],"label:",labels[i])
        plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    
    plt.scatter(centroids[:,0],centroids[:,1])

    plt.show()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if year=='2012-13':
    '''
    import get1213
    get1213.test(bb,dic)
    
    dic=['playerfile','gp','pts','fg_pct','fg3_pct','ft_pct','oreb','dreb','reb','ast','stl','tov','pf']
    standings=['html','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center','center']   #每年統計戰機不同
    '''
    URI='http://www.nba.com/heat/stats?season=2012-13&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('1213statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for l in range(15):
        s= linecache.getline("1213statistic.csv", 413+l)
        s=list(s)
        
        for io in range(len(dic)):
            s = ''.join(s)
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    h
                else:
                    break
            for p in range(20):
                if s[key+h+p]!='<':
                    p
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]                          #球員個數
      
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])
    
    f = open('1213statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')

    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()

    URI='http://www.basketball-reference.com/leagues/NBA_2013_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('1213standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    
    for team in range(30):                                                     #30隊
        for qq in range(23):                                                   #22種戰績
            s1= linecache.getline("1213standings.csv", 676+qq+26*team)
            position1=s1.find(standings[qq])
            for q in range(50):
                if s1[position1+q]!='>':
                    q
                else:
                    break;
            for r in range(50):
                if s1[position1+q+r]!='<':
                    r
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]  #30隊  
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])
    
    f = open('1213standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse Southeast div'+','+'Verse Northeast div'+','+'Verse Pacific div'+','+'Verse Southwest div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'OCT'+','+'NOV'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')

    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()


    overall=[]
    f = open('1213standings.csv', 'r')  
    for row in csv.reader(f):  
        overall.append(row[1])
    f.close()  
    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((30,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    kmeans=KMeans(n_clusters=3)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)

    colors =["g.","r.","b."]

    for i in range(len(X)):
        print("coordinate:",X[i],"label:",labels[i])
        plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    
    plt.scatter(centroids[:,0],centroids[:,1])

    plt.show()















if year=='2013-14':
    '''
    import get1314
    get1314.test(bb,dic)
    '''
    URI='http://www.nba.com/spurs/stats?season=2013-14&season_type=regular%20season'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('1314statistic.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    for l in range(15):
        s= linecache.getline("1314statistic.csv", 423+l)
        s=list(s)
        
        for io in range(len(dic)):
            s = ''.join(s)
            key=s.find(dic[io])
            for h in range(50):
                if s[key+h]!='>':
                    h
                else:
                    break
            for p in range(20):
                if s[key+h+p]!='<':
                    p
                else:
                    break
            bb.append(s[key+h+1:key+h+p])
            
    f.close()
    sta=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]                          #球員個數
      
    for o in range(l+1):
        sta[o]=','.join(bb[len(dic)*o:len(dic)+len(dic)*o])
    
    f = open('1314statistic.csv', 'w', encoding = 'UTF-8')
    f.write('Player'+','+'GP'+','+'PTS'+','+'FG%'+','+'3P%'+','+'FT%'+','+'OREB'+','+'DREB'+','+'REB'+','+'AST'+','+'STL'+','+'TO'+','+'PF'+'\n')

    for e in range(len(sta)):
        f.write(sta[e]+'\n')
    f.close()
    
    
    URI='http://www.basketball-reference.com/leagues/NBA_2013_standings.html'
    data=urllib.request.urlopen(URI).read()
    data=data.decode('utf-8')
 
    f = open('1314standings.csv', 'w', encoding = 'UTF-8')    # 也可使用指定路徑等方式，如： C:\A.txt
    f.write(data)
    
    for team in range(30):                                                     #30隊
        for qq in range(23):                                                   #22種戰績
            s1= linecache.getline("1314standings.csv", 676+qq+26*team)
            position1=s1.find(standings[qq])
            for q in range(50):
                if s1[position1+q]!='>':
                    q
                else:
                    break;
            for r in range(50):
                if s1[position1+q+r]!='<':
                    r
                else:
                    break;
            kk.append(s1[position1+q+1:position1+q+r])
    f.close()
    b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]  #30隊  
    for u in range(len(b)):
        b[u]=', '.join(kk[(qq+1)*u:(qq+1)+(qq+1)*u])
    
    f = open('1314standings.csv', 'w', encoding = 'UTF-8')
    f.write('TEAM'+','+'Overall'+','+'Home'+','+'Road'+','+'East'+','+'West'+','+'Verse Atlantic div'+','+'Verse Central div'+','+'Verse Southeast div'+','+'Verse Northeast div'+','+'Verse Pacific div'+','+'Verse Southwest div'+','+'Pre allstar game'+','+'Post allstar game'+','+'< 3points'+','+'>10points'+','+'OCT'+','+'NOV'+','+'DEC'+','+'JAN'+','+'FEB'+','+'MAR'+','+'APR'+'\n')

    for w in range(len(b)):
        f.write(b[w]+'\n')
    f.close()
    overall=[]
    f = open('1314standings.csv', 'r')  
    for row in csv.reader(f):  
        overall.append(row[1])
    f.close()  
    trans=''.join(overall)
    win=[]
    for j in range(len(overall)-1):
        win.append(trans[8+6*j:10+6*j])
    win=list(map(int,win))
    lose=[]
    for jj in range(len(overall)-1):
        lose.append(trans[11+6*jj:13+6*jj])
    lose=list(map(int,lose))

    apap=np.zeros((30,2))
    for i in range(len(win)):
        apap[i][0]=win[i]
    for ii in range(len(lose)):
        apap[ii][1]=lose[ii]
    X = np.array(apap)

    kmeans=KMeans(n_clusters=3)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)

    colors =["g.","r.","b."]

    for i in range(len(X)):
        print("coordinate:",X[i],"label:",labels[i])
        plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
    
    plt.scatter(centroids[:,0],centroids[:,1])

    plt.show()