#coding=utf-8

import numpy as np 

# 计算错误率
def checkErrorRate(testMatData, testLabelData, W):
    accuracyCount = 0
    for i in range(len(testMatData)):
        vect = testMatData[i, :]
        extraBiasVect = np.append(1, vect)
        resultY = np.dot(W, extraBiasVect)
        if (resultY <= 0):
            labelY = -1
        else:
            labelY = 1
        if (labelY == testLabelData[i]):
            accuracyCount += 1
    return accuracyCount / len(testLabelData)


# 数据非线性可分的情况下，pocketPerceptron实现
def pocketPerceptronLearn(trainMatData, trainLabelData, testMatData, testLabelData):
    # 设定最大迭代次数
    maxIteration = 100000
    # 初始向量
    W = [0, 0, 0, 0, 0]
    # labely
    iterationFinish = False
    # 当前迭代次数
    times = 0
    bestW = W
    bestAccuracyRate = 0
    for interationCount in range(maxIteration):
        for dataIndex in range(len(trainMatData)):
            # 计算向量内积
            vect = trainMatData[dataIndex, :]
            extraBiasVect = np.append(1, vect)
            resultY = np.dot(W, extraBiasVect)
            if (resultY <= 0):
                labelY = -1
            else:
                labelY = 1
 
            if (labelY != trainLabelData[dataIndex]):
                W = W + trainLabelData[dataIndex] * extraBiasVect
                times += 1
                rate = checkErrorRate(testMatData, testLabelData, W)
                if (rate > bestAccuracyRate):
                    bestAccuracyRate = rate
                    bestW = W
            else:
                if (dataIndex == (len(trainMatData) - 1)):
                    iterationFinish = True
        if (iterationFinish == True):
            break
            # 验证测试
        if (times >= 50):
            print(bestW)
            print(bestAccuracyRate)
    return bestW, bestAccuracyRate

