#! /usr/bin/

from scapy.all import *

if len(sys.argv) != 3:
    print ("Utilizando: Python sniff_scapy.py")
    exit()

a = sniff(count = 10)
print(a.nsummary())