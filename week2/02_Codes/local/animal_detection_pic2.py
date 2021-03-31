from psychopy import core,visual,event
import numpy as np, glob as gb
f=[gb.glob('T*.jpg'),gb.glob('D*.jpg')] #files
f=np.append(np.random.choice(f[0],3,False),np.random.choice(f[1],3,False))
corAns=np.array(['y']*3+['n']*3)
ACC=np.array([]); RT=[]
w=visual.Window(fullscr=True)
for i in range(2):
  keys=np.array([])
  trials=np.random.permutation(range(len(f)))
  for j in trials:
    core.wait(1)
    visual.ImageStim(w,f[j],units='pix',size=[512,512]).draw() 
    w.flip(); core.wait(0.2); w.flip()
    r=event.waitKeys(keyList=['y','n'],timeStamped=core.Clock())
    keys=np.append(keys,r[0][0]); RT=np.append(RT,r[0][1])
  ACC=np.append(ACC,keys==corAns[trials])
np.savetxt('data.txt',np.vstack([ACC,RT]).T,['%d','%f'])
