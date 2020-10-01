from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.routes import RouteTable
from jnpr_devices import srx2
from jnpr_func import check_connected,gather_routes

srx2_dev = Device(**srx2)
srx2_dev.open()

route_t = gather_routes(srx2_dev)
print("Route table before change:")
print(route_t.keys())

srx2_cfg = Config(srx2_dev)

srx2_cfg.lock()

srx2_cfg.load(path="set_juniper.conf", format="text", merge=True)

print("Config diff:")
print(srx2_cfg.diff())

srx2_cfg.commit()
print("Change committed")

print("Route table after change:")
print(route_t.keys())

srx2_cfg.load(path="del_juniper.conf", format="set", merge=True)

print("Config diff:")
print(srx2_cfg.diff())

srx2_cfg.commit()

print("Route table change reverted:")
print(route_t.keys())

srx2_cfg.unlock()

srx2_dev.close()

