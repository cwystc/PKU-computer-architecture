./build/ARM/gem5.opt --outdir=configs/proj2/tmp1 configs/proj2/t2.py --tournament --localsize=1024
mv configs/proj2/tmp1/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_localsize=1024.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp1 configs/proj2/t2.py --tournament --localsize=2048
mv configs/proj2/tmp1/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_localsize=2048.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp1 configs/proj2/t2.py --tournament --localsize=4096
mv configs/proj2/tmp1/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_localsize=4096.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp1 configs/proj2/t2.py --tournament --localsize=8192
mv configs/proj2/tmp1/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_localsize=8192.txt
