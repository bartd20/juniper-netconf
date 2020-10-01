from jnpr.junos import Device
from jnpr_devices import srx2
from lxml import etree
from pprint import pprint

srx2_dev = Device(**srx2)
srx2_dev.open(normalize=True)

xml_out = srx2_dev.rpc.get_software_information()
print(etree.tostring(xml_out,pretty_print=True).decode())
print("-----------------------")

xml_out = srx2_dev.rpc.get_interface_information(terse=True)
print(etree.tostring(xml_out,pretty_print=True).decode())
print("-----------------------")

xml_out = srx2_dev.rpc.get_interface_information(terse=True,interface_name="fe-0/0/7")
print(etree.tostring(xml_out,pretty_print=True).decode())

srx2_dev.close()

