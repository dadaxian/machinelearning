#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('D:\\fallingspace\\perceptron\\data\\Exam\\exam_x.dat')
data2 = np.loadtxt('D:\\fallingspace\\perceptron\\data\\Exam\\exam_y.dat')
#data_x = np.load('./data/exam_x.dat',allow_pickle=True)
# %matplotlib auto
x = data1[:,:]
y = data2[:]
m,n = x.shape
# for i in range(m):
#     if y[i]==0:
#         y[i]=-1
positive = np.where(y==1)
negtive = np.where(y==0)

#分析数据集
def show_ax():
    fig1 = plt.figure(1)
    ax = fig1.add_subplot(1,1,1)
    ax.scatter(x[positive, 0], x[positive, 1], color='blue', marker='+', label='Addmit')
    ax.scatter(x[negtive, 0], x[negtive, 1], color='red', marker='o', label='Not Addmit')      
    plt.xlabel('Exam_x')
    plt.ylabel('Exam_y')
    plt.title('Title')
    plt.legend()
    plt.show()



# 归一化
def normalizefeature(x):
    # 均值 方差
    u = np.mean(x, axis=0)
    v = np.std(x, axis=0)
    x = (x - u) / v
    return x
# 初始化 w
def init_W(x):
    # X加上bias项
    x = np.hstack((np.ones((x.shape[0],1)), x))
    # 权重初始化
    w = np.array([1.5,1.5,1.5]).reshape(3,1)
    return x,w

def PLA(x,w,theta,threshold,iter):
    fig2 = plt.figure(figsize=(6,8))
    
    # plt.ylim(-3, 3)
  
    s = np.dot(x, w)
    y_pred = np.ones_like(y)    
    loc_n = np.where(s < threshold)[0]    
    y_pred[loc_n] = 0

    # 第一个分类错误的点
    t = np.where(y != y_pred)[0][0]
    # 更新权重w
    w += y[t] * x[t, :].reshape((3,1))
    #print(np.where(y != y_pred))

    x1 = -2.5
    y1 =  -1 / w[2] * (w[0] * 1 + w[1] * x1)
    x2 = 2.5
    y2 =  -1 / w[2] * (w[0] * 1 + w[1] * x2)
    xx=np.array([x1,x2])
    yy=np.array([y1,y2])


    cost_x = np.linspace(1,iter,iter)
    cost_y = np.zeros_like(cost_x)
    
    bx = fig2.add_subplot(211)
    
    bx.scatter(x[positive, 1], x[positive, 2], color='blue', marker='+', label='Addmit')
    bx.scatter(x[negtive, 1], x[negtive, 2], color='red', marker='o', label='Not Addmit')  
    bx.legend()
   
    plt.pause(1)
    plt.ion()

    cx = fig2.add_subplot(212)
    for i in range(iter):#15次迭代
        yy[0] =  -1 / w[2] * (w[0] * 1 + w[1] * x1)
        yy[1] = -1 / w[2] * (w[0] * 1 + w[1] * x2)

        cost = 0.0
        for j in range(m):
            cost += (y_pred[j] - y[j]) * np.dot(w.reshape(1,3),x[j, :])

        cost_y[i] = cost
        # lines = plt.plot(cost_x ,cost_y,'r')

        try:
            bx.lines.remove(bx.lines_bx[0])
            cx.lines.remove(cx.lines_cx[0])
        except Exception:
            pass
        lines_bx = bx.plot(xx ,yy,'r')
        lines_cx = cx.plot(cost_x[0:i] ,cost_y[0:i],'r')
        plt.pause(0.2)
    
        s = np.dot(x, w)
        y_pred = np.ones_like(y)
        loc_n = np.where(s < threshold)[0]
        y_pred[loc_n] = 0
        num_fault = len(np.where(y != y_pred)[0])
        print('No. %2d time iterator,classification errors,%2d' % (i, num_fault))
        if num_fault == 0:
            break
        else:
            r = np.random.choice(num_fault)
        
            t = np.where(y != y_pred)[0][r]
            w2 = w + theta *(y[t] - y_pred[t]) * x[t, :].reshape((3,1))
            s=np.dot(x,w2)
            y_pred_2 = np.ones_like(y)
            loc_n_2 = np.where(s<threshold)[0]
            y_pred_2[loc_n_2] = 0
            num_fault_w2 = len(np.where(y!=y_pred_2)[0])
            if num_fault_w2 < num_fault:
                w = w2
    print(cost_x)
    print(cost_y)




# x1 = -2.5
# y1 =  -1 / w[2] * (w[0] * 1 + w[1] * x1)
# x2 = 2.5
# y2 =  -1 / w[2] * (w[0] * 1 + w[1] * x2)
# fig3 = plt.figure(figsize=(12,6))
# plt.ylim(-3, 3)
# plt.xlim(-3, 3)
# cx = fig3.add_subplot(1,1,1)
# cx.plot([x1,x2], [y1,y2],'r')
# # 作图
# cx.scatter(x[positive, 1], x[positive, 2], color='blue', marker='+', label='Addmit')
# cx.scatter(x[negtive, 1], x[negtive, 2], color='red', marker='o', label='Not Addmit')  
# plt.xlabel('Exam_x')
# plt.ylabel('Exam_y')
# plt.title('Title')
# plt.legend()


if __name__ == '__main__':
    theta = 0.5
    iter = 30
    threshold = 0.2
    show_ax()
    x = normalizefeature(x)
    x,w = init_W(x)
    PLA(x,w,theta,threshold,iter)
