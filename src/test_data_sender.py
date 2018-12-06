import time
from socket import *
from data import get_sample
import json

#Send ping 10 times 
while True:  

    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #Set a timeout value of 1 second
    clientSocket.settimeout(1)

    #Ping to server
    message = json.dumps(get_sample()).encode()

    addr = ("172.24.27.70", 12000)

    #Send ping
    start = time.time()
    clientSocket.sendto(message, addr)

    time.sleep(1)