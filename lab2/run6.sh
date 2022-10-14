./build/ARM/gem5.opt --outdir=configs/proj2/tmp4 configs/proj2/t2.py --bimode --globalsize=2048
mv configs/proj2/tmp4/stats.txt ../PKU-computer-architecture/lab2/res/t2_bimode_globalsize=2048.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp4 configs/proj2/t2.py --bimode --globalsize=4096
mv configs/proj2/tmp4/stats.txt ../PKU-computer-architecture/lab2/res/t2_bimode_globalsize=4096.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp4 configs/proj2/t2.py --bimode --globalsize=8192
mv configs/proj2/tmp4/stats.txt ../PKU-computer-architecture/lab2/res/t2_bimode_globalsize=8192.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp4 configs/proj2/t2.py --bimode --globalsize=16384
mv configs/proj2/tmp4/stats.txt ../PKU-computer-architecture/lab2/res/t2_bimode_globalsize=16384.txt
