#! /usr/bin

 # Establecer el nviel de Log 
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) 
from scapy.all import *

# Revisar si existe un error
if len(sys.argv) != 3:
    print ("Utilizando: Python connect_scan.py")
    exit()

src_port = RandShort()
dst_port = 22
dst_ip   = sys.argv[1]
ports    = sys.argv[2]

# Evaluación de 
ports.replace(" ","")
scanPorts = ports.strip().split(':')
for port in scanPorts:
    response = sr1(IP(dst = dst_ip) / TCP(sport = src_port, dport = int(port), flags="S"))
    if (str(type(response))) == "<type 'NoeType'>":
        print (port+": Puerto Cerrado")
    elif (response.haslayer(TCP)):
        if (response.getlayer(TCP).flags == 0x12):
            send_rst = sr1(IP(dst = dst_ip) / TCP (sport = src_port, dport = int(port), flags="AR"))
            print (port+": Puerto Abierto")
    elif (response.getlayer(TCP).flags == 0x14):
        print (port+": Puerto Cerrado")

