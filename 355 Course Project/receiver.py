#receiver.py
import os
import socket


phrase = "" #initialize a phrase to be receieved
sock = socket.socket() #initialize a socket value
endflag = 0
def sooket():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #print("this is the socket value")
    #print(sock)
    return

def extract():
    global phrase
    global sock
    global endflag
    #i = 0 #debug
    data = '1'; #debug
    # UDP Server Listener
    #print ("READY")
    data, addr = sock.recvfrom(1)
    #print ("data receieved")
    #print(data[0])
    print("")
    #phrase += chr(data[0])
    
    
    #while True:
    # Receive 1 byte string (character)
    #data, addr = sock.recvfrom(1)
    #i += 1 #debug
    if chr(data[0]) == '0':
        endflag = 1
    else:
        #phrase += str(i) #debug
        phrase += chr(data[0])
    
    return
    
def softbind():
    global sock
    # UDP Server Info
    UDP_IP = 	"127.0.0.1" #ip of computer
    UDP_PORT = 20001
    #bind()
    sock.bind((UDP_IP, UDP_PORT))
    print("connected")
    print ("READY")
    return

def deliver_data():
    #deliver_data()
    global phrase 
    #print("printing")
    print(phrase)
    return
    
def rdt_recv():
    extract()
    deliver_data()
    return


sooket()
softbind()
while True:
    rdt_recv()
    if endflag == 1:
        break;
print("END")