import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind (('192.168.31.163',9090))
client = []
print ('сервер запущен')
f = open("G:\chat.txt","w")
while 1:
    data , addres = s.recvfrom(1024)
    print (addres[0], addres[1])
    if addres not in client :
        client.append(addres)
    for clients in client :
        if clients == addres :
            continue
        s.sendto(data,clients)