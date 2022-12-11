#p=['local','tournament','mysimple']
#p = ['perceptron']
p = ['perceptron', 'perceptron_thre49', 'perceptron_thre109', 'perceptron_hislen24', 'perceptron_hislen44','perceptron_tablesz140', 'perceptron_tablesz340']
t=2
for bp in p:
	print(f'./build/ARM/gem5.opt --outdir=configs/proj5/tmp{t} configs/proj5/1_t{t}.py --{bp}')
	print(f'mv configs/proj5/tmp{t}/stats.txt ../PKU-computer-architecture/lab5/res/2e8_t{t}_{bp}.txt')

