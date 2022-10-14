./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --local --btbentry=1024
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_local_btbentry=1024.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --local --btbentry=2048
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_local_btbentry=2048.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --local --btbentry=4096
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_local_btbentry=4096.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --local --btbentry=8192
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_local_btbentry=8192.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --tournament --btbentry=1024
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_btbentry=1024.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --tournament --btbentry=2048
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_btbentry=2048.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --tournament --btbentry=4096
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_btbentry=4096.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --tournament --btbentry=8192
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_tournament_btbentry=8192.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --bimode --btbentry=1024
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_bimode_btbentry=1024.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --bimode --btbentry=2048
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_bimode_btbentry=2048.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --bimode --btbentry=4096
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_bimode_btbentry=4096.txt
./build/ARM/gem5.opt --outdir=configs/proj2/tmp2 configs/proj2/t2.py --bimode --btbentry=8192
mv configs/proj2/tmp2/stats.txt ../PKU-computer-architecture/lab2/res/t2_bimode_btbentry=8192.txt
