import random
import socket
import json
from predictor import predict_proba, predict

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

while True:
    message, address = server_socket.recvfrom(1024)
    print("got message from address", address)
    #predict(data_sample=json.loads(message))
    #predict_proba(data_sample=json.loads(message))
    #server_socket.sendto(results, address)