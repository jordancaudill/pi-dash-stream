import pexpect
from scapy.all import *
Boolean ingame
ingame = true
def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == 'a0:02:dc:9b:74:3d':
        if inGame == false;
          print "Connecting to dash button, then running script"
          game = pexpect.spawn('sudo moonlight stream 192.168.1.11 -1080 -localaudio')
          inGame = true
        else:
          print "Closing game"
          game.kill()
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=0)
