./build/ARM/gem5.opt --outdir=configs/proj5/tmp1 configs/proj5/1_t1.py --local
mv configs/proj5/tmp1/stats.txt ../PKU-computer-architecture/lab5/res/t1_local.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp1 configs/proj5/1_t1.py --tournament
mv configs/proj5/tmp1/stats.txt ../PKU-computer-architecture/lab5/res/t1_tournament.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp1 configs/proj5/1_t1.py --mysimple
mv configs/proj5/tmp1/stats.txt ../PKU-computer-architecture/lab5/res/t1_mysimple.txt
