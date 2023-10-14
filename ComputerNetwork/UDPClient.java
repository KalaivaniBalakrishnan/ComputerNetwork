import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class UDPClient {
    private static final int SERVER_PORT = 9999;
    private static final int BUFFER_SIZE = 1024;

    public static void main(String[] args) {
        try (DatagramSocket clientSocket = new DatagramSocket()) {
            InetAddress serverAddress = InetAddress.getByName("127.0.0.1"); // Replace with the server's IP address

            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.println("Tourism Management System Menu:");
                System.out.println("1. List Tourist Places");
                System.out.println("2. List Tourists");
                System.out.println("3. Book a Tour");
                System.out.println("4. Exit");
                System.out.print("Enter your choice: ");

                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume the newline

                String requestMessage = "";

                switch (choice) {
                    case 1:
                        requestMessage = "GET_PLACES";
                        break;
                    case 2:
                        requestMessage = "GET_TOURISTS";
                        break;
                    case 3:
                        System.out.print("Enter Place ID, Tourist ID, Guide Name, Amount, Days (comma-separated): ");
                        requestMessage = "BOOK_TOUR," + scanner.nextLine();
                        break;
                    case 4:
                        System.out.println("Exiting...");
                        return;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                        continue;
                }

                byte[] sendData = requestMessage.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, serverAddress, SERVER_PORT);
                clientSocket.send(sendPacket);

                byte[] receiveData = new byte[BUFFER_SIZE];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

                clientSocket.receive(receivePacket);
                String responseMessage = new String(receivePacket.getData(), 0, receivePacket.getLength());

                System.out.println("\nServer Response:\n" + responseMessage);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
