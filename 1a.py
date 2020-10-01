from jnpr.junos import Device
from pprint import pprint

srx2 = Device(
    host = "srx2.lasthop.io",
    user = "pyclass",
    password = "PASSWORD"
)

srx2.open()

#pprint(srx2.facts)

pprint((srx2.facts)["hostname"]
)
