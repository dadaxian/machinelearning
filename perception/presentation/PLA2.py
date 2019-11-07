import numpy as np
import matplotlib.pyplot as plt


"""
positive为label为1的数据坐标
negtive为label为0的数据标签
"""
data1 = np.loadtxt('D:\\fallingspace\\perceptron\\data\\ex4Data\\ex4x.dat')
data2 = np.loadtxt('D:\\fallingspace\\perceptron\\data\\ex4Data\\ex4y.dat')

x = data1[:,:]
y = data2[:]
m,n = x.shape
positive = np.where(y==1)
negtive = np.where(y==0)

# 显示数据集

def show_data_set():
    fig1 = plt.figure(1)
    ax = fig1.add_subplot(1,1,1)
    ax.scatter(x[positive, 0], x[positive, 1], color='blue', marker='+', label='Addmit')
    ax.scatter(x[negtive, 0], x[negtive, 1], color='red', marker='o', label='Not Addmit')      
    plt.xlabel('Exam_x')
    plt.ylabel('Exam_y')
    plt.title('Data set 1')
    plt.legend()
    plt.show()

 
# 归一化处理数据x
def normalizefeature(x):
    u = np.mean(x, axis=0)
    v = np.std(x, axis=0)
    x = (x - u) / v
    return x
    
# 初始化W
def init_W(x):

    x = np.hstack((np.ones((x.shape[0],1)), x))
    w = np.array([1.0,1.0,1.0]).reshape(3,1)
    return x,w

def PLA(x,w,alpha,threshold,iter):
    
    # 计算x和w的乘积，如果小于阈值则y_pred设为0，否则为1 
    s = np.dot(x, w)
    y_pred = np.ones_like(y)    
    loc_n = np.where(s < threshold)[0]    
    y_pred[loc_n] = 0
    
    t = np.where(y != y_pred)[0][0]
    # 第一次更新权值
    w += y[t] * x[t, :].reshape((3,1))

    #动态绘图
    x1 = -2.5
    y1 =  -1 / w[2] * (w[0] * 1 + w[1] * x1)
    x2 = 2.5
    y2 =  -1 / w[2] * (w[0] * 1 + w[1] * x2)
    xx=np.array([x1,x2])
    yy=np.array([y1,y2])

    cost_x = np.linspace(1,iter,iter)
    cost_y = np.zeros_like(cost_x)

    err_x = np.linspace(1,iter,iter)
    err_y = np.zeros_like(err_x)
    
    fig2 = plt.figure(figsize=(10,8))
    bx = fig2.add_subplot(221)
    bx.scatter(x[positive, 1], x[positive, 2], color='blue', marker='+', label='Addmit')
    bx.scatter(x[negtive, 1], x[negtive, 2], color='red', marker='o', label='Not Addmit')  
    bx.legend(loc = 'upper left')
    bx.set_ylim([-3,2.5])
    bx.set_ylim([-3,3])
    bx.set_title('PLA')

    cx = fig2.add_subplot(223)
    dx = fig2.add_subplot(224)
    cx.set_title('cost function')
    dx.set_title('error num')
    plt.ion()
    plt.subplots_adjust(left=0.1, bottom=0.1, right=None, top=None,wspace=None, hspace=0.5)
    # pocket 算法
    for i in range(iter):#iter次迭代
        yy[0] =  -1 / w[2] * (w[0] * 1 + w[1] * x1)
        yy[1] = -1 / w[2] * (w[0] * 1 + w[1] * x2)
        
        cost = 0.0
        s = np.dot(x, w)
        y_pred = np.ones_like(y)
        loc_n = np.where(s < threshold)[0]
        y_pred[loc_n] = 0
        num_fault = len(np.where(y != y_pred)[0])
        print('No. %2d times iterator，classification errors：%2d' % (i, num_fault))
        if num_fault == 0:
            break
        else:
            r = np.random.choice(num_fault)
        
            t = np.where(y != y_pred)[0][r]
            # 临时权重w2
            w2 = w + alpha *(y[t] - y_pred[t]) * x[t, :].reshape((3,1))
            s=np.dot(x,w2)
            y_pred_2 = np.ones_like(y)
            loc_n_2 = np.where(s<threshold)[0]
            y_pred_2[loc_n_2] = 0
            num_fault_w2 = len(np.where(y!=y_pred_2)[0])
            if num_fault_w2 < num_fault:
                w = w2
        for j in range(m):
            cost += (y_pred[j] - y[j]) * np.dot(w.reshape(1,3),x[j, :])

        cost_y[i] = cost
        err_y[i] = len(np.where(y!=y_pred)[0])


        try:
            bx.lines.remove(lines_bx[0])
            cx.lines.remove(lines_cx[0])
            cx.lines.remove(lines_dx[0])
        except Exception:
            pass
        lines_bx = bx.plot(xx ,yy,'r')
        lines_cx = cx.plot(cost_x[0:i] ,cost_y[0:i],'ro',)
        lines_dx = dx.plot(err_x[0:i] ,err_y[0:i],'ro',)

        plt.pause(0.25)
    plt.ioff()
    plt.show()

if __name__ == '__main__':
    show_data_set()
    x = normalizefeature(x)
    x,w = init_W(x)
    PLA(x,w,alpha=0.2,threshold=0.0,iter=50)
