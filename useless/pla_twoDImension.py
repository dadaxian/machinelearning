#coding=utf-8
import numpy as np 
import pandas as pd
import numpy as np
import plot as plts
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


# 计算正确率
def checkTrueRate(testMatData, testLabelData, W):
    accuracyCount = 0

    for index,item in enumerate(testMatData):
        result=np.dot(item,W)
        labelExt=-1 if result<=0 else 1
        if(labelExt==testLabelData[index]):
            accuracyCount+=1
    return accuracyCount


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


a = np.random.randint(0,10,size=[50,2])
b=np.random.randint(11,20,size=[50,2])

data=np.vstack((a,b))

value=[]
for index,item in enumerate(a):
    value.append(1)
for index,item in enumerate(b):
    value.append(0)


# 随机化数据
data,value=shuffleData(data,value)

training_set=np.insert(data,2,values=1,axis=1)
print(training_set)


threshold=0
learning_rate=0.1
weights=[0,0,0]



marker={0:'o',1:'+'}
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




bestW=weights
bestAccuracyRate=0

epoch=100
while(epoch>0):
    print('-'*60)
    error_count=0
    for index,input_vector in enumerate(training_set):
        result=dot_product(input_vector,weights)>threshold
        error=value[index]-result
        if error!=0:
            error_count+=1
            weights+=learning_rate*error*input_vector
            currentRate=checkTrueRate(training_set,value,weights)
            if(currentRate>bestAccuracyRate):
                bestAccuracyRate=currentRate
                print(currentRate)
                bestW=weights
            print(index)
        print(weights)
    plt.pause(0.001)
    print(weights)
    epoch-=1
    if error_count==0:
        break
    y = (-bestW[0] * x- bestW[2])/(bestW[1])
    try:
        ax.lines.remove(ax.lines[0])
    except Exception:
        pass
    lines = ax.plot(x ,y)
# 显示前关掉交互模式
plt.ioff()
plt.show()