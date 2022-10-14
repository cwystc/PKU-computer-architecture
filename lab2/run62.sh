./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --tournament --localhissize=1024
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_localhissize=1024.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --tournament --localhissize=2048
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_localhissize=2048.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --tournament --localhissize=4096
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_localhissize=4096.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --tournament --localhissize=8192
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_localhissize=8192.txt
