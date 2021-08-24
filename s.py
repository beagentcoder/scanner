#!/bin/bash
import sys
import socket
from datetime import datetime 

#define the target
if len(sys.argv) ==2:
	target=socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid Amount of arguments.")
	print("Syntax:python3 scanner.py <ip>")

#add a banner
print("-" * 50)
print("Time started:"+ str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port)) #returns an error indicator
		if result==0:
			print("port {} is open ".format(port))
		s.close()
except KeyboardInterrupt:
	print ("\nExiting program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()	
except socket.error:
	print("couldn't connect to server")
	sys.exit()
	
