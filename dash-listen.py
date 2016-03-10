import pexpect
from scapy.all import *

def arp_display(pkt):
  try:
    ingame = game.isalive()
  except NameError:
    ingame = False
  else:
    ingame = True
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == 'a0:02:dc:9b:74:3d':
        if ingame == False:
          print "Connecting to dash button, then running script"
          game = pexpect.spawn('sudo moonlight stream 192.168.1.11 -1080 -localaudio')
          ingame = True
        else:
          print "Closing game"
          game.kill()
          ingame = False
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=0)
