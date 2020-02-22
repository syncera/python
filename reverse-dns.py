#1/usr/bin/env python3
# This script is designed to perform a reverse DNS
# lookup on all of the hosts in a specified range.
# sincera

import socket
net = '10.0.12.'
for hst in range(0,256):
    ip= net + str(hst)
    try:
        print(ip, ': ', socket.gethostbyaddr(ip), '\n')
    except:
        print(ip, ': Unknown host\n')
