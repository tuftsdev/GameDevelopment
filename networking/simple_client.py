import socket

s = socket.socket()
host = socket.gethostname()
port = 15050

s.connect((host, port))

# Get data from server
print s.recv(4096)
s.close
