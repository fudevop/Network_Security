import socket
from IPy import IP

def get_banner(peer):
    return peer.recv(1500)

def validip(ipaddr):   #convert to given value into valid ip format
       try :
            IP(ip)
            return ip
       except ValueError:
            return socket.gethostbyname(ipaddr)

def scan(ip,port):
    try :
        sock = socket.socket()  #open our ports
        sock.settimeout(3)    #set timeout for each port scanning period
        sock.connect((ip, port)) #perform port scanning
        try :
            banner = get_banner(sock)  #use to see service explanations belong to port
            print(f"Port {port} is open on {ip} and the service is {banner.decode()}")
        except :
            print(f"Port {port} is open on {ip}")
    except:
        #print(f"Port {port} is close on {ip}")  #if we do not want to see closed ports we can configure PASS
        pass
 if __name__ == '__main__':  # it helps to program run this code if we only run this module itself,if we import this code into another program this __main__ code will not be run in there
    ip = input("Please type your ip addresses seperated by comman : ")
    iplist = ip.split(",")
    for ipaddr in iplist:
    validip(ipaddr)
    for port in range(20,120):
        scan(ipaddr,port)

