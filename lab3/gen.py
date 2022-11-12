r=['Clock']

for t in {2}:
	for rp in r:
		print(f'./build/ARM/gem5.opt --outdir=configs/proj3/tmp{t} configs/proj3/t{t}.py --{rp}')
		print(f'mv configs/proj3/tmp{t}/stats.txt ../PKU-computer-architecture/lab3/res/t{t}_{rp}.txt')
