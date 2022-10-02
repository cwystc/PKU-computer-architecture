tasks = ['123', '2mm', 'bfs', 'bzip2', 'mcf']
l=['ddr3_1600_8x8','ddr3_2133_8x8','ddr4_2400_16x4','ddr4_2400_8x8','lpddr2_s4_1066_1x32','wideio_200_1x128','lpddr3_1600_1x32']
print('bandwidth',end=', ')
for i,dram in enumerate(l):
	if (i<6):
		print(dram, end = ', ')
	else:
		print(dram)
for t in range(1,5,1):
	print(tasks[t], end=', ')
	for i,dram in enumerate(l):
		f = open(f'res/t{t}_{dram}.txt', 'r', encoding="utf-8")
		for ss in f:
			s=ss.split()
			if (len(s)>0):
				#print(s)
				if (s[0]=='system.mem_ctrl.dram.bwTotal::total'):
					B=int(s[1])
		if (i<6):
			print(f'{B}', end=', ')
		else:
			print(f'{B}')


