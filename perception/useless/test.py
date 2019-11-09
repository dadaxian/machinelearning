#coding=utf-8

import numpy as np

# for j in range(0,2):
#     print(j)

# path="D:\\fallingspace\\perceptron\\data\\ex4Data\\"
# data= np.loadtxt(path+"ex4x.dat")
# value= np.loadtxt(path+"ex4Y.dat")

# def shuffleData(data,value):
#     tempData=[]
#     for index,item in enumerate(data):
#         tempData.append([item[0],item[1],value[index]])
#     print(tempData)
#     np.random.shuffle(tempData)
#     print(tempData)
#     tempData=np.array(tempData)
#     return tempData[...,:2],tempData[...,2]

# print(shuffleData(data,value))

# a = np.random.randint(0,10,size=[50,2])
# b=np.random.randint(11,20,size=[50,2])

# data=np.vstack((a,b))

# value=[]
# for index,item in enumerate(a):
#     value.append(1)
# for index,item in enumerate(b):
#     value.append(-1)
# # print(value)
# for i in range(4):
#     print(i)
print(np.mat(np.random.normal(size=(2, 7))))