#!/usr/bin/python
"""
This is the script that will eventually walk over the XML stats and 
put the data in Graphite.
"""

import xml.etree.ElementTree as ET
import subprocess
import time
from socket import socket 

CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003

stats = subprocess.check_output("./get-stats.sh interface_stats", shell=True)
root = ET.fromstring(stats)
now = str( time.time())

lines = []

interface = 0
while interface <= 2:
    stat=2
    if interface == 2:
        last = 6
    else:
        last = 7
    while stat <= last:
        lines.append("router." + root[interface][1].text.lower() + "." + root[interface][stat].tag + " " + root[interface][stat].text + " " + now )
        stat += 1
    interface += 1
message = '\n'.join(lines) + '\n'

sock = socket()
try:
    sock.connect( (CARBON_SERVER,CARBON_PORT) )
except:
    print "Couldn't connect to %(server)s on port %(port)d, is carbon-agent.py running?" % { 'server':CARBON_SERVER, 'port':CARBON_PORT }
    sys.exit(1)

sock.sendall(message)

