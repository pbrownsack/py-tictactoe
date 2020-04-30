import sys
from socket import *

def cli_send(client, data):
    if client == clients[1]:
        print("X >", data)
    elif client == clients[2]:
        print("O >", data)
    client.sendall(str(data).encode())

def send_all(clients, data):
    cli_send(clients[1], data)
    cli_send(clients[2], data)

def recv_msg():
    pass

# Setup default board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Check if port was passed as arg
if len(sys.argv) != 2:
    print("usage: python server.py port")
    exit(1)

print("Networking server starting...")
print("Waiting on clients...")

# Setup server socket
s = socket(AF_INET, SOCK_STREAM)
s.bind(("", int(sys.argv[1])))
s.listen(5)

# Wait for both clients to connect
client1, addr1 = s.accept()
client2, addr2 = s.accept()
clients = [s, client1, client2]

send_all(clients, "All clients connected")

# Close out client connections
client1.close()
client2.close()

# Close out the socket, we're done boys
s.close()