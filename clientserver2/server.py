
import socket 
s = socket.socket()
print('Socket Created')
s.bind(('localhost',9999))  
s.listen(3)
print('waiting for connection')
while True:
    c, addr = s.accept()         #client socket & address
    name = c.recv(1024).decode()
    print("Connected with ", addr, name) 
    
    c.send(bytes('Welcome to Pixbim','utf-8'))


