import socket
import sys

def start_client(host='127.0.0.1', port=65432):
    """
    Starts a TCP client to connect to the server.
    """
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"[ATTEMPT] Connecting to server at {host}:{port}...")
        client_socket.connect((host, port))
        print("[SUCCESS] Connected to server!")

        # Send a message
        message = "Hello, Server! This is the Client."
        client_socket.sendall(message.encode('utf-8'))
        print(f"[SENT] Message: '{message}'")

        # Receive response
        data = client_socket.recv(1024)
        print(f"[RECEIVED] Server reply: {data.decode('utf-8')}")

    except ConnectionRefusedError:
        print("[ERROR] Connection refused. Is the server running?")
    except socket.gaierror:
        print("[ERROR] Address-related error. Check hostname/IP.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
    finally:
        print("[CLOSING] Closing connection.")
        client_socket.close()

if __name__ == "__main__":
    start_client()
   