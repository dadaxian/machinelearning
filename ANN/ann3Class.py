import numpy as np 
import matplotlib.pyplot as plt
import time

path="D:\\fallingspace\\machinelearning\\data\\Iris\\"
data_x= np.loadtxt(path+"iris_x.dat")
data_y= np.loadtxt(path+"iris_y.dat")

# 学习率
learn_rate=0.05
output_size=3
hidden_size=7
fold_count=5
single_fold_count=(int)(data_y.size/output_size/fold_count)




# region 方法定义
# 归一化数据
def normalizefeature(data):
    x_norm = data
    meam = np.mean(data, axis=0)
    sigma = np.std(data, axis=0)
    x_norm = (data - meam) / sigma
    return x_norm

# sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# endregion



# 预处理数据
data_x=normalizefeature(data_x)
# print(data_y)
data_y=data_y.reshape(-1,1)
# print(data_y)

# 设置标准输出
y=np.zeros([data_y.size,output_size])
for i in range(data_y.size):
    y[i][(int)(data_y[i][0])]=1


data_sets=list()
for i in range(data_y.size):
    if i % single_fold_count == 0 and i != 0:
        data_sets.append(data_x[i-single_fold_count:i, :])
    if i == data_y.size-1:
        data_sets.append(data_x[i-single_fold_count-1:i+1, :])

# print(single_fold_count)
class1_x = data_x[0:50, :]
class1_label = y[0:50, :]
class2_x = data_x[50:100, :]
class2_label = y[50:100, :]
class3_x = data_x[100:150, :]
class3_label = y[100:150, :]

total=0
 # 关闭阻塞模式，打开交互模式
plt.ion() 
plt.show()
for j in range(fold_count):
    
    x_=np.delete(class1_x, range(j*single_fold_count, (j+1)*single_fold_count), 0)
    x_=np.r_[x_,np.delete(class2_x, range(j*single_fold_count, (j+1)*single_fold_count), 0)]
    x_=np.r_[x_,np.delete(class3_x, range(j*single_fold_count, (j+1)*single_fold_count), 0)]

    y_ = np.delete(class1_label, range(j*single_fold_count, (j+1)*single_fold_count), 0)
    y_ = np.r_[y_,np.delete(class2_label, range(j*single_fold_count, (j+1)*single_fold_count), 0)]
    y_ = np.r_[y_,np.delete(class3_label, range(j*single_fold_count, (j+1)*single_fold_count), 0)]
 
    test_x = np.r_[data_sets[j], data_sets[j+fold_count]]
 
    test_label = np.r_[data_y[j*single_fold_count:(j+1)*single_fold_count], data_y[(j+fold_count)*single_fold_count:(j+fold_count+1)*single_fold_count]]
    # data_x = np.mat(data_x)
    data_x = np.mat(x_)
    temp = np.ones(data_y.size-single_fold_count*output_size)
    weight_input = np.mat(np.random.normal(size=(data_x.shape[1], hidden_size)))
    weight_hidden = np.mat(np.random.normal(size=(hidden_size+1, output_size)))
    steps = 600
    loss_values = list()
 
    for i in range(steps):
        # 前向传播过程
        hidden_input = data_x*weight_input                      # ah+yh
        hidden_out = sigmoid(hidden_input)             # bn
        hidden_out_ = np.c_[hidden_out, temp]
        # print(hidden_out)                                     # weight_hidden 最后一行才是bias
        output_input = hidden_out_*weight_hidden
        output = sigmoid(output_input)
        # 计算损失
        loss = 0.5*np.sum(np.multiply(output-y_,  output-y_))
        loss_values.append(loss)
        # 反向传播过程
 
        output_error = np.multiply(np.multiply(output-y_, output), 1-output)
        dew_hidden = hidden_out_.T*output_error
        output_error_ = dew_hidden[7]
        weight_hidden_ = np.delete(weight_hidden, 7, axis=0)
        hidden_error = np.multiply(np.multiply(output_error_*weight_hidden_.T, hidden_out), 1-hidden_out)
        dew_input = data_x.T*hidden_error
 
        weight_hidden = weight_hidden-learn_rate*dew_hidden
        weight_input = weight_input-learn_rate*dew_input
 
    plt.plot(loss_values)
    plt.show()
    # plt.legend()
    temp = np.ones(test_label.size)
    hidden_input = test_x*weight_input
    hidden_out = sigmoid(hidden_input)
    hidden_out_ = np.c_[hidden_out, temp]
    output_input = hidden_out_*weight_hidden
    output = sigmoid(output_input)
 
    count = 0
    # print(output)
    # print(test_label)
    output = np.array(output)
    for i in range(test_label.size):
        outs = output[i].ravel()
        outs = outs.tolist()
        if int(test_label[i]) == outs.index(max(outs)):
            count = count+1
    print("test accuracy", count/test_label.size)
    total = total+count/test_label.size

print("accuracy:", total/fold_count)
# 显示前关掉交互模式
plt.ioff()
plt.savefig("D:\\fallingspace\\machinelearning\\ANN\\result\\ann3class"+(str)(time.time())+".png")
plt.show()