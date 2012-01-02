import socket

# Create socket object
s = socket.socket()

# Create host and port
host = socket.gethostname()
port = 15050 # Give this a port number of your own

# Bind to socket
s.bind((host, port))

s.listen(5)
print "Starting server " + host + " on port " + str(port)

# Wait for connection
while True:
	connection, address = s.accept()
	print "Connection from " + str(address)
	connection.send("You successfully connected to me!")
	connection.close()
