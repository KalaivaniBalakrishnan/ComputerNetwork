import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

# Sample data (replace with your data storage or database)
tourist_places = {
    1: "Beach Resort: A beautiful beachside resort.",
    2: "Mountain Lodge: Cozy lodge in the mountains."
}

tourists = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))

    print("UDP server listening on port", SERVER_PORT)

    while True:
        data, client_address = server_socket.recvfrom(1024)
        request = data.decode()
        print("Received request:", request)

        response = process_request(request)
        server_socket.sendto(response.encode(), client_address)

def process_request(request):
    parts = request.split(',')
    action = parts[0]

    if action == "GET_PLACES":
        return get_tourist_places()
    elif action == "GET_TOURISTS":
        return get_tourists()
    elif action == "BOOK_TOUR" and len(parts) == 6:
        place_id, tourist_id, guide_name, amount, days = parts[1:]
        return book_tour(place_id, tourist_id, guide_name, amount, days)
    else:
        return "Invalid request"

def get_tourist_places():
    response = "Tourist Places:"
    for place_id, description in tourist_places.items():
        response += f"\nID: {place_id}, Description: {description}"
    return response

def get_tourists():
    response = "Tourists:"
    for tourist_id, name in tourists.items():
        response += f"\nID: {tourist_id}, Name: {name}"
    return response

def book_tour(place_id, tourist_id, guide_name, amount, days):
    return f"Booking confirmed:\nPlace ID: {place_id}\nTourist ID: {tourist_id}\nGuide: {guide_name}\nAmount: {amount}\nDuration: {days} days"

if __name__ == "__main__":
    main()
