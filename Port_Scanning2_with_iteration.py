import socket
from IPy import IP


def scan(ip,port):
    try :
        sock = socket.socket()  #open our ports
        sock.settimeout(3)    #set timeout for each port scanning period
        sock.connect((ip, port)) #perform port scanning
        print(f"Port {port} is open on {ip}")
    except:
        print(f"Port {port} is close on {ip}")

ip = input("Please type your ip address : ")
for port in range(53,55):
    scan(ip,port)