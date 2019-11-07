#coding=utf-8
import pandas as pd
import numpy as np
import plot as plts
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

threshold=0.5
learning_rate=0.1
weights=[0,0,0]
training_set=[((1,0,0),1),((1,0,1),1),((1,1,0),1),((1,1,1),0)]

def dot_product(values,weights):
    return sum(value*weight for value, weight in zip(values,weights))


fig, ax = plt.subplots()
 # line的数据
x = np.linspace(20,60)
y=x*-2+150
# 创建线，并添加
line1=ax.add_line(Line2D(x, y, linewidth=1, color='red'))

while(True):
    print('-'*60)
    error_count=0
    print(weights)
    for input_vector,desired_output in training_set:
        print(input_vector)
        result=dot_product(input_vector,weights)>threshold
        error=desired_output-result
        if error!=0:
            error_count+=1
            for index,value in enumerate(input_vector):
                weights[index]=weights[index]+learning_rate*error*value
    y = (-weights[1] * x- weights[0])/weights[2]
    try:
        ax.lines.remove(ax.lines[0])
    except Exception:
        pass
    lines = ax.plot(x ,y)
    plt.pause(1)


    if error_count==0:
        break
# 显示前关掉交互模式
plt.ioff()
plt.show()