./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t2.py --tournament --globalsize=2048
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_globalsize=2048.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t2.py --tournament --globalsize=4096
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_globalsize=4096.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t2.py --tournament --globalsize=8192
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_globalsize=8192.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t2.py --tournament --globalsize=16384
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_globalsize=16384.txt
