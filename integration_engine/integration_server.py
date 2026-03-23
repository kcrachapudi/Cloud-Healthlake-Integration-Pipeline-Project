import socket
from router import route_message
from ack import generate_ack
from logger import log_message

HOST = "0.0.0.0"
PORT = 2575

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Integration Engine Running")

while True:
    conn, addr = server.accept()

    data = conn.recv(4096).decode()

    msg_type = route_message(data)

    ack = generate_ack(data)

    conn.send(ack.encode())

    log_message(data, msg_type)

    conn.close()