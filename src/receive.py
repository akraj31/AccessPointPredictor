import random
import socket
import json
from predictor import predict_proba, predict, locations

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

user_db = dict()
access_points = dict()
ap_states = dict()

for val in locations():
	ap_states[val] = False

while True:
    message, address = server_socket.recvfrom(4096)
    address = address[0]
    print("Received data from Mobile User ", address)
    final = predict_proba(data_sample=json.loads(message.decode()))

    print("Prediction for ",address, " is ", final)
    if address not in user_db:
    	user_db[address] = True
    
    done = False
    for ap in access_points:
    	if address in access_points[ap]:
    		print("change")
    		done = True
    		del access_points[ap][address]
    		if final not in access_points:
    			access_points[final] = {address:True}
    		else:
    			access_points[final][address] = True
    		break
    if not done:
    	access_points[final] = {address:True}
    
    for k,v in access_points.items():
    	ap_states[k] = not not v
    print(access_points)
    
    print("State of Access Points")
    for state in ap_states:
    	print(state," : ", "On" if ap_states[state] else "Off")