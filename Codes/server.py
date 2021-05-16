from socket import *
def createServer():
	# Create a server socket, meaning it's creating an endpoint.
	# It is making the phone, it is up to us later whether we want to receive or make phone calls
	serversocket = socket(AF_INET, SOCK_STREAM)
	try:
		# We're saying that this server is willing to receive phone calls on port 9000
		serversocket.bind(('localhost', 9000))
		# Listening for incoming requests. 5 means that if server is busy handling 1 request, 
		# the OS should queue up to 4 additional requests for it to server when it gets back
		serversocket.listen(5)
		while(1):
			(clientsocket, address) = serversocket.accept()
			# Read the data, 5000 characters and decode utf-8 into unicode
			rd = clientsocket.recv(5000).decode()
			# Split by new line
			pieces = rd.split("\n")
			if len(pieces) > 0:
				[print(piece) for piece in pieces]
			data = "HTTP/1.1 200 OK\r\n"
			data += "Content-Type: text/html; charset=utf-8\r\n"
			data += "\r\n"
			data += "<html><body>Hello World</body></html>\r\n\r\n"
			clientsocket.sendall(data.encode())
			clientsocket.shutdown(SHUT_WR)
	# Exit on Ctrl + C in terminal/cmd
	except KeyboardInterrupt:
		print("Shutting down...\n")
	except Exception as exc:
		print("Error:\n", exc)
	# Hang up the call
	serversocket.close()

createServer()
