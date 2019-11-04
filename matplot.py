import matplotlib.pyplot as plt
import numpy as  np

# fig = plt.figure(figsize = (12, 6))
# ax1=fig.add_subplot(121)
# ax2=fig.add_subplot(122)
# x=np.linspace(1,4)
# y=x*2
# ax1.plot(x,y)
# ax1.fill(x,y,'b',alpha=0.5)
# ax2.plot(x,x*x)
# plt.show()


 
x= np.linspace(0,5*np.pi, 1000)
 
y1 = np.sin(x)
y2 = np.sin(2*x)
 
#plt.plot(x,y1)
#plt.plot(x,y2)
 
plt.fill(y1,y2,'b',alpha=0.5)

 
# plt.fill_between(x,y1,y2,facecolor='green')
plt.grid(True)
 
plt.show()
