import socket
SERVER_IP = "127.0.0.1"  # Replace with the server's IP address
SERVER_PORT = 9999
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        print("Tourism Management System Menu:")
        print("1. List Tourist Places")
        print("2. List Tourists")
        print("3. Book a Tour")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            send_request(client_socket, "GET_PLACES")
        elif choice == "2":
            send_request(client_socket, "GET_TOURISTS")
        elif choice == "3":
            place_id = input("Enter Place ID: ")
            tourist_id = input("Enter Tourist ID: ")
            guide_name = input("Enter Guide Name: ")
            amount = input("Enter Amount: ")
            days = input("Enter Number of Days: ")

            request_message = f"BOOK_TOUR,{place_id},{tourist_id},{guide_name},{amount},{days}"
            send_request(client_socket, request_message)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    client_socket.close()

def send_request(client_socket, message):
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    response, server_address = client_socket.recvfrom(1024)
    print("\nServer Response:\n" + response.decode())

if __name__ == "__main__":
    main()
