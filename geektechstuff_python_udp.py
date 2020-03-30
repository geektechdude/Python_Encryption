# geektechstuff

# imports socket library
import socket

def udp_server():
    # creates a UDP socket
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # binds the socket to IP address and port
    udp_server.bind(("0.0.0.0", 8899))
    # used to receive data
    data, client_address = udp_server.recvfrom(1024)
    # prints received data
    print(data,client_address)
    message = "Thanks for connecting"
    # encodes message
    data = message.encode()
    # sends data
    udp_server.sendto(data, client_address)
    

def udp_client():
    # creates a UDP socket
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # binds the socket to IP address and port
    udp_client.connect(("127.0.0.1", 8899))
    message = "Hello, I have connected"
    data = message.encode()
    udp_client.send(data)
    # used to receive data
    data, client_address = udp_client.recvfrom(1024)
     # prints received data
    print(data,client_address)   

udp_server()