./build/ARM/gem5.opt --outdir=configs/proj3/tmp2 configs/proj3/t2.py --Random
mv configs/proj3/tmp2/stats.txt ../PKU-computer-architecture/lab3/res/t2_Random.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp2 configs/proj3/t2.py --LRU
mv configs/proj3/tmp2/stats.txt ../PKU-computer-architecture/lab3/res/t2_LRU.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp2 configs/proj3/t2.py --MRU
mv configs/proj3/tmp2/stats.txt ../PKU-computer-architecture/lab3/res/t2_MRU.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp4 configs/proj3/t4.py --Random
mv configs/proj3/tmp4/stats.txt ../PKU-computer-architecture/lab3/res/t4_Random.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp4 configs/proj3/t4.py --LRU
mv configs/proj3/tmp4/stats.txt ../PKU-computer-architecture/lab3/res/t4_LRU.txt
./build/ARM/gem5.opt --outdir=configs/proj3/tmp4 configs/proj3/t4.py --MRU
mv configs/proj3/tmp4/stats.txt ../PKU-computer-architecture/lab3/res/t4_MRU.txt
