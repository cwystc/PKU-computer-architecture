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

    return (numInsts / numCycles, (imis+dmis)/(ihit+dhit+imis+dmis), l2misrate)

tt = 1
tas = (f't{tt}')
policy = ["LRU", "MRU", "Random", "Clock"]
task = ["?", "2mm", "bfs", "bzip2", "mcf"]

IPC = []
L1MIS = []
L2MIS = []
print(tas)

for p in policy:
    filename = f'res/{tas}_{p}.txt'
    res = read_result(filename)
    IPC.append(res[0])
    L1MIS.append(res[1])
    L2MIS.append(res[2])

M = [[], [], [], []]

for i in range(4):
	M[i]=L1MIS[i]



fig, ax1 = plt.subplots()
ax1.set_ylabel('L1MIS')
ax1.bar([0.0 ], M[0], width=0.2, color="red", align='edge', label = policy[0])
ax1.bar([0.2], M[1], width=0.2, color="orange", align='edge', label = policy[1])
ax1.bar([0.4], M[2], width=0.2, color="yellow", align='edge', label = policy[2])
ax1.bar([0.6], M[3], width=0.2, color="green", align='edge', label = policy[3])

ax1.set_xticklabels(ax1.get_xticklabels())

plt.legend(loc = "upper right")
# plt.tight_layout()
# plt.show()
plt.savefig(f'bar graph/{task[tt]}_L1MIS.png')
