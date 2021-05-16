import socket
# Make a call
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Dial this number, meaning try to connect to this server, on port number 9000
mysock.connect(('localhost', 9000))
# Try to fetch the following page,
# if you have headers they will go after \r\n
# Also, encode is used because string in Pyhton are unicode and we need to convert
# that into UTF-8 using .encode() method
cmd = 'GET'.encode()

# We are the browser in this case so, we talk first before we get a response
mysock.send(cmd)

while True:
	# Get 512 characters in one go
	data = mysock.recv(512)
	# If we get no data, meaning socket was closed by the remote server
	# So, the length of data returned will be 0
	if len(data) < 1:
		break
	# Data returned is UTF-8 again, so we decode it to unicode which print() function wants
	print(data.decode(), end='')


# Response ends
# Hang up the phone, meaning disconnect from the server
mysock.close()

 
