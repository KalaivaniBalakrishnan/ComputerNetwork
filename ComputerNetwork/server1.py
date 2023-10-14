import socket
import threading
import json
tourist_places = [
    {"id": 1, "name": "Beach Resort", "description": "A beautiful beachside resort."},
    {"id": 2, "name": "Mountain Lodge", "description": "Cozy lodge in the mountains."},
]
tourists = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]
bookings = []
guides = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Emily"},
]

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    try:
        request_data = json.loads(request)
        response_data = {}

        if "action" in request_data:
            action = request_data["action"]

            if action == "get_tourist_places":
                response_data["tourist_places"] = tourist_places
            elif action == "get_tourists":
                response_data["tourists"] = tourists
            elif action == "book_tour":
                place_id = request_data.get("place_id")
                tourist_id = request_data.get("tourist_id")
                guide_id = request_data.get("guide_id")
                days = request_data.get("days")
                amount = request_data.get("amount")

                if not (place_id and tourist_id and guide_id and days and amount):
                    response_data["error"] = "Missing data"
                else:
                    place = next((p for p in tourist_places if p["id"] == place_id), None)
                    tourist = next((t for t in tourists if t["id"] == tourist_id), None)
                    guide = next((g for g in guides if g["id"] == guide_id), None)

                    if not (place and tourist and guide):
                        response_data["error"] = "Invalid place, tourist, or guide ID"
                    else:
                        booking = {
                            "place": place["name"],
                            "tourist": tourist["name"],
                            "guide": guide["name"],
                            "days": days,
                            "amount": amount,
                        }
                        bookings.append(booking)
                        response_data["message"] = "Booking successful"
            else:
                response_data["error"] = "Unknown action"
        else:
            response_data["error"] = "Action not provided"
    except json.JSONDecodeError:
        response_data = {"error": "Invalid JSON format"}
    response = json.dumps(response_data).encode()
    client_socket.send(response)
    client_socket.close()
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Server is Listening on port 9999...")
    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
if __name__ == '__main__':
    main()
