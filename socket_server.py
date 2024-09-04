# socket_server.py

import socket
import time
import random

# Setup server
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started, waiting for connections on {HOST}:{PORT}")
    
    while True:
        conn, addr = s.accept()  # Blocking call until client connects
        print('Connected by', addr)
        with conn:
            try:
                while True:
                    # Simulate sending random data
                    data = str(random.uniform(0, 100))  # Random float data
                    print(f"Sending data: {data}")
                    conn.sendall(data.encode('utf-8'))  # Send encoded data
                    time.sleep(1)  # Simulate data flow every second
            except (BrokenPipeError, ConnectionResetError):
                print("Client disconnected, waiting for new connection...")
                break  # Go back to accepting new connections
