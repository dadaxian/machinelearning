#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('D:\\fallingspace\\perceptron\\data\\Exam\\exam_x.dat')
data2 = np.loadtxt('D:\\fallingspace\\perceptron\\data\\Exam\\exam_y.dat')
#data_x = np.load('./data/exam_x.dat',allow_pickle=True)

x = data1[:,:]
y = data2[:]
m,n = x.shape
for i in range(m):
    if y[i]==0:
        y[i]=-1

positive = np.where(y==1)
negtive = np.where(y==-1)
plt.scatter(x[positive, 0], x[positive, 1], color='blue', marker='+', label='Addmit')
plt.scatter(x[negtive, 0], x[negtive, 1], color='red', marker='o', label='Not Addmit')      
plt.xlabel('Exam_x')
plt.ylabel('Exam_y')
plt.title('Title')
plt.legend()
plt.show()

# 均值
u = np.mean(x, axis=0)
# 方差
v = np.std(x, axis=0)
x = (x - u) / v

plt.scatter(x[positive, 0], x[positive, 1], color='blue', marker='+', label='Addmit')
plt.scatter(x[negtive, 0], x[negtive, 1], color='red', marker='o', label='Not Addmit')
plt.xlabel('Exam_x')
plt.ylabel('Exam_y')
plt.title('Title')
plt.show()

# X加上偏置项
x = np.hstack((np.ones((x.shape[0],1)), x))
print(x)
# 权重初始化
w = np.array([1.0,1.0,1.0]).reshape(3,1)
print(w)

# 直线第一个坐标（x1，y1）
x1 = -2.5
y1 =  -1 / w[2] * (w[0] * 1 + w[1] * x1)
# 直线第二个坐标（x2，y2）
x2 = 2.5
y2 =  -1 / w[2] * (w[0] * 1 + w[1] * x2)
# 作图
plt.scatter(x[positive, 1], x[positive, 2], color='blue', marker='+', label='Addmit')
plt.scatter(x[negtive, 1], x[negtive, 2], color='red', marker='o', label='Not Addmit')  
plt.plot([x1,x2], [y1,y2],'r')
plt.xlabel('Exam_x')
plt.ylabel('Exam_y')
plt.title('Title')
plt.legend()
plt.show()

s = np.dot(x, w)
y_pred = np.ones_like(y)    # 预测输出初始化
loc_n = np.where(s < 0)[0]    # 大于零索引下标
y_pred[loc_n] = 0

# 第一个分类错误的点
t = np.where(y != y_pred)[0][0]
# 更新权重w
w += y[t] * x[t, :].reshape((3,1))

#搜索错误数最少的权重
min_num = len(np.where(y != y_pred)[0])
best_weight = w.copy()

for i in range(15):#15次迭代
    s = np.dot(x, w)
    y_pred = np.ones_like(y)
    loc_n = np.where(s < 0)[0]
    y_pred[loc_n] = -1
    num_fault = len(np.where(y != y_pred)[0])
    print('%2depoch,wrong count:%2d' % (i, num_fault))
    if num_fault < min_num :
        min_num = num_fault
        best_weight = w.copy()     
    if num_fault == 0:
        break
    else:
        t = np.where(y != y_pred)[0][0]
        w += y[t] * x[t, :].reshape((3,1))
# 直线第一个坐标（x1，y1）
print('wrong count：%2d' % (min_num))
w = best_weight.copy()
x1 = -2.5
y1 =  -1 / w[2] * (w[0] * 1 + w[1] * x1)
# 直线第二个坐标（x2，y2）
x2 = 2.5
y2 =  -1 / w[2] * (w[0] * 1 + w[1] * x2)
plt.plot([x1,x2], [y1,y2],'r')
# 作图
plt.scatter(x[positive, 1], x[positive, 2], color='blue', marker='+', label='Addmit')
plt.scatter(x[negtive, 1], x[negtive, 2], color='red', marker='o', label='Not Addmit')  
plt.xlabel('Exam_x')
plt.ylabel('Exam_y')
plt.title('Title')
plt.legend()
plt.show()
