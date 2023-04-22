import socket
import requests

UDP_IP = "127.0.0.1"
UDP_PORT = 1000

sock = socket.socket(socket.AF_INET, # Internet
					 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

changed = " "

def req():
	item = parse()
	url = 'http://127.0.0.1/item'

	r = requests.post(url, json={"Item": item})

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
	
	


