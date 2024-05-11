import threading
from socket import *

s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 4600
s.bind((host, port))
s.listen()

handled_clients = 0
clients = []
nicknames = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle(client):
    global handled_clients
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client) 
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            handled_clients -= 1
            if handled_clients == 0:
                s.close()
            break

def receive():
    global handled_clients
    while True:
        print("Server is running, if you need to leave the chat room write 'exit'")
        client, addr = s.accept()
        handled_clients += 1
        print(f'{str(addr)} connected to the server')
        client.send('Nickname?'.encode('utf-8'))
        nickname = client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)
        print('Nickname of the new client is ' + str(nickname))
        broadcast(f'{nickname} connected to the chat room'.encode('utf-8'), client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()