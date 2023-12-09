import paramiko

def main():
    ip = ''
    username = ''
    password = ''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password, timeout=5)
    print(client)

if __name__ == '__main__':
    main()