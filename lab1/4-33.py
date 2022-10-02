tasks = ['123', '2mm', 'bfs', 'bzip2', 'mcf']
l=['ddr3_1600_8x8','ddr3_2133_8x8','ddr4_2400_16x4','ddr4_2400_8x8','lpddr2_s4_1066_1x32','wideio_200_1x128','lpddr3_1600_1x32']
cpu = ['o3', 'inorder']
u=['0.3','0.6','0.9','1.8','2.7','3.6','5','8']
print('sim seconds',end=', ')
for i in range(1,5,1):
	if (i<4):
		print(f'{tasks[i]}', end = ', ')
	else:
		print(f'{tasks[i]}')
dram = 'ddr4_2400_16x4'
for c in cpu:
	for freq in u:
		print(f'{c} {freq}GHZ', end='')
		for i in range(1,5,1):
			f = open(f'res/t{i}_{dram}_{freq}GHZ_{c}.txt', 'r', encoding="utf-8")
			for ss in f:
				s=ss.split()
				if (len(s)>0):
					#print(s)
					if (s[0]=='simInsts'):
						I=int(s[1])
					elif (s[0]=='system.cpu.numCycles'):
						C=int(s[1])
					elif (s[0]=='simSeconds'):
						S=float(s[1])
			print(f', {S}', end='')
		print()
