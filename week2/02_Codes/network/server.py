import socket
code='utf-8'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('localhost', 1234)) # IP=localhost, port =12345
s.listen(1) # max number of clients
s.settimeout(60) # max waiting time=60s
for i in range(3):
 (c,adr)=s.accept() 
 print('Client:',i,adr)
 msg=c.recv(1024) # receive up to 1024 bytes
 print(msg.decode(code))
 c.sendall((str(i)+' from server!').encode(code))
s.close()
