import m5
from new_cache import *

from optparse import OptionParser
parser = OptionParser()
parser.add_option('--o3', action="store_true")
parser.add_option('--inorder', action="store_true")
parser.add_option('--cpu_clock', type="string", default="2GHz")
parser.add_option('--ddr3_1600_8x8', action="store_true")
parser.add_option('--ddr3_2133_8x8', action="store_true")
parser.add_option('--ddr4_2400_16x4', action="store_true")
parser.add_option('--ddr4_2400_8x8', action="store_true")
parser.add_option('--lpddr2_s4_1066_1x32', action="store_true")
parser.add_option('--wideio_200_1x128', action="store_true")
parser.add_option('--lpddr3_1600_1x32', action="store_true")


parser.add_option('--mysimple', action="store_true")
parser.add_option('--local', action="store_true")
parser.add_option("--tournament", action="store_true")
parser.add_option('--bimode', action="store_true")
parser.add_option('--btbentry', type="int", default=4096)
parser.add_option('--ras', type="int", default=16)
parser.add_option('--localsize', type="int", default=2048)
parser.add_option('--localhissize', type="int", default=2048)
parser.add_option('--globalsize', type="int", default=8192)
parser.add_option('--choicesize', type="int", default=8192)
(options, args) = parser.parse_args()

root = Root()
root.full_system = False
root.system = System()

root.system.clk_domain = SrcClockDomain()
root.system.clk_domain.clock = '2GHz'
root.system.clk_domain.voltage_domain = VoltageDomain()

root.system.mem_mode = 'timing'
root.system.mem_ranges = [AddrRange ('2GB')]
root.system.mem_ctrl = MemCtrl()
root.system.mem_ctrl.dram = DDR4_2400_16x4 ()
root.system.mem_ctrl.dram.range = root.system.mem_ranges[0]

root.system.cpu = DerivO3CPU()

root.system.membus = SystemXBar()

root.system.cpu.icache = L1ICache()
root.system.cpu.dcache = L1DCache()
root.system.l2cache = L2Cache()

########################### add branch predictor ###########################
if options.mysimple:
	root.system.cpu.branchPred = MySimpleBP()
elif options.local:
	root.system.cpu.branchPred = LocalBP()
elif options.tournament:
	root.system.cpu.branchPred = TournamentBP()
elif options.bimode:
	root.system.cpu.branchPred = BiModeBP()
else:
	root.system.cpu.branchPred = TournamentBP()
root.system.cpu.branchPred.BTBEntries = options.btbentry
root.system.cpu.branchPred.RASSize = options.ras

if options.local:
	root.system.cpu.branchPred.localPredictorSize = options.localsize
elif options.tournament:
	root.system.cpu.branchPred.localPredictorSize = options.localsize
	root.system.cpu.branchPred.localHistoryTableSize = options.localhissize
	root.system.cpu.branchPred.globalPredictorSize = options.globalsize
	root.system.cpu.branchPred.choicePredictorSize = options.choicesize
elif options.bimode:
	root.system.cpu.branchPred.globalPredictorSize = options.globalsize
	root.system.cpu.branchPred.choicePredictorSize = options.choicesize
########################### add branch predictor ###########################



#root.system.cpu.icache_port = root.system.membus.cpu_side_ports
#root.system.cpu.dcache_port = root.system.membus.cpu_side_ports
root.system.cpu.icache.cpu_side = root.system.cpu.icache_port
root.system.cpu.dcache.cpu_side = root.system.cpu.dcache_port

root.system.l2bus = L2XBar()
root.system.cpu.icache.mem_side = root.system.l2bus.cpu_side_ports
root.system.cpu.dcache.mem_side = root.system.l2bus.cpu_side_ports
root.system.l2cache.cpu_side = root.system.l2bus.mem_side_ports
root.system.l2cache.mem_side = root.system.membus.cpu_side_ports

root.system.mem_ctrl.port = root.system.membus.mem_side_ports
root.system.cpu.createInterruptController()
root.system.system_port = root.system.membus.cpu_side_ports
# root.system.cpu.interrupts[0].pio = system.membus.mem_side_ports
# root.system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
# root.system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

root.system.cpu.max_insts_any_thread = 1000000000

process = Process()
process.cmd = ['test_bench/BFS/bfs','-f','test_bench/BFS/USA-road-d.NY.gr']

exe_path = process.cmd[0]
root.system.workload = SEWorkload.init_compatible(exe_path)

root.system.cpu.workload = process
root.system.cpu.createThreads()

m5.instantiate()
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))

