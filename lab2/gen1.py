#l=['ddr3_1600_8x8','ddr3_2133_8x8','ddr4_2400_16x4','ddr4_2400_8x8','lpddr2_s4_1066_1x32','wideio_200_1x128','lpddr3_1600_1x32']
#u=['0.6','0.3','5','8']
p=['local','tournament','bimode']
ra=[8,16,32,64]
t=2
for bp in p:
	for ras in ra:
		print(f'./build/ARM/gem5.opt --outdir=configs/proj2/tmp{t+2} configs/proj2/t{t}.py --{bp} --ras={ras}')
		print(f'mv configs/proj2/tmp{t+2}/stats.txt ../PKU-computer-architecture/lab2/res/t{t}_{bp}_ras={ras}.txt')

