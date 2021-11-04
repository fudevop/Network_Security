import socket
from IPy import IP


class PortScan():
    banners = []
    open_ports = []
    def __init__(self,target, port_num):
        self.target = target
        self.port_num = port_num

    def port_num(self):
        for port in range(1,self.port_num):
            self.scan(port)

    def validip(self):   #convert to given value into valid ip format
           try :
                IP(self.target)
                return self.target
           except ValueError:
             return socket.gethostbyname(self.target)

    def scan(self,port):
        try :
            converted_ip = self.validip()
            sock = socket.socket()  #open our ports
            sock.settimeout(3)    #set timeout for each port scanning period
            sock.connect((converted_ip, port)) #perform port scanning
            self.open_ports.append(port)
            try :
                banner = sock.recv(1500).decode().strip('\n').strip('\r')  #use to see service explanations belong to port
                self.banners.append(banner)
            except :
                self.banners.append('no_banner')
                pass
            sock.close()
        except:
           pass
