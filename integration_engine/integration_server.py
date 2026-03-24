import socket
from integration_engine.hl7_classifier import classify_hl7
from integration_engine.ack import generate_ack
from integration_engine.logger import log_message
import boto3
from sqs_sender import send_to_queue

HOST = "0.0.0.0"
PORT = 2575

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Integration Engine Running")

while True:
    conn, addr = server.accept()
    data = conn.recv(4096).decode()
    msg_type = classify_hl7(data)
    ack = generate_ack(data)
    conn.send(ack.encode())

    send_to_queue(data, msg_type)  

    log_message(data, msg_type)
    conn.close()