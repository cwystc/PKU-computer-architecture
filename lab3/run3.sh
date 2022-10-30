./build/ARM/gem5.opt --outdir=configs/proj3/tmp3 configs/proj3/t3.py --Random
mv configs/proj3/tmp3/stats.txt ../PKU-computer-architecture/lab3/res/t3_Random.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp3 configs/proj3/t3.py --LRU
mv configs/proj3/tmp3/stats.txt ../PKU-computer-architecture/lab3/res/t3_LRU.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp3 configs/proj3/t3.py --MRU
mv configs/proj3/tmp3/stats.txt ../PKU-computer-architecture/lab3/res/t3_MRU.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp4 configs/proj3/t4.py --Random
mv configs/proj3/tmp4/stats.txt ../PKU-computer-architecture/lab3/res/t4_Random.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp4 configs/proj3/t4.py --LRU
mv configs/proj3/tmp4/stats.txt ../PKU-computer-architecture/lab3/res/t4_LRU.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp4 configs/proj3/t4.py --MRU
mv configs/proj3/tmp4/stats.txt ../PKU-computer-architecture/lab3/res/t4_MRU.txt
