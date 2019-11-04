#coding=utf-8
import pandas as pd
import numpy as np
import plot as plts
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np



path="D:\\fallingspace\\perceptron\\data\\ex4Data\\"
data= np.loadtxt(path+"ex4x.dat")
value= np.loadtxt(path+"ex4Y.dat")





def shuffleData(data,value):
    tempData=[]
    for index,item in enumerate(data):
        tempData.append([item[0],item[1],value[index]])
    # print(tempData)
    np.random.shuffle(tempData)
    # print(tempData)
    tempData=np.array(tempData)
    return tempData[...,:2],tempData[...,2]


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

def dot_product(values,weights):
    return sum(value*weight for value, weight in zip(values,weights))




threshold=0
learning_rate=0.1
weights=[0,0,0]
training_set=data




for index,item in enumerate(value):
    value[index]=-1 if value[index]==0 else 1

data,value=shuffleData(data,value)

training_set=np.insert(data,2,values=1,axis=1)






marker={-1:'o',1:'+'}
cmarker=list(map(lambda x:marker[x],value))
fig, ax = plt.subplots()
 # line的数据
x = np.linspace(-1,60)
y=x*-2+150
# 创建线，并添加
line1=ax.add_line(Line2D(x, y, linewidth=1, color='red'))
scatter = mscatter(data[:,0], data[:,1], c='b', m=cmarker, ax=ax,cmap=plt.cm.RdYlBu)
# 关闭阻塞模式，打开交互模式
plt.ion()   
# for i in range(10):
#     y = x*(-i*4) + 50*i
#     try:
#         ax.lines.remove(ax.lines[0])
#     except Exception:
#         pass
#     lines = ax.plot(x ,y)
#     plt.pause(1)
epoch=100
while(epoch>0):
    print('-'*60)
    error_count=0
    
    for index,input_vector in enumerate(training_set):
        result=dot_product(input_vector,weights)*value[index]<=0
        if result==1:
            error_count+=1
            weights+=learning_rate*value[index]*input_vector
            # print(index)
        # print(weights)
    plt.pause(0.001)
    print(weights)
    epoch-=1
    if error_count==0:
        break
    y = (-weights[0] * x- weights[2])/(weights[1])
    try:
        ax.lines.remove(ax.lines[0])
    except Exception:
        pass
    lines = ax.plot(x ,y)
# 显示前关掉交互模式
plt.ioff()
plt.show()
