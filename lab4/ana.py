import numpy as np
import matplotlib.pyplot as plt

def read_result(filename):   
    with open(filename) as f:
        filedata = f.readlines()
    for line in filedata:
        if "simTicks" in line:
            numTicks = int(line.split()[1])

    return (numTicks,)

num_thread = [i for i in range(1,9,1)]
numTicks = []
for n in num_thread:
	filename = f'res/{n}.txt'
	res = read_result(filename)
	numTicks.append(res[0])


x = num_thread#点的横坐标
k1 = numTicks#线1的纵坐标
#k2 = [0.8988,0.9334,0.9435,0.9407,0.9453,0.9453]#线2的纵坐标
plt.plot(x,k1,'s-',color = 'r')#s-:方形
#plt.plot(x,k2,'o-',color = 'g',label="CNN-RLSTM")#o-:圆形
plt.xlabel("number of threads")#横坐标名字
plt.ylabel("simTicks")#纵坐标名字
plt.legend(loc = "best")#图例
#plt.show()
plt.savefig('ana.png')
