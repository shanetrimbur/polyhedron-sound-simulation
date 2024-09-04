# socket_client.py

import socket
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Setup client
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Variables for storing and plotting the data
data_stream = []

# Create the figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
line, = ax.plot([], [], lw=2)

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

# Function to update the plot with streaming data
def update(frame):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024).decode('utf-8')  # Receive and decode data
            print(f"Received data: {data}")
            if data:
                data_stream.append(float(data))
    except ConnectionResetError:
        print("Connection reset by server, retrying...")
        time.sleep(1)
        return line,
    except ConnectionRefusedError:
        print("Server not available, retrying...")
        time.sleep(1)
        return line,

    # Update the plot with the latest data
    line.set_data(range(len(data_stream)), data_stream)
    
    # Adjust x-axis as new data is appended
    ax.set_xlim(0, max(100, len(data_stream)))
    
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=1000)

# Show the plot
plt.show()
