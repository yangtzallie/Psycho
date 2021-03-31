# -*- coding: utf-8 -*-
from psychopy import core,visual,event
import numpy as np
words=['小貓','小狗','貓熊','桌子','手機','袋子']
corAns=np.array(['y']*3+['n']*3)
ACC=np.array([]); RT=np.array([])
w=visual.Window(size=[800,600])
for i in range(2):
  keys=np.array([])
  trials=np.random.permutation(range(len(words)))
  for j in trials:
    core.wait(1)
    visual.TextStim(w,text=words[j],height=.5,font="Songti SC").draw()
    w.flip(); core.wait(0.2); w.flip()
    r=event.waitKeys(keyList=['y','n'],timeStamped=core.Clock())
    print(r)
    keys=np.append(keys,r[0][0]); RT=np.append(RT,r[0][1])
  ACC=np.append(ACC,keys==corAns[trials])
np.savetxt('data.txt',np.vstack([ACC,RT]).T,['%d','%f'])
