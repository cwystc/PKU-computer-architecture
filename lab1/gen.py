#l=['ddr3_1600_8x8','ddr3_2133_8x8','ddr4_2400_16x4','ddr4_2400_8x8','lpddr2_s4_1066_1x32','wideio_200_1x128','lpddr3_1600_1x32']
u=['0.6','0.3','5','8']
t=4
for f in u:
	print(f'./build/ARM/gem5.opt --outdir=configs/proj1/tmp{t} configs/proj1/t{t}.py --cpu_clock={f}GHz --ddr4_2400_16x4 --o3')
	print(f'mv configs/proj1/tmp{t}/stats.txt ../PKU-computer-architecture/lab1/res/t{t}_ddr4_2400_16x4_{f}GHZ_o3.txt')
	print(f'./build/ARM/gem5.opt --outdir=configs/proj1/tmp{t} configs/proj1/t{t}.py --cpu_clock={f}GHz --ddr4_2400_16x4 --inorder')
	print(f'mv configs/proj1/tmp{t}/stats.txt ../PKU-computer-architecture/lab1/res/t{t}_ddr4_2400_16x4_{f}GHZ_inorder.txt')
	
