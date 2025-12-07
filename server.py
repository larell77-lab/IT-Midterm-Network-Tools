import socket
import sys

def start_server(host='127.0.0.1', port=65432):
    """
    Starts a basic TCP server that listens for incoming connections.
    """
    # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow the address to be reused immediately after the program closes
    # This prevents "Address already in use" errors during testing
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Bind the socket to the host and port
        server_socket.bind((host, port))
        print(f"[STATUS] Server started on {host}:{port}")
        
        # Listen for incoming connections
        server_socket.listen()
        print("[STATUS] Waiting for incoming connections...")

        # Accept a connection
        conn, addr = server_socket.accept()
        with conn:
            print(f"[CONNECTED] Connected by {addr}")
            
            while True:
                # Receive data from the client (buffer size 1024 bytes)
                data = conn.recv(1024)
                if not data:
                    break # Connection closed by client
                
                decoded_data = data.decode('utf-8')
                print(f"[RECEIVED] Client says: {decoded_data}")
                
                # Send a response back to the client
                response = f"Server received: {decoded_data}"
                conn.sendall(response.encode('utf-8'))
                print("[SENT] Response sent to client.")
                
    except KeyboardInterrupt:
        print("\n[STOP] Server stopped manually.")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    finally:
        server_socket.close()
        print("[CLOSED] Server socket closed.")

if __name__ == "__main__":
    start_server()