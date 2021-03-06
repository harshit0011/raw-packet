#!/usr/bin/env python

# region Import
from json import dumps
from sys import path
from os.path import dirname, abspath
project_root_path = dirname(dirname(dirname(abspath(__file__))))
utils_path = project_root_path + "/Utils/"
path.append(utils_path)

from base import Base
from network import Sniff_raw

Base = Base()
# endregion


# region Print packet function
def print_packet(request):
    global Base

    print("\n")

    if 'ARP' in request.keys():
        Base.print_info("ARP packet from: ", request['Ethernet']['source'])

    if 'ICMPv6' in request.keys():
        Base.print_info("ICMPv6 packet from: ", request['Ethernet']['source'])

    if 'DNS' in request.keys():
        Base.print_info("DNS packet from: ", request['Ethernet']['source'])

    if 'DHCP' in request.keys():
        Base.print_info("DHCP packet from: ", request['Ethernet']['source'])

    if 'DHCPv6' in request.keys():
        Base.print_info("DHCPv6 packet from: ", request['Ethernet']['source'])

    print(dumps(request, indent=4))

# endregion


# region Main function
if __name__ == "__main__":

    # region Print info message
    Base.print_info("Available protocols: ", "Ethernet ARP IP IPv6 ICMPv6 UDP DNS DHCP DHCPv6")
    Base.print_info("Start test sniffing ...")
    # endregion

    # region Start sniffer
    sniff = Sniff_raw()
    sniff.start(protocols=['ARP', 'IP', 'IPv6', 'ICMPv6', 'UDP', 'DNS', 'DHCP', 'DHCPv6'], prn=print_packet)
    # endregion

# endregion
