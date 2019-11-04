#coding=utf-8
import pandas as pd
import numpy as np
import plot as plts

path="D:\\fallingspace\\perceptron\\data\\ex4Data\\"
dataX= pd.read_table(path+"ex4x.dat",sep="   ",header=None,engine='python')
dataY= pd.read_table(path+"ex4Y.dat",sep="   ",header=None,engine='python')

x=dataX[0]
y=dataX[1]
value=dataY[0]
plts.show(x,y,value)
# plts.show(x,y,value)
# plts.drawLine(dataX)


 
