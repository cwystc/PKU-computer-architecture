./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --local --ras=8
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_local_ras=8.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --local --ras=16
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_local_ras=16.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --local --ras=32
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_local_ras=32.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --local --ras=64
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_local_ras=64.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --tournament --ras=8
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_tournament_ras=8.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --tournament --ras=16
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_tournament_ras=16.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --tournament --ras=32
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_tournament_ras=32.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --tournament --ras=64
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_tournament_ras=64.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --bimode --ras=8
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_bimode_ras=8.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --bimode --ras=16
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_bimode_ras=16.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --bimode --ras=32
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_bimode_ras=32.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp3 configs/proj2/t1.py --bimode --ras=64
mv configs/proj2/tmp3/stats.txt ../PKU-computer-architecture/lab2/res/t1_bimode_ras=64.txt
