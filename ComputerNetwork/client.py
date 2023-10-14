import socket
# Define the server's IP address and port
server_ip = "127.0.0.1"  # Change this to the IP address of your server
server_port = 12345  # Use the same port number as your server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((server_ip, server_port))

    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")

        if message.lower() == "exit":
            break

        # Send the message to the server
        client_socket.send(message.encode())

        # Receive and print the server's response
        response = client_socket.recv(1024)
        print(f"Server says: {response.decode()}")

except ConnectionRefusedError:
    print("Connection to the server failed. Make sure the server is running.")

finally:
    # Close the client socket
    client_socket.close()
