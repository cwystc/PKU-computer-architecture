./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --perceptron
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/2e8_t2_perceptron.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --perceptron_thre49
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/2e8_t2_perceptron_thre49.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --perceptron_thre109
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/2e8_t2_perceptron_thre109.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --perceptron_hislen24
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/2e8_t2_perceptron_hislen24.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --perceptron_hislen44
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/2e8_t2_perceptron_hislen44.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --perceptron_tablesz140
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/2e8_t2_perceptron_tablesz140.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --perceptron_tablesz340
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/2e8_t2_perceptron_tablesz340.txt
