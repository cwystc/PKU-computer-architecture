import m5
from m5.objects import *

class L1DCache(Cache):
	size = '32kB'
	assoc = 2
	tag_latency = 2
	data_latency = 2
	response_latency = 2
	mshrs = 4
	tgts_per_mshr = 20
	
	def __init__(self):
		super(L1DCache, self).__init__()

class L1ICache(Cache):
	size = '32kB'
	assoc = 2
	tag_latency = 2
	data_latency = 2
	response_latency = 2
	mshrs = 4
	tgts_per_mshr = 20
	
	def __init__(self):
		super(L1ICache, self).__init__()

class L2Cache(Cache):
	size = '256kB'
	assoc = 8
	tag_latency = 20
	data_latency = 20
	response_latency = 20
	mshrs = 20
	tgts_per_mshr = 12
	def __init__(self):
		super(L2Cache, self).__init__()


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
parser.add_option('--Random', action="store_true")
parser.add_option('--LRU', action="store_true")
parser.add_option('--MRU', action="store_true")
parser.add_option('--MyMRU', action="store_true")
parser.add_option('--Clock', action="store_true")
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

root.system.cpu = TimingSimpleCPU()

root.system.membus = SystemXBar()

root.system.cpu.icache = L1ICache()
root.system.cpu.dcache = L1DCache()
root.system.l2cache = L2Cache()

if (options.Random):
	root.system.cpu.icache.replacement_policy = RandomRP()
	root.system.cpu.dcache.replacement_policy = RandomRP()
	root.system.l2cache.replacement_policy = RandomRP()
elif (options.LRU):
	root.system.cpu.icache.replacement_policy = LRURP()
	root.system.cpu.dcache.replacement_policy = LRURP()
	root.system.l2cache.replacement_policy = LRURP()
elif (options.MRU):
	root.system.cpu.icache.replacement_policy = MRURP()
	root.system.cpu.dcache.replacement_policy = MRURP()
	root.system.l2cache.replacement_policy = MRURP()
elif (options.MyMRU):
	root.system.cpu.icache.replacement_policy = MyMRURP()
	root.system.cpu.dcache.replacement_policy = MyMRURP()
	root.system.l2cache.replacement_policy = MyMRURP()
elif (options.Clock):
	root.system.cpu.icache.replacement_policy = ClockRP()
	root.system.cpu.dcache.replacement_policy = ClockRP()
	root.system.l2cache.replacement_policy = ClockRP()

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
process.cmd = ['test_bench/mcf/mcf_base.amd64-m64-gcc42-nn','test_bench/mcf/inp.in']

exe_path = process.cmd[0]
root.system.workload = SEWorkload.init_compatible(exe_path)

root.system.cpu.workload = process
root.system.cpu.createThreads()

m5.instantiate()
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))

