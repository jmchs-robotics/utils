#
# udpSocketListener.py
#
# use: udpSocketListener.py [port [ip_address]]
# port default is 59330
# ip_address default is local network broadcast address,
#  from 'ifconfig |grep cast'
#

import socket
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
print( "Listening to %s:%s" % ( ip, port))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(( ip, port))
ts_100 = -2
ts_last = -1
ts = 0
i = 0
while 1:
    data, addr = s.recvfrom(1024)
    print data
    m = re.search( "(\d+)", data)
    if( m):
      ts = int( m.group(1))
      if ts < ts_last:
        print 'hiccup'
      if ts != ts_last:
        print data + ' frame rate ' + str( 1e9 / (ts - ts_last))
      ts_last = ts
      i += 1
      if( i >= 100):
        i = 0
        print 'Ave frame rate, last 100 frames: ' + str( 1e11 / (ts - ts_100))
        ts_100 = ts

