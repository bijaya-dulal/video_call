# server.py
import cv2
import socket
import pickle
import struct

# Server IP and port
SERVER_HOST = '0.0.0.0'  # Use '0.0.0.0' to listen on all available interfaces
SERVER_PORT = 5000

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)  # Listen for incoming connections

print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established!")

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Serialize the frame
    data = pickle.dumps(frame)

    # Send frame size and frame data to the client
    message_size = struct.pack("L", len(data))
    client_socket.sendall(message_size + data)

    # Display the frame locally
    cv2.imshow('Server - Press ESC to exit', frame)

    # Exit loop if ESC is pressed
    if cv2.waitKey(1) == 27:
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
