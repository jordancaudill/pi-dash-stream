from scapy.all import *
import os

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
    print "detected an ARP probe"
      if pkt[ARP].hwsrc == 'a0:02:dc:9b:74:3d':
          print "Connecting to dash button, then running script"
          os.system("sudo moonlight stream 192.168.1.6 -1080 -localaudio")
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=0)
