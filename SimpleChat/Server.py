from socket import *
s = socket(AF_INET,SOCK_STREAM)
print("socket successfully created")
host='127.0.0.1'
port= 6500
s.bind((host,port))
print("socket binded to ",port)
s.listen(5)
print("socket is listening")
c,addr = s.accept()
print('get connection from', addr)

while True:
    y=c.recv(2048)
    print("client:",y.decode('utf-8'))
    if y.decode('utf-8') == "Salam" :
        break   
    message= input("server: ").encode('utf-8')
    length = len(message)
    if length > 2048:
        x = (length % 2048) + 1
        for i in range(x):
            s = i * 2048
            e = min((i + 1) * 2048, length)
            s.send(message[s:e])
    else:
        c.send(message)
       
c.close()