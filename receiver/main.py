import socket
import requests

UDP_IP = "127.0.0.1"
UDP_PORT = 1000

sock = socket.socket(socket.AF_INET, # Internet
					 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def req():
	if item == "Light1":
		url = 'http://127.0.0.1:3000/l/1'
		r = requests.get(url)
		 
		print("Light1")

	elif item == "Light2":
		url = 'http://127.0.0.1:3000/l/2'
		r = requests.get(url)
		 
		print("Light2")
	elif item == "Door":
		url = 'http://127.0.0.1:3000/d'
		r = requests.get(url)
		print("Door")
	elif item == "Blind":
		url = 'http://127.0.0.1:3000/b'
		r = requests.get(url)
		 
		print("blind")
	else:
		pass
	

while True:
	data, addr = sock.recvfrom(10000)
	parse = ("%s" % data)
	n = parse.split("itz_") 
	parse = n[1]
	n = parse.split("_zti")
	item = n[0]
	print(item)
	req()


	
	


