# This script sends a command to control a Yamaha audio mixing console
# Please execute this scrupt like this:
# "python command.py ssrecall_ex MIXER:Lib/Scene 1"
# It will recall scene #001 of the target console

import sys
import socket
import time

# Host is console's IP
host ="192.168.0.128"
# Port must be 49280
port =49280

# create command
args = sys.argv
args.pop(0)



    

# connect socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
s.connect((host,port))


for i in range(25):
    command = 'set MIXER:Current/InCh/Fader/On {} 0 1'.format(i)
    command += '\n'
    command += 'set MIXER:Current/InCh/Fader/On {} 0 0'.format(i-1)
    command += '\n'
    s.sendall(command.encode())
    time.sleep(0.1)

# receive a message before closing socket
s.recv(1500)

# close socket
s.close ()
