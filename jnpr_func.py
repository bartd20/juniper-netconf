from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable

def check_connected(device):
    return device.connected
 
def gather_arp_table(device):
    return ArpTable(device).get()

def gather_routes(device):
    return RouteTable(device).get()
