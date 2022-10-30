import m5
from m5.objects import *

class L1Cache(Cache):
	size = '32kB'
	assoc = 2
	tag_latency = 2
	data_latency = 2
	response_latency = 2
	mshrs = 4
	tgts_per_mshr = 20
	
	def __init__(self):
		super(L1Cache, self).__init__()

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

root.system.l1cache = L1Cache()
root.system.l2cache = L2Cache()
root.system.l1bus = L2XBar()

root.system.l1bus.cpu_side_ports = root.system.cpu.icache_port
root.system.l1bus.cpu_side_ports = root.system.cpu.dcache_port

root.system.l1bus.mem_side_ports = root.system.l1cache.cpu_side
root.system.l1cache.mem_side = root.system.l2cache.cpu_side
root.system.l2cache.mem_side = root.system.membus.cpu_side_ports

root.system.mem_ctrl.port = root.system.membus.mem_side_ports
root.system.cpu.createInterruptController()
root.system.system_port = root.system.membus.cpu_side_ports
# root.system.cpu.interrupts[0].pio = system.membus.mem_side_ports
# root.system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
# root.system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

exe_path = 'tests/test-progs/hello/bin/arm/linux/hello'
root.system.workload = SEWorkload.init_compatible(exe_path)
process = Process()
process.cmd = [exe_path]
root.system.cpu.workload = process
root.system.cpu.createThreads()

m5.instantiate()
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))

