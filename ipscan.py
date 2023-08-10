import pyfiglet
from tqdm import tqdm
import sys
import time
import socket
from datetime import datetime

text = pyfiglet.figlet_format("WELCOME")
for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.003)

target = input(str("Enter Target IP:"))

print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:
    for port in tqdm(range(1, 65535)): # 1,100 (quick scan) ,1,65535 (full scan)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
            print("Scanning Port:", port)
        s.close()

except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()

except socket.error:
    print("\n Host not responding :(")
    sys.exit()