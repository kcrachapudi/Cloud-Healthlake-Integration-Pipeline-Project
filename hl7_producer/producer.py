import socket
import glob
import time

HOST = "localhost"
PORT = 2575

files = glob.glob("../hl7_samples/*.hl7")

for f in files:

    msg = open(f).read()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.send(msg.encode())

    ack = s.recv(4096).decode()

    print("Sent:", f)
    print("ACK:", ack)

    s.close()

    time.sleep(1)

print("All HL7 messages sent successfully.")