import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


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

task = "t2"
predictor = ["tournament"]

IPC = []
MISS = []
print(task)

gs=[2048,4096,8192,16384]

for gsz in gs:
	filename = f'res/t2_tournament_globalsize={gsz}.txt'
	res = read_result(filename)
	IPC.append(res[0])
	MISS.append(res[1])

M = [[], [], [], []]


for j in range(4):
	M[j].append(IPC[j])

fig, ax1 = plt.subplots()
ax1.set_ylabel('IPC')

ax1.bar([0.0 ], M[0], width=0.2, color="red", align='edge', label = gs[0])
ax1.bar([0.2], M[1], width=0.2, color="orange", align='edge', label = gs[1])
ax1.bar([0.4], M[2], width=0.2, color="blue", align='edge', tick_label = predictor, label = gs[2])
ax1.bar([0.6], M[3], width=0.2, color="lightseagreen", align='edge', label = gs[3])

ax1.set_xticklabels(ax1.get_xticklabels())


plt.legend(loc = "upper right")
# plt.tight_layout()
# plt.show()
plt.savefig("bar graph/6_globalsize_IPC.png")
