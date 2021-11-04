import Port_Scanning6_withClass

targets_ip = input('Please type ip addresses to scan : ')
port_number = int(input('Please type port numbers : '))

target = Port_Scanning6_withClass.PortScan(targets_ip,port_number)
target.port_num()


with  open('vulnerabilities.txt','w+') as file :
  for i in range(len(target.open_ports)):
      file.write('\n')
      port_list = target.open_ports
      banners_list = target.banners
      file.write(f'open port is {str(port_list[i])} with banner {banners_list[i]}')


