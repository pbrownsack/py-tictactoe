import sys
from socket import *

# Check command args
if len(sys.argv) < 3:
    print("usage: python client.py host port")
    exit(1)



# Setup client socket
s = socket(AF_INET, SOCK_STREAM)

ip_addr = sys.argv[1]
port = int(sys.argv[2])

s.connect((ip_addr, port))

data = s.recv(1024)
print(data.decode())

s.close()
