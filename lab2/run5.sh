./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --local --localsize=1024
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_local_localsize=1024.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --local --localsize=2048
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_local_localsize=2048.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --local --localsize=4096
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_local_localsize=4096.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --local --localsize=8192
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_local_localsize=8192.txt
