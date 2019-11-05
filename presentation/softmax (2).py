import numpy as np
import matplotlib.pyplot as plt
import time
import os

def getIrisData():
	filepath = 'D:\\fallingspace\\perceptron\\data\\Iris\\iris_x.dat'
	markpath = 'D:\\fallingspace\\perceptron\\data\\Iris\\iris_y.dat'
	f = open(filepath,'r')
	m = open(markpath,'r')
	lines = f.readlines()
	markLine = m.readlines()
	dataSet = []
	markSet = []
	lenth = len(lines)

	for i in range(lenth):
		pData = lines[i].split(' ')
		mData = markLine[i]
		tempData = [float(pData[0]),float(pData[1])]
		dataSet.append(tempData)
		markSet.append(int(mData))
	
	f.close()
	m.close()
	return dataSet,markSet 

def zScoreStd(X):
    """
    功能: z-score标准化
    """
    return (X - X.mean(axis=0)) / X.std(axis=0)

def makeData(x,y):
	
	x = np.mat(x)
	x = zScoreStd(x)
	y = np.mat(y).T
	b = np.ones(y.shape)
	X = np.column_stack((b,x))
	X = np.mat(X)
	labelType = np.unique(y.tolist())

	eyes = np.eye(len(labelType))

#	print(eyes)

	Y = np.zeros((X.shape[0],len(labelType)))

	for i in range(X.shape[0]):
		Y[i,:] = eyes[int(y[i,0])]

#	print(Y)
	return X,y,Y

def softmax(s): #s行向量
	return np.exp(s)/np.sum(np.exp(s), axis = 1)


def costFunc(X,Y,weights):
	temp = 0
	pre = np.log(softmax(X*weights).T)
	for i in range(len(Y)):
		temp += Y[i,:] * pre[:,i]

	return -temp/len(Y)



def gradAscent(x,y,z):
	alpha = 0.01
	max_loop = 1000


	weights = np.ones((x.shape[1],y.shape[1]))
	costs = costFunc(x,y,weights)

	print("init weights : \n", weights.T)
	print("init costs : ", costs)

	#x = StandardScaler().fit_transform(x)
	for k in range(max_loop):
		h = softmax(x*weights)
		error = y-h
		weights = weights + alpha*x.T*error

	plotBestFit(X,z,weights)
	costs = costFunc(x,y,weights)
	print(weights)
	print(costs)

	return weights.getA()

def plotBestFit(dataMat,labelMat,weights):

    # 获取数据边界值，也就属性的取值范围。
    x1_min, x1_max = dataMat[:, 1].min() - .5, dataMat[:, 1].max() + .5
    x2_min, x2_max = dataMat[:, 2].min() - .5, dataMat[:, 2].max() + .5
    # 产生x1和x2取值范围上的网格点，并预测每个网格点上的值。
    step = 0.01
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, step), np.arange(x2_min, x2_max, step))
    testMat = np.c_[xx1.ravel(), xx2.ravel()]   #形成测试特征数据集
    testMat = np.column_stack((np.ones(((testMat.shape[0]),1)),testMat))  #添加第一列为全1代表b偏量
    testMat = np.mat(testMat)
    # 预测网格点上的值
    y = softmax(testMat*weights)   #输出每个样本属于每个分类的概率
    # 判断所属的分类
    predicted = y.argmax(axis=1)                            #获取每行最大值的位置，位置索引就是分类
    predicted = predicted.reshape(xx1.shape).getA()
    # 绘制区域网格图
    plt.pcolormesh(xx1, xx2, predicted, cmap=plt.cm.Paired)

    # 再绘制一遍样本点，方便对比查看
    plt.scatter(dataMat[:, 1].flatten().A[0], dataMat[:, 2].flatten().A[0],
                c=labelMat.flatten().A[0],alpha=.5)  # 第一个偏量为b，第2个偏量x1，第3个偏量x2
    plt.show()

m,n = getIrisData()
X,y,Y = makeData(m,n)
print(gradAscent(X,Y,y))