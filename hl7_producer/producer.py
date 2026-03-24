import socket
import time
import glob

HOST = "localhost"
PORT = 2575

files = glob.glob("../hl7_samples/*.hl7")

while True:

    for f in files:

        msg = open(f).read()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        s.send(msg.encode())

        # 🔥 WAIT FOR ACK
        ack = s.recv(4096).decode()

        print("Sent:", f)
        print("ACK Received:")
        print(ack)

        s.close()

        time.sleep(3)