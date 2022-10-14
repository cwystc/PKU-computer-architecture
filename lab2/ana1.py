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

    return (numInsts / numCycles, 1.0 - numIncorrect / numPred)

task = "t1"
predictor = ["local", "tournament", "bimode"]

IPC = []
HIT = []
print(task)

for p in predictor:
    filename = f'res/{task}_{p}_btbentry=4096.txt'
    res = read_result(filename)
    IPC.append(res[0])
    HIT.append(res[1])

M = [[], [], [], []]

for i in range(3):
	M[i]=HIT[i]
'''
for i,p in enumerate(predictor):
	M[i].append(ErrorRate)
    print(name + " predictor ", end="")
#    for btb in [10424, 2048, 4096, 8192]:
#        filename = p + "-" + task + ("-BTB" + str(btb) if btb != 4096 else "") + "/stats.txt"
    for ras in [4, 8, 16, 32]:
        filename = p + "-" + task + ("-RAS" + str(ras) if ras != 16 else "") + "/stats.txt"
        res = read_result(filename)
        print("& $%.6lf\\%%$ " % (res[1] * 100), end="")

        M[Map[ras]].append(res[1])
    print("\\\\ \n \\hline")
'''



fig, ax1 = plt.subplots()
ax1.set_ylabel('Hit Rate')
ax1.bar([0.0 ], M[0], width=0.2, color="lightseagreen", align='edge', label = predictor[0])
ax1.bar([0.2], M[1], width=0.2, color="tab:blue", align='edge', label = predictor[1])
ax1.bar([0.4], M[2], width=0.2, color="orange", align='edge', label = predictor[2])

ax1.set_xticklabels(ax1.get_xticklabels())

plt.legend(loc = "upper right")
# plt.tight_layout()
# plt.show()
plt.savefig("bar graph/1_2mm_HIT.png")
