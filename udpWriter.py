#
# udpWriter.py
#
# use: udpSocketWriter.py [port [ip_address]]
# port default is 59330
# ip_address default is local network broadcast address,
#  from 'ifconfig |grep cast'
#

from socket import *
import sys
import os
import re

# default ip set to broadcast address
# ip = '192.168.1.255'
f = os.popen( 'ifconfig |grep "cast"')
a = f.read()
a = re.search( 'cast[:\s](\d+\.\d+\.\d+\.\d+)', a)
ip = a.group(1)

port = 59330

# user-supplied ip and port
if len(sys.argv) >= 2:
  port = sys.argv[1]
  if len(sys.argv) >= 3:
    ip = sys.argv[2]
print( "Writing to %s:%s" % ( ip, port))

s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
#s.sendto( 'this is testing', ( '255.255.255.255', 8888))
s.sendto( 'this is testing', ( ip, port))
