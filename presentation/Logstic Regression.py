#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n = 79
a = np.diag(np.array([1, 2]))

# Load data from file
x_ = pd.read_table('D:\\fallingspace\\perceptron\\data\\ex4Data\\ex4x.dat', sep='\s+')
x_.columns = ['Exam 1', 'Exam 2']
y_ = pd.read_table('D:\\fallingspace\\perceptron\\data\\ex4Data\\ex4y.dat', sep='\s+')
y_.columns = ['Admitted']

data = pd.concat([x_, y_], axis=1)

positive = data[
    data['Admitted'] == 1]  # returns the subset of rows such Admitted = 1, i.e. the set of *positive* examples
negative = data[
    data['Admitted'] == 0]  # returns the subset of rows such Admitted = 0, i.e. the set of *negative* examples
data = data.values

# sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 计算损失
def cost(X, y, theta):
    return np.mean(-y * np.log(sigmoid(X @ theta)) - (1 - y) * np.log(1 - sigmoid(X @ theta)))

# 预测函数
def predict(X, theta):
    return [1 if x >= 0.5 else 0 for x in (X @ theta)]

# 计算梯度值
def gradient(X, y, theta):
    return (1 / len(X)) * (X.T @ (sigmoid(X @ theta) - y))

# 归一化数据
def normalizefeature(data):
    x_norm = data
    meam = np.mean(data, axis=0)
    sigma = np.std(data, axis=0)
    x_norm = (data - meam) / sigma

    return x_norm

# 随机化数据
def shuffleData(data):
    np.random.shuffle(data)  # 是否打乱数据
    cols = data.shape[1]
    X = data[:, 0:cols - 1]
    X = normalizefeature(X)  # 使用归一化
    X = np.column_stack((np.ones(n), X)) # 加上偏置项
    y = data[:, cols - 1:]
    return X, y

# 进行梯度下降   alpha为学习率
def descent(data, theta, batchSize, iter, alpha):
    i = 0  # 迭代次数
    k = 0  # batch
    X, y = shuffleData(data)
    costs = []  # 损失值

    # plt,bx 背景
    pos = list(np.where(y == 1.0)[0])
    positive = X[pos]
    neg = list(np.where(y == 0.0)[0])
    negative = X[neg]
    plt.suptitle("Logistic Regression", fontsize=20)  # 添加总标题，并设置文字大小
    bx = plt.subplot(1, 2, 1)
    bx.scatter(positive[:, 1], positive[:, 2], c='b', marker='o', label='Admitted')
    bx.scatter(negative[:, 1], negative[:, 2], c='r', marker='+', label='Not Admitted')
    bx.legend()
    plt.ylim(-3, 3)
    bx.set_xlabel('Exam 1 Score')
    bx.set_ylabel('Exam 2 Score')
    plt.pause(1)
    plt.ion()

    while True:
        grad = gradient(X[k:k + batchSize], y[k:k + batchSize], theta)
        k += batchSize  # choose batch
        if k >= n:
            k = 0
            cost_ = cost(X, y, theta)
            costs.append(cost_)
            X, y = shuffleData(data)
            i += 1
            
            #right graph ax
            ax = plt.subplot(1, 2, 2)
            ax.set_xlabel('epoch')
            ax.set_ylabel('cost')
            ax.plot(np.arange(i), costs, 'r-')
            
            # draw the line
            plt.pause(0.0001)
            xx = np.linspace(-2, 3)
            yy = []
            for j in xx:
                res = (j * -(theta[1][0]) - (theta[0][0])) / (theta[2][0])
                yy.append(res)
            try:
                bx.lines.remove(lines[0])
            except Exception:
                pass
            lines = bx.plot(xx,yy)
        
        # update theta
        theta = theta - alpha * grad  

        if i > iter: break
    plt.ioff()
    plt.show()
    return theta, costs, grad


def run_logistic(data, theta, batchSize, iter, alpha):
    theta, costs, grad = descent(data, theta, batchSize, iter, alpha)

    print("theta:", theta, "\nCost:", costs[-1])
    return theta


if __name__ == '__main__':
    theta = np.array([[-2], [1], [1]])
    run_logistic(data, theta, 2, 100, alpha=0.01)   #SGD
