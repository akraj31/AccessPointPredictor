import random
import socket
import json
from predictor import predict_proba, predict

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

while True:
    message, address = server_socket.recvfrom(4096)
    print("got message from address", address)
    final = predict_proba(data_sample=json.loads(message.decode()))
    print(final)