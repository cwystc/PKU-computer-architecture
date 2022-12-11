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
        if "system.cpu.icache.overallMisses::total" in line:
            imis = int(line.split()[1])
        if "system.cpu.dcache.overallMisses::total" in line:
            dmis = int(line.split()[1])
        if "system.cpu.icache.overallHits::total" in line:
            ihit = int(line.split()[1])
        if "system.cpu.dcache.overallHits::total" in line:
        	dhit = int(line.split()[1])
        if "system.l2cache.overallMissRate::total" in line:
        	l2misrate = float(line.split()[1])
        if "system.cpu.commit.branchMispredicts" in line:
        	branchmis = int(line.split()[1])
        if "system.cpu.numBranches" in line:
        	numbranch = int(line.split()[1])
        if "system.cpu.branchPred.condPredicted" in line:
            numPred = int(line.split()[1])
        if "system.cpu.branchPred.condIncorrect" in line:
            numIncorrect = int(line.split()[1])

    return (numInsts / numCycles, numIncorrect / numPred)

tt = 1
tas = (f't{tt}')
task = ["?", "2mm", "bfs"]
bp = ["mysimple", "local", "tournament", "perceptron", "multiperspectiveperceptron"]

IPC = []
BPMIS = []
print(tas)

for p in bp:
    filename = f'res/{tas}_{p}.txt'
    res = read_result(filename)
    IPC.append(res[0])
    BPMIS.append(res[1])

M = [[], [], [], [], []]

for i in range(5):
	M[i].append(IPC[i])



fig, ax1 = plt.subplots()
ax1.set_ylabel('IPC')
ax1.bar([0.0 ], M[0], width=0.2, color="red", align='edge', label = bp[0])
ax1.bar([0.2], M[1], width=0.2, color="orange", align='edge', label = bp[1])
ax1.bar([0.4], M[2], width=0.2, color="yellow", align='edge', label = bp[2])
ax1.bar([0.6], M[3], width=0.2, color="green", align='edge', label = bp[3])
ax1.bar([0.8], M[4], width=0.2, color="blue", align='edge', label = bp[4])

ax1.set_xticklabels(ax1.get_xticklabels())

plt.legend(loc = "upper right")
# plt.tight_layout()
# plt.show()
plt.savefig(f'bar graph/22_{task[tt]}_IPC.png')
