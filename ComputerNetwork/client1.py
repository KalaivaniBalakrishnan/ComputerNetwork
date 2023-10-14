import socket
import json
def send_request(action, data=None):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 9999))
        request_data = {"action": action}
        if data:
            request_data.update(data)
        request_json = json.dumps(request_data)
        client_socket.send(request_json.encode())
        response = client_socket.recv(1024).decode()
        response_data = json.loads(response)
        return response_data
    except ConnectionRefusedError:
        print("Error: The server is not running or is unavailable.")
        return {"error": "Server not available"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}
    finally:
        client_socket.close()
def main():
    while True:
        print("\nTourism Management System Menu:")
        print("1. List Tourist Places")
        print("2. List Guide")
        print("3. Book a Tour")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            response = send_request("get_tourist_places")
            if "tourist_places" in response:
                print("\nTourist Places:")
                for place in response["tourist_places"]:
                    print(f"{place['id']}. {place['name']}: {place['description']}")
            else:
                print(f"Error: {response.get('error', 'Unknown error')}")

        elif choice == "2":
            response = send_request("get_tourists")
            if "tourists" in response:
                print("\nGuides:")
                for tourist in response["tourists"]:
                    print(f"{tourist['id']}. {tourist['name']}")
            else:
                print(f"Error: {response.get('error', 'Unknown error')}")

        elif choice == "3":
            place_id = input("Enter the ID of the tourist place: ")
            tourist_id = input("Enter the ID of the tourist: ")
            guide_id = input("Enter the ID of the guide: ")
            days = input("Enter the number of days for the tour: ")
            amount = input("Enter the booking amount: ")

            data = {
                "place_id": int(place_id),
                "tourist_id": int(tourist_id),
                "guide_id": int(guide_id),
                "days": int(days),
                "amount": float(amount),
            }

            response = send_request("book_tour", data)
            if "message" in response:
                print(response["message"])
            else:
                print(f"Error: {response.get('error', 'Unknown error')}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == '__main__':
    main()
