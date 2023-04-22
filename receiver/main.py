import socket
import requests

UDP_IP = "127.0.0.1"
UDP_PORT = 1000

sock = socket.socket(socket.AF_INET, # Internet
					 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

changed = " "

def req():
	if item == "LightOn":
		url = 'http://127.0.0.1/LightOn1'
		r = requests.post(url, json={"Requested": True})
		print(r.json())
	elif item == "LightOff":
		url = 'http://127.0.0.1/LightOff1'
		r = requests.post(url, json={"Requested": True})
		print(r.json())
	elif item == "LightOn2":
		url = 'http://127.0.0.1/LightOn2'
		r = requests.post(url, json={"Requested": True})
		print(r.json())
	elif item == "LightOff2":
		url = 'http://127.0.0.1/LightOff2'
		r = requests.post(url, json={"Requested": True})
		print(r.json())
	elif item == "DoorOpen":
		url = 'http://127.0.0.1/DoorOpen'
		r = requests.post(url, json={"Requested": True})
		print(r.json())
	elif item == "DoorClose":
		url = 'http://127.0.0.1/DoorClose'
		r = requests.post(url, json={"Requested": True})
		print(r.json())
	elif item == "BlindUP":
		url = 'http://127.0.0.1/BlindsUP'
		r = requests.post(url, json={"Requested": True})
		print(r.json())
	elif item == "BlindsDown":
		url = 'http://127.0.0.1/BlindsDown'
		r = requests.post(url, json={"Requested": True})
		print(r.json())
	

while True:
	data, addr = sock.recvfrom(1024)
	parse = ("%s" % data)
	n = parse.split("\\x06")
	parse = n[2]
	n = parse.split("\\t")
	item = n[0]
	if item == changed:
		req()
	else:
		print("No changes")
	changed = item 


	
	


