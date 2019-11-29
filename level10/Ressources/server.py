#! /usr/bin/python3

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.1.22", 6969)
print("starting up on %s port %s" % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
	print("waiting for a connection")
	connection, client_address = sock.accept()
	print("connection from", client_address)
	while True:
		data = connection.recv(64)
		print('received "%s"' % data)
		if len(data) < 1:
			connection.close()
			break
	break
