import numpy as np
import matplotlib.pyplot as plt

def read_result(filename):   
    with open(filename) as f:
        filedata = f.readlines()
    for line in filedata:
        if "system.cpu.numCycles" in line:
            numCycles = int(line.split()[1])
        if "simInsts" in line:
            numInsts = int(line.split()[1])
        if "system.cpu.branchPred.condPredicted" in line:
            numPred = int(line.split()[1])
        if "system.cpu.branchPred.condIncorrect" in line:
            numIncorrect = int(line.split()[1])

    return (numInsts / numCycles, numIncorrect / numPred)

task = "t1"
predictor = ["local", "tournament", "bimode"]

IPC = []
MISS = []
print(task)

bt=[1024,2048,4096,8192]

for p in predictor:
	for btb in bt:
		filename = f'res/{task}_{p}_btbentry={btb}.txt'
		res = read_result(filename)
		IPC.append(res[0])
		MISS.append(res[1])

M = [[], [], [], []]


for i in range(3):
	for j in range(4):
		M[j].append(IPC[i*4+j])

fig, ax1 = plt.subplots()
ax1.set_ylabel('IPC')
ax1.bar([0.0,1.0,2.0 ], M[0], width=0.2, color="red", align='edge', label = bt[0])
ax1.bar([0.2,1.2,2.2], M[1], width=0.2, color="orange", align='edge', label = bt[1])
ax1.bar([0.4,1.4,2.4], M[2], width=0.2, color="blue", align='edge', tick_label = predictor, label = bt[2])
ax1.bar([0.6,1.6,2.6], M[3], width=0.2, color="lightseagreen", align='edge', label = bt[3])

ax1.set_xticklabels(ax1.get_xticklabels())

plt.legend(loc = "upper right")
# plt.tight_layout()
# plt.show()
plt.savefig("bar graph/2_2mm_IPC.png")
