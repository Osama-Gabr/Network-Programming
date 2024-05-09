from socket import *
s = socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port= 6500
s.connect((host,port))
print("'Salam' to end the session")

while True:
    message= input("client: ").encode('utf-8')
    length = len(message)
    if length > 2048:
        x = (length % 2048) + 1
        for i in range(x):
            s = i * 2048
            e = min((i + 1) * 2048, length)
            s.send(message[s:e])
    else:
        s.send(message)
    if message.decode('utf-8') == "Salam":
         break
    y=s.recv(2048)
    print("server:",y.decode('utf-8'))
    
s.close()