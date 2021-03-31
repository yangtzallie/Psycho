from psychopy import core,visual,event
import numpy as np,glob as gb,socket

w=visual.Window(size=[800,400],units='norm')
visual.TextStim(w,text='Waiting for the server').draw()
w.flip(); code='utf-8'; nTrials=6; ACC=np.array([]);

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost', 1234))

for i in range(nTrials):
  msg=c.recv(6).decode(code); print(msg); 
  sz=int(msg[1:]);
  with open('tmp.jpg','wb') as file:
    file.write(c.recv(sz))
  visual.ImageStim(w,'tmp.jpg',size=[0.8,0.8]).draw(); w.flip()
  key=event.waitKeys(keyList=['y','n'])
  print(key);w.flip()
  ACC=np.append(ACC,key[0]==msg[0])
  c.sendall(key[0].encode(code))

c.close()
print(np.mean(ACC))
