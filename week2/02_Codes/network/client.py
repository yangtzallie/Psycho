import socket
code='utf-8'
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost', 1234)) 
c.sendall('Hello from client!'.encode(code))
print(c.recv(1024).decode(code))
c.close()
