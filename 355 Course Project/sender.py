#sender.py

import os
import socket
import time
from array import *


sock = socket.socket()  #initialize a socket value
#packet initialization
phrase = "This is a test"
packet='a'
packetctr=0
length = len(phrase)

def sooket():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    return
    
def make_pkt():
    global packet
    global phrase
    global packetctr
    packet=phrase[packetctr]
    packetctr+=1
    #packet=phrase[i]
    return

def udt_send():
    global sock
    global packetctr
    global length
    # UDP Server Info
    UDP_IP = "127.0.0.1" #ip of computer
    UDP_PORT = 20001
    
    sock.sendto(str.encode(packet), (UDP_IP,UDP_PORT))
    if packetctr == length:
        sock.sendto(str.encode('0'), (UDP_IP,UDP_PORT))   
    return
    print("message sent")

def rtd_send():
    make_pkt()
    udt_send()
    return
    
def wait():
    print("wait one second")
    time.sleep(1)
    return
#    
sooket()

while True:
    rtd_send()
    wait()
    if packetctr == length:
        break
sock.close()

'''
# UDP Server Info
UDP_IP = "127.0.0.1" #ip of computer
UDP_PORT = 20001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

foo = "g"
phrase = "This is a test"
packet='a'
packetctr=0
ex = '0'
length = len(phrase)

for i in range(length):
    sock.sendto(str.encode(phrase[i]), (UDP_IP,UDP_PORT))
    

#sock.sendto(str.encode(foo), (UDP_IP,UDP_PORT))
#print("foo sent!")
sock.sendto(str.encode(ex), (UDP_IP,UDP_PORT))
print("ex sent!")
sock.close()
'''


