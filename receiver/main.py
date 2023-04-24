# This program receives data from the unicorn speller trough UDP and sends it to the index.js.
import socket
import requests

UDP_IP = "127.0.0.1" #IP adress that the unicorn speller sends UDP requests to. 
UDP_PORT = 1000 #UDP port that the unicorn speller will send data to.

sock = socket.socket(socket.AF_INET, 
					 socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def req(): #Sends a signal to the index.js file to activate the specific arduino
	if item == "Light1":
		url = 'http://127.0.0.1:3000/l/1'
		r = requests.get(url)

	elif item == "Light2":
		url = 'http://127.0.0.1:3000/l/2'
		r = requests.get(url)

	elif item == "Door":
		url = 'http://127.0.0.1:3000/d'
		r = requests.get(url)

	elif item == "Blind":
		url = 'http://127.0.0.1:3000/b'
		r = requests.get(url)

	else:
		pass
	

while True:
	data, addr = sock.recvfrom(10000)
	#The next five lines search for an identifier that we added to the start and end of each item output of the custom board. More in-depth explanation is located in the README.md
	parse = ("%s" % data)
	n = parse.split("itz_") 
	parse = n[1]
	n = parse.split("_zti")
	item = n[0]
	req()


	
	


