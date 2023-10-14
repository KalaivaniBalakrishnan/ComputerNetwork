import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class UDPServer {
    private static final int SERVER_PORT = 9999;
    private static final int BUFFER_SIZE = 1024;

    public static void main(String[] args) {
        try (DatagramSocket serverSocket = new DatagramSocket(SERVER_PORT)) {
            System.out.println("UDP server listening on port " + SERVER_PORT + "...");

            while (true) {
                byte[] receiveData = new byte[BUFFER_SIZE];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

                serverSocket.receive(receivePacket);

                String receivedMessage = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Received message: " + receivedMessage);

                String responseMessage = processRequest(receivedMessage);

                byte[] sendData = responseMessage.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(
                    sendData,
                    sendData.length,
                    receivePacket.getAddress(),
                    receivePacket.getPort()
                );

                serverSocket.send(sendPacket);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String processRequest(String request) {
        String[] parts = request.split(",");
        String action = parts[0];

        switch (action) {
            case "GET_PLACES":
                return getTouristPlaces();
            case "GET_TOURISTS":
                return getTourists();
            case "BOOK_TOUR":
                if (parts.length == 6) {
                    int placeId = Integer.parseInt(parts[1]);
                    int touristId = Integer.parseInt(parts[2]);
                    String guideName = parts[3];
                    double amount = Double.parseDouble(parts[4]);
                    int days = Integer.parseInt(parts[5]);

                    return bookTour(placeId, touristId, guideName, amount, days);
                }
                break;
            default:
                return "Unknown action";
        }

        return "Invalid request";
    }

    private static String getTouristPlaces() {
        // Implement logic to retrieve and return a list of tourist places
        return "Tourist Places:\n1. Beach Resort\n2. Mountain Lodge";
    }

    private static String getTourists() {
        // Implement logic to retrieve and return a list of tourists
        return "Tourists:\n1. Alice\n2. Bob\n3. Charlie";
    }

    private static String bookTour(int placeId, int touristId, String guideName, double amount, int days) {
        // Implement logic to book a tour and return a confirmation message
        return "Booking confirmed:\nPlace ID: " + placeId +
               "\nTourist ID: " + touristId +
               "\nGuide: " + guideName +
               "\nAmount: $" + amount +
               "\nDuration: " + days + " days";
    }
}
