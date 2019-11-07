#coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

def plotPic(data):
    print(data)

def mscatter(x,y,ax=None, m=None, **kw):
    import matplotlib.markers as mmarkers
    if not ax: ax=plt.gca()
    sc = ax.scatter(x,y,**kw)
    if (m is not None) and (len(m)==len(x)):
        paths = []
        for marker in m:
            if isinstance(marker, mmarkers.MarkerStyle):
                marker_obj = marker
            else:
                marker_obj = mmarkers.MarkerStyle(marker)
            path = marker_obj.get_path().transformed(
                        marker_obj.get_transform())
            paths.append(path)
        sc.set_paths(paths)
    return sc

def show3Class(x,y,value):
    marker={0:'o',1:'*',2:'^'}
    cmarker=list(map(lambda x:marker[x],value))
    fig, ax = plt.subplots()
    scatter = mscatter(x, y, c='', m=cmarker, ax=ax,cmap=plt.cm.RdYlBu,edgecolors='k')
    plt.show()

def show(xX,yX,value):
    marker={0:'o',1:'+'}
    cmarker=list(map(lambda x:marker[x],value))
    fig, ax = plt.subplots()
    scatter = mscatter(xX, yX, c='b', m=cmarker, ax=ax,cmap=plt.cm.RdYlBu)
    plt.show()

def drawLine(data):
    figure, ax = plt.subplots()
    # 设置x，y值域
    ax.set_xlim(left=0, right=20)
    ax.set_ylim(bottom=0, top=10)
    # 两条line的数据
    line1 = [(1, 1), (5, 5)]
    line2 = [(11, 9), (8, 8)]
    (line1_xs, line1_ys) = zip(*line1)
    (line2_xs, line2_ys) = zip(*line2)
    # 创建两条线，并添加
    ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='blue'))
    ax.add_line(Line2D(line2_xs, line2_ys, linewidth=1, color='red'))
    plt.show()
def fixShow(xX,yX,value):
    marker={0:'o',1:'+'}
    cmarker=list(map(lambda x:marker[x],value))
    fig, ax = plt.subplots()
     # line的数据
    line1 = [(20, 80), (60, 40)]
    (line1_xs, line1_ys) = zip(*line1)

    # 创建线，并添加
    ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='red'))

    scatter = mscatter(xX, yX, c='b', m=cmarker, ax=ax,cmap=plt.cm.RdYlBu)
    plt.show()
def fixShow1(xX,yX,value):
    marker={0:'o',1:'+'}
    cmarker=list(map(lambda x:marker[x],value))
    fig, ax = plt.subplots()
     # line的数据
    x = np.linspace(20,60)
    y=x*-2+150

    # 创建线，并添加
    line1=ax.add_line(Line2D(x, y, linewidth=1, color='red'))
    print(ax.lines)
    scatter = mscatter(xX, yX, c='b', m=cmarker, ax=ax,cmap=plt.cm.RdYlBu)
    # 关闭阻塞模式，打开交互模式
    plt.ion()   
    for i in range(10):
        y = x*(-i*4) + 50*i
        try:
            ax.lines.remove(ax.lines[0])
        except Exception:
            pass
        lines = ax.plot(x ,y)
        plt.pause(1)
    # 显示前关掉交互模式
    plt.ioff()
    plt.show()
def startFixShow1(xX,yX,value):
    marker={0:'o',1:'+'}
    cmarker=list(map(lambda x:marker[x],value))
    fig, ax = plt.subplots()
     # line的数据
    x = np.linspace(20,60)
    y=x*-2+150

    # 创建线，并添加
    line1=ax.add_line(Line2D(x, y, linewidth=1, color='red'))
    print(ax.lines)
    scatter = mscatter(xX, yX, c='b', m=cmarker, ax=ax,cmap=plt.cm.RdYlBu)
    # 关闭阻塞模式，打开交互模式
    plt.ion()   
    return plt.axis
def changeLine(ax):
    # line的数据
    x = np.linspace(20,60)
    for i in range(10):
        y = x*(-i*4) + 50*i
        try:
            plt.axis.lines.remove(ax.lines[0])
        except Exception:
            pass
        lines = plt.axis.plot(x ,y)
        plt.pause(1)
    # 显示前关掉交互模式
    plt.ioff()
    plt.show()