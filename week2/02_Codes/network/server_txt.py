from psychopy import core,visual,event
import socket,numpy as np

code='utf-8'; nTrials=6
words=['cat','dog','panda','table','iphone','bag']
instruct='Press 1, 2, ..., 6 to pick a word:\n\n'
instruct=instruct+', '.join(words)
corAns=np.array(['y']*3+['n']*3)
ACC=np.array([]); RT=np.array([])
w=visual.Window(size=[800,500],color=[-1,-1,-1])
visual.TextStim(w,text='Waiting for a client').draw()
w.flip() # show init screen

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('localhost', 1234))
s.listen(1) # allow 1 client
(c,adr)=s.accept()

for i in range(nTrials):
 visual.TextStim(w,text=instruct).draw()
 w.flip() # show choices
 print('Server got:')
 key=event.waitKeys(keyList=['1','2','3','4','5','6']) # allow 1-6
 print(key)
 w.flip() # clear screen
 idx=int(key[0])-1 # choice as the array index
 c.sendall((corAns[idx]+words[idx]).encode(code)) # something like 'ycat'
 visual.TextStim(w,text='Waiting for the client').draw()
 w.flip() # show waiting
 print(c.recv(1).decode()) # waiting for a response from the client
