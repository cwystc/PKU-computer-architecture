./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --local
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/t2_local.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --tournament
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/t2_tournament.txt
./build/ARM/gem5.opt --outdir=configs/proj5/tmp2 configs/proj5/1_t2.py --mysimple
mv configs/proj5/tmp2/stats.txt ../PKU-computer-architecture/lab5/res/t2_mysimple.txt
