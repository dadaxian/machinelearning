import numpy as np


path = "D:\\fallingspace\\perceptron\\data\\Iris\\"


def getIrisData():
    filepath = path+'iris_x.dat'
    markpath = path+'iris_y.dat'
    f = open(filepath, 'r')
    m = open(markpath, 'r')
    lines = f.readlines()
    markLine = m.readlines()
    dataSet = []
    markSet = []
    lenth = len(lines)

    for i in range(lenth):
        pData = lines[i].split(' ')
        mData = markLine[i]
        tempData = [float(pData[0]), float(pData[1])]
        dataSet.append(tempData)
        markSet.append(int(mData))

    f.close()
    m.close()
    return dataSet, markSet


def makeData(x, y):

    x = np.mat(x)
    y = np.mat(y).T
    b = np.ones(y.shape)
    X = np.column_stack((b, x))
    X = np.mat(X)
    labelType = np.unique(y.tolist())

    eyes = np.eye(len(labelType))

#	print(eyes)

    Y = np.zeros((X.shape[0], len(labelType)))

    for i in range(X.shape[0]):
        Y[i, :] = eyes[int(y[i, 0])]

#	print(Y)
    return X, y, Y

# s行向量


def softmax(s):
    return np.exp(s)/np.sum(np.exp(s), axis=1)


def costFunc(X, Y, weights):
    return np.mean(np.log(Y*softmax(X*weights).T))


def gradAscent(x, y):
    alpha = 0.1
    max_loop = 5000

    weights = np.ones((x.shape[1], y.shape[1]))
    costs = costFunc(x, y, weights)

    print("init weights : \n", weights)
    print("init costs : ", costs)

    for k in range(max_loop):
        h = softmax(x*weights)
        error = h - y
        weights = weights - alpha*x.T*error
    costs = costFunc(x, y, weights)
    print(costs)
    return weights


m, n = getIrisData()
X, y, Y = makeData(m, n)
print(gradAscent(X, Y))
