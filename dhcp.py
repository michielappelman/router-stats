#!/usr/bin/python
import xml.etree.ElementTree as ET
import subprocess
from netaddr import *

stats = subprocess.check_output("./get-stats.sh dhcp_clients", shell=True)
root = ET.fromstring(stats)

print "IP \t\tMAC \t\t\tResv \tHostname \tCountdown\tOwner"

for client in root:
    hostname=str(client[2].text)
    if len(hostname) <= 6:
        hostname+="\t"
    mac = EUI(client[1].text)
    oui = mac.oui.registration().org
    seconds = client[3].text
    if len(seconds) <= 6:
        seconds+="\t"
    print client[0].text + " \t" + client[1].text + " \t" + client[4].text + " \t" + hostname + " \t" + seconds  + " \t" + oui 

