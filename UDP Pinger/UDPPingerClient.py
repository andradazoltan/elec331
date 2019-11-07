from socket import * 
import time

# Create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set a timeout for the client of 1s
clientSocket.settimeout(1) 

for iter in range(10):
	start = time.time() 

	clientSocket.sendto("ping".encode(), ('localhost', 12000))

	try:
		message, address = clientSocket.recvfrom(1024)
		rtt = (time.time() - start) 

		print(message)
		print(rtt)

	except timeout: 
		print("Request timed out")
		continue

clientSocket.close()