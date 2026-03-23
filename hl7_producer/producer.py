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
        s.close()

        print("Sent:", f)
        time.sleep(3)