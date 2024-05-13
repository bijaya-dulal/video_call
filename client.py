# client.py
import cv2
import socket
import pickle
import struct

# Server IP and port
SERVER_HOST = '127.0.0.1'  # Change to the server's IP address
SERVER_PORT = 5000

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Receive frame from the server
data = b""
payload_size = struct.calcsize("L")

while True:
    # Receive frame size
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024)
        if not packet: break
        data += packet

    # Extract frame size and receive frame data
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Deserialize frame data
    frame = pickle.loads(frame_data)

    # Display the received frame
    cv2.imshow('Client - Press ESC to exit', frame)

    # Exit loop if ESC is pressed
    if cv2.waitKey(1) == 27:
        break

# Clean up
cv2.destroyAllWindows()
client_socket.close()
