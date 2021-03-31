from psychopy import core,visual,event
import numpy as np,glob as gb,socket

code='utf-8'; nTrials=6
instruct='Press 1, 2, ..., 6 to pick a picture:\n\n'
f=[gb.glob('T*.jpg'),gb.glob('D*.jpg')] # picture files
f=np.append(np.random.choice(f[0],3,False),np.random.choice(f[1],3,False))
corAns=np.array(['y']*3+['n']*3)
w=visual.Window(size=[800,500],color=[-1,-1,-1],units='norm')
visual.TextStim(w,text='Waiting for a client').draw()
w.flip() # show init screen

imgs=[] # list of 6 images 
for i in range(len(f)):
  (x,y)=(-.75+i*.3,-.2)
  imgs.append(visual.ImageStim(w,f[i],size=.3,pos=(x,y)))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('localhost', 1234))
s.listen(1) # allow 1 client
(c,adr)=s.accept()

for t in range(nTrials):
  visual.BufferImageStim(w,stim=imgs).draw()
  visual.TextStim(w,text=instruct).draw()
  w.flip() # show choices
  print('Server got:')
  key=event.waitKeys(keyList=['1','2','3','4','5','6']) # allow 1-6
  print(key)
  w.flip() # clear screen
  idx=int(key[0])-1 # choice as the array index
  with open(f[idx],'rb') as file:
    data=file.read() # read in pic file
  c.sendall((corAns[idx]+str(len(data))).encode(code)) # inform ans + pic size
  c.sendall(data) # send pic file to the client
  visual.TextStim(w,text='Waiting for the client').draw()
  w.flip() # show waiting
  print(c.recv(1).decode(code)) # waiting for a response from the client

s.close()
