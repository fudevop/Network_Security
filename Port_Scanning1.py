import socket
from IPy import IP

ip = input("Please type your ip address : ")
port = int(input("Please type your port number : "))

try :
    sock = socket.socket()
    sock.connect((ip, port))
    print(f"Port {port} is open on {ip}")
except:
    print(f"Port {port} is close on {ip}")

