from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
from pprint import pprint
from jnpr_devices import srx2

def check_connected(device):
    return device.connected

def gather_arp_table(device):
    return ArpTable(device).get()

def gather_routes(device):
    return RouteTable(device).get()

def print_output(device,rt_table,arp_table):
    print("Hostname:")
    print(device.facts["hostname"])
    print("NETCONF port:")
    print(device.port)
    print("Username:")
    print(device.user)
    print(rt_table.keys())
    print(arp_table.keys())

srx2_dev = Device(**srx2)
srx2_dev.open()

route_t = gather_routes(srx2_dev)
arp_t = gather_arp_table(srx2_dev)

print_output(srx2_dev,route_t,arp_t)

