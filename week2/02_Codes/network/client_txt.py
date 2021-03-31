from psychopy import core,visual,event
import socket,numpy as np
socket.setdefaulttimeout(None)

code='utf-8'; nTrials=6
ACC=np.array([]);
w=visual.Window(size=[800,400])
visual.TextStim(w,text='Waiting for the server').draw()
w.flip() # show init screen

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost', 1234)) # connect to the server

for i in range(nTrials):
  msg=c.recv(1024).decode(code) # read correct answer + experiment word
  visual.TextStim(w,text=msg[1:]).draw() 
  w.flip() # show the received word
  key=event.waitKeys(keyList=['y','n']) # ask animal or not 
  print(key);w.flip()
  ACC=np.append(ACC,key[0]==msg[0]) # correct?
  c.sendall(key[0].encode(code)) # send response back to the server

c.close()
print(np.mean(ACC)) # show accuracy
