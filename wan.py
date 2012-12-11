#!/usr/bin/python
import xml.etree.ElementTree as ET
import subprocess
import sys

stats = subprocess.check_output("./get-stats.sh wan_connection_status", shell=True)
root = ET.fromstring(stats)

sys.stdout.write(root[1][3].text)
