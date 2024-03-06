import socket
import threading

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT_TCP = 5555
SERVER_PORT_UDP = 5556

# Function to handle TCP client connections
def handle_tcp_client(client_socket, address):
    print(f"[TCP] New connection from {address}")

    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"[{address}] {message}")

            # Broadcast message to all clients
            broadcast_tcp(message, client_socket)
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"[TCP] Connection from {address} closed")
    client_socket.close()

# Function to broadcast TCP message to all clients
def broadcast_tcp(message, sender_socket):
    for client in tcp_clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                tcp_clients.remove(client)

# Function to handle UDP client messages
def handle_udp_client():
    while True:
        try:
            # Receive message from client
            message, address = udp_socket.recvfrom(1024)
            print(f"[UDP] {address}: {message.decode()}")

            # Broadcast message to all clients
            broadcast_udp(message, address)
        except Exception as e:
            print(f"Error: {e}")

# Function to broadcast UDP message to all clients
def broadcast_udp(message, sender_address):
    for address in udp_clients:
        if address != sender_address:
            try:
                udp_socket.sendto(message, address)
            except:
                udp_clients.remove(address)

# TCP server initialization
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((SERVER_HOST, SERVER_PORT_TCP))
tcp_server.listen(5)
print(f"[TCP] Server started on {SERVER_HOST}:{SERVER_PORT_TCP}")

# UDP server initialization
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((SERVER_HOST, SERVER_PORT_UDP))
print(f"[UDP] Server started on {SERVER_HOST}:{SERVER_PORT_UDP}")

# Lists to keep track of clients
tcp_clients = []
udp_clients = []

# Start UDP client handler thread
udp_thread = threading.Thread(target=handle_udp_client)
udp_thread.start()

try:
    while True:
        # Accept new TCP client connections
        client_socket, address = tcp_server.accept()
        tcp_clients.append(client_socket)

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_tcp_client, args=(client_socket, address))
        client_thread.start()

        # Add UDP client to the list
        udp_clients.append(address)
finally:
    # Close all sockets
    tcp_server.close()
    udp_socket.close()
