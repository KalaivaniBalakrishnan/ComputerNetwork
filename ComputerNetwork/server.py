import socket

# Define the server's IP address and port
server_ip = "127.0.0.1"  # Use your server's IP address or "0.0.0.0" to listen on all available network interfaces
server_port = 12345  # Choose a port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections (max 5 clients in the queue)
server_socket.listen(5)

print(f"Server is listening on {server_ip}:{server_port}")

while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()

    print(f"Accepted connection from {client_address}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024)

        if not data:
            # No more data from the client, so break the inner loop
            break

        # Echo back the received data to the client
        client_socket.send(data)

    # Close the client socket
    client_socket.close()
