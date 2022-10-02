./build/ARM/gem5.opt --outdir=configs/proj1/tmp1 configs/proj1/t1.py --cpu_clock=0.6GHz --ddr4_2400_16x4 --o3
mv configs/proj1/tmp1/stats.txt ../PKU-computer-architecture/lab1/res/t1_ddr4_2400_16x4_0.6GHZ_o3.txt
./build/ARM/gem5.opt --outdir=configs/proj1/tmp1 configs/proj1/t1.py --cpu_clock=0.6GHz --ddr4_2400_16x4 --inorder
mv configs/proj1/tmp1/stats.txt ../PKU-computer-architecture/lab1/res/t1_ddr4_2400_16x4_0.6GHZ_inorder.txt
./build/ARM/gem5.opt --outdir=configs/proj1/tmp1 configs/proj1/t1.py --cpu_clock=0.3GHz --ddr4_2400_16x4 --o3
mv configs/proj1/tmp1/stats.txt ../PKU-computer-architecture/lab1/res/t1_ddr4_2400_16x4_0.3GHZ_o3.txt
./build/ARM/gem5.opt --outdir=configs/proj1/tmp1 configs/proj1/t1.py --cpu_clock=0.3GHz --ddr4_2400_16x4 --inorder
mv configs/proj1/tmp1/stats.txt ../PKU-computer-architecture/lab1/res/t1_ddr4_2400_16x4_0.3GHZ_inorder.txt
./build/ARM/gem5.opt --outdir=configs/proj1/tmp1 configs/proj1/t1.py --cpu_clock=5GHz --ddr4_2400_16x4 --o3
mv configs/proj1/tmp1/stats.txt ../PKU-computer-architecture/lab1/res/t1_ddr4_2400_16x4_5GHZ_o3.txt
./build/ARM/gem5.opt --outdir=configs/proj1/tmp1 configs/proj1/t1.py --cpu_clock=5GHz --ddr4_2400_16x4 --inorder
mv configs/proj1/tmp1/stats.txt ../PKU-computer-architecture/lab1/res/t1_ddr4_2400_16x4_5GHZ_inorder.txt
./build/ARM/gem5.opt --outdir=configs/proj1/tmp1 configs/proj1/t1.py --cpu_clock=8GHz --ddr4_2400_16x4 --o3
mv configs/proj1/tmp1/stats.txt ../PKU-computer-architecture/lab1/res/t1_ddr4_2400_16x4_8GHZ_o3.txt
./build/ARM/gem5.opt --outdir=configs/proj1/tmp1 configs/proj1/t1.py --cpu_clock=8GHz --ddr4_2400_16x4 --inorder
mv configs/proj1/tmp1/stats.txt ../PKU-computer-architecture/lab1/res/t1_ddr4_2400_16x4_8GHZ_inorder.txt
