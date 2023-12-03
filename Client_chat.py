import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(f"Received: {message}")

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))

    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    # Main thread to send messages
    while True:
        message = input("Your message: ")
        client.send(message.encode())

        if message.lower() == 'exit':
            break

    client.close()

if __name__ == "__main__":
    start_client()
