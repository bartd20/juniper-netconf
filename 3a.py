from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
from jnpr_devices import srx2
from jnpr_func import check_connected

srx2_dev = Device(**srx2)
srx2_dev.open()

srx2_cfg = Config(srx2_dev)

srx2_cfg.lock()

srx2_cfg.load("set interfaces fe-0/0/1 description pyclass-student-was-here", format="set", merge=True)

print("Config diff:")
print(srx2_cfg.diff())

srx2_cfg.commit()
print("Change committed")

srx2_cfg.load("delete interfaces fe-0/0/1 description pyclass-student-was-here", format="set", merge=True)

print("Config diff:")
print(srx2_cfg.diff())

srx2_cfg.commit()

srx2_cfg.unlock()

