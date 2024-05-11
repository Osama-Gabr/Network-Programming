import threading
from socket import *

Nickname = input('Enter your nickname:')

client = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 4600

client.connect((host,port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "Nickname?":
                client.send(Nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("you left chat room.")
            client.close()
            break

def send():
    while True:
        text = input()
        message = f'{Nickname}: {text}'
        client.send(message.encode('utf-8'))
        if text == "exit" :
            client.close()
            break

    
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
