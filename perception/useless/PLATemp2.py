# -*- coding: utf-8 -*-
import copy
import pandas as pd
import numpy as np
import plot as plts
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


path="D:\\fallingspace\\perceptron\\data\\simpleData\\"
data= np.loadtxt(path+"ex4x.dat")
value= np.loadtxt(path+"ex4Y.dat")
trainint_set=[]
for index,item in enumerate(data):
    trainint_set.append(((item[0],item[1]),-1 if value[index]==0 else 1))
# print(trainint_set)

def mscatter(x,y,ax=None, m=None, **kw):
    import matplotlib.markers as mmarkers
    if not ax: ax=plt.gca()
    sc = ax.scatter(x,y,**kw)
    if (m is not None) and (len(m)==len(x)):
        paths = []
        for marker in m:
            if isinstance(marker, mmarkers.MarkerStyle):
                marker_obj = marker
            else:
                marker_obj = mmarkers.MarkerStyle(marker)
            path = marker_obj.get_path().transformed(
                        marker_obj.get_transform())
            paths.append(path)
        sc.set_paths(paths)
    return sc

marker={0:'o',1:'+'}
cmarker=list(map(lambda x:marker[x],value))


fig, ax = plt.subplots()
 # line的数据
x = np.linspace(-1,2)
y=x*-2+150
# 创建初始线，并添加
line1=ax.add_line(Line2D(x, y, linewidth=1, color='red'))
scatter = mscatter(data[:,0], data[:,1], c='b', m=cmarker, ax=ax,cmap=plt.cm.RdYlBu)


 
# trainint_set = [[(3,3),1],[(4,3),1],[(1,1),-1]]       #输入数据
w = [0,0]          #初始化w参数
b = 0              #初始化b参数

def update(item):
    global w,b
    w[0] += 1*item[1]*item[0][0]               #w的第一个分量更新
    w[1] += 1*item[1]*item[0][1]               #w的第二个分量更新
    b += 1*item[1]
    # print 'w = ',w,'b=',b                     #打印出结果

def judge(item):                               #返回y = yi(w*x+b)的结果
    res = 0
    for i in range(len(item[0])):
        res +=item[0][i]*w[i]                   #对应公式w*x
    res += b                                    #对应公式w*x+b
    res *= item[1]                              #对应公式yi(w*x+b)
    return res

def check():                                    #检查所有数据点是否分对了
    flag = False
    for item in trainint_set:
        if judge(item)<=0:                       #如果还有误分类点，那么就小于等于0
            flag = True
            update(item)                         #只要有一个点分错，我就更新
    return flag                                  #flag为False，说明没有分错的了

if __name__ == '__main__':
    flag = False
    for i in range(10000):
        if not check():                            #如果已经没有分错的话
            flag = True
            print(w,b)
            break
        y = (-w[1] * x-b)/w[0]
        try:
            ax.lines.remove(ax.lines[0])
        except Exception:
            pass
        lines = ax.plot(x ,y)
        plt.pause(0.01)
    # 显示前关掉交互模式
    plt.ioff()
    plt.show()
    if flag:
        print("OK")
    else:
        print("fail")