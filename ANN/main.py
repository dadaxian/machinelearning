#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import numpy as np


path="D:\\fallingspace\\machinelearning\\data\\ex4Data\\"
data= np.loadtxt(path+"ex4x.dat")
value= np.loadtxt(path+"ex4y.dat")


# sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 计算正确率（未使用）
def checkTrueRate(testMatData, testLabelData, W):
    accuracyCount = 0
    for index,item in enumerate(testMatData):
        for indexw in range(0,3):
            result=np.dot(item,W[indexw])
            if(result<0 and indexw!=testLabelData[index]):accuracyCount+=1
            if(result>0 and indexw==testLabelData[index]):accuracyCount+=1
    return accuracyCount

# 计算损失率（未使用）
def checkNotTrueRate(testMatData, testLabelData, W):
    accuracyCount = 0
    for index,item in enumerate(testMatData):
        for indexw in range(0,2):
            result=np.dot(item,W[indexw])
            if(result<=0 and indexw==testLabelData[index]):accuracyCount+=1
            if(result>0 and indexw!=testLabelData[index]):accuracyCount+=1
    return accuracyCount

# 计算损失
def chechLoss(testMatData,testLabelData,W):
    loss = 0
    for index,item in enumerate(testMatData):
        for indexw in range(0,3):
            result=np.dot(item,W[indexw])
            if(result<0 and indexw==testLabelData[index]):loss+=result
            if(result>0 and indexw!=testLabelData[index]):loss+=result
    return loss

# 计算单个超平面正确率
def checkSingleTrueRate(testMatData, testLabelData, w,indexw):
    accuracyCount = 0
    for index,item in enumerate(testMatData):
        result=np.dot(item,w)
        if(result<0 and indexw!=testLabelData[index]):accuracyCount+=1
        if(result>0 and indexw==testLabelData[index]):accuracyCount+=1
    return accuracyCount

# 归一化数据
def normalizefeature(data):
    x_norm = data
    meam = np.mean(data, axis=0)
    sigma = np.std(data, axis=0)
    x_norm = (data - meam) / sigma
    return x_norm

# 随机化数据
def shuffleData(data,value):
    tempData=[]
    for index,item in enumerate(data):
        tempData.append([item[0],item[1],value[index]])
    np.random.shuffle(tempData)
    tempData=np.array(tempData)
    return tempData[...,:2],tempData[...,2]

# 绘制图标
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





# 初始化权值数组
W=[(0.5,0.5,0.5),(0.5,0.5,0.5)]
V=[(0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,0.5,0.5)]
# 最优权值组
bestW=[(0,0,0),(0,0,0)]
# 最优正确分类数
bestClassifyCount=[0,0]
# 数据预处理
data,value=shuffleData(data,value)
data=normalizefeature(data)

# 添加偏置参数
data=np.insert(data,2,values=1,axis=1)


# 作图相关
# 给标签映射图形
# 圆形 星星 正三角
marker={0:'o',1:'*'}
cmarker=list(map(lambda x:marker[x],value))
# 生成子图
# fig, ax = plt.subplots()
# 创建图像布局对象fig
fig = plt.figure(figsize = (12, 6))
# ax1=fig.add_subplot(122)
 # 初始线的数据
x = np.linspace(-5,5)
# 添加总标题，并设置文字大小
plt.suptitle("multi_class_PLA_2Class", fontsize=20) 
ax=fig.add_subplot(121)
# 坐标轴范围
plt.xlim((-3,3))
plt.ylim((-3,3))
ax1=fig.add_subplot(122)
ax1.set_xlabel('epoch')
ax1.set_ylabel('BadPointCount')
# 最终设置
plt.grid(True)
scatter = mscatter(data[:,0], data[:,1],c='', m=cmarker, ax=ax,cmap=plt.cm.RdYlBu,edgecolors='k')
# 关闭阻塞模式，打开交互模式
plt.ion() 

# 学习参数设置 
# 学习率
a=0.1
# 学习轮数
epochs=5
epoch=1

while(epoch<epochs+1):
    

# costs=[]
# costs.append(checkNotTrueRate(data,value,bestW))
# ax1.plot(np.arange(epoch), costs, 'r-')

# while(epoch<epochs+1):
#     # 数据预处理
#     data,value=shuffleData(data,value)
#     # 添加偏置参数
#     data=np.insert(data,2,values=1,axis=1)
#     print("epoch:%2d"%epoch)
#     epoch+=1
#     for k,input_vector in enumerate(data):
#         ck=maxJBywx(W,input_vector)
#         # 对每个权重向量更新
#         for j in range(0,2):
#             if(j==ck and j!=value[k]):
#                 W[j]=W[j]-a*input_vector
                
#             elif(j==value[k] and j!=ck):
#                 W[j]=W[j]+a*input_vector
#             # 获取当前效果（正确分类个数）
#             currentRate=checkSingleTrueRate(data,value,W[j],j)
#             # 如果更好就更换最优权值
#             if(currentRate>bestClassifyCount[j]):
#                 bestClassifyCount[j]=np.copy(currentRate)
#                 bestW[j]=np.copy(W[j])

#     costs.append(checkNotTrueRate(data,value,bestW))
#     ax1.plot(np.arange(epoch), costs, 'r-')

#     # 更新超平面
#     try:
#         while len(ax.lines)>0:
#             ax.lines.remove(ax.lines[0])
#     except Exception:
#         pass
#     y0 = (-bestW[0][0] * x- bestW[0][2])/(bestW[0][1])
#     y1 = (-bestW[1][0] * x- bestW[1][2])/(bestW[1][1])
#     # 圆
#     ax.plot(x ,y0,color='red',label='0 circle')
#     # 星
#     ax.plot(x ,y1,color='blue',label='1 star')
#     plt.pause(0.1)

# 显示前关掉交互模式
plt.ioff()
plt.show()

"""
'-'	实线样式
'--'	短横线样式
'-.'	点划线样式
':'	虚线样式
'.'	点标记
','	像素标记
'o'	圆标记
'v'	倒三角标记
'^'	正三角标记
'&lt;'	左三角标记
'&gt;'	右三角标记
'1'	下箭头标记
'2'	上箭头标记
'3'	左箭头标记
'4'	右箭头标记
's'	正方形标记
'p'	五边形标记
'*'	星形标记
'h'	六边形标记 1
'H'	六边形标记 2
'+'	加号标记
'x'	X 标记
'D'	菱形标记
'd'	窄菱形标记
'&#124;'	竖直线标记
'_'	水平线标记
"""