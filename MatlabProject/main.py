import matplotlib.pyplot as plt
import numpy as np

A = 1  # bottom plate is moving in negative x-direction
U = -8  # where U= C
b = 1
mu = 7.975e-4
P_Grand = []
P2 = []
P = []
X = []
MiniX = []
Y = []
arr = ['k','y','m','k','c','b','g','r','k','g','r']
count = 0

P = np.arange(-5, 6, 1)

Y = np.arange(0, 1.01, 0.01)

for i in P:
    P_Grand.append(-(i * 2 * mu * U) / pow(b, 2))
for i in P_Grand:
    P2.append(((pow(b, 2)) / (2 * mu * U)) * i)

for i in P2:
    for j in Y:
        MiniX.append((-i * pow(j, 2)) + (((i + 1) * j) - 1))
    X.append(MiniX)
    MiniX = []

for i in X:
    plt.plot(i,Y,arr[count])
    count+=1
plt.xlabel('u/U',fontsize=20)
plt.ylabel('y/b',fontsize=20)
plt.title('FLUID VELOCITY PROFILE',fontsize=22)
plt.grid()
plt.legend(['P=- 5','P=- 4','P=- 3','P=- 2','P=- 1','P= 0','P= 1','P= 2','P= 3','P= 4','P= 5'],loc="lower right",prop={'size': 10})
fig = plt.gcf()
fig.set_size_inches(10, 8)
fig.savefig('test.png', dpi=100)
plt.show()


