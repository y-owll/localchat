import socket
import threading


def read_sok():
    while 1:
        data = s.recv(1024)
        print(data.decode('utf-8'))


server = ('192.168.31.163', 9090)
print('введите ваш никнейм')
nickname = input()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.31.163', 0))
s.sendto((nickname + ' => присоединился к чату').encode('utf-8'), server)
potok = threading.Thread(target=read_sok)  
potok.start()

while 1:
    message = input()
    if message == '/history':
        g = open(r"G:\chat.txt", "r")
        history = g.read()
        print(history)
    else:
        with open(r"G:\chat.txt", "a") as file:
            file.writelines('[' + nickname + ']' + message + '\n')
        s.sendto(('[' + nickname + ']' + message).encode('utf-8'), server)
