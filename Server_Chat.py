import socket
import threading

def handle_client(client_socket, client_address, clients):
    try:
        print(f"New connection from {client_address}")

        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            print(f"Received from {client_address}: {message}")

            # Broadcast the message to all clients
            for other_client, _ in clients:
                if other_client != client_socket:
                    try:
                        other_client.send(message.encode())
                    except:
                        # Remove disconnected client
                        clients.remove((other_client, _))

    except Exception as e:
        print(f"Error handling client {client_address}: {e}")

    finally:
        print(f"Connection from {client_address} closed")
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(5)
    print('Server is listening...')

    clients = []

    while True:
        client_socket, client_address = server.accept()
        clients.append((client_socket, client_address))

        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
        client_handler.start()

if __name__ == "__main__":
    start_server()

