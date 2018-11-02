from time import time
import uuid
import heapq
from collections import OrderedDict



def getitem():
    yield {'priority':22.12,'corid':"d02d5ec4-1559-4318-97a2-4a29a01cf963",'redflag':'redflag','np_present':False}
    yield {'priority':11.12,'corid':"97b84c6f-8626-416d-8265-4d6c1169e26e",'redflag':'redflag','np_present':True}
    yield {'priority':33.12,'corid':"3de6c8cd-63dc-4b6c-8ed5-d461d72f9232",'redflag':'redflag','np_present':True}


def comp(msg):
  if msg['corid'] in d and msg['newpolicy']:
      print("yes its there")


f=getitem()
item1=next(f)
item2=next(f)
item3=next(f)

d=OrderedDict()

d[item1['corid']]=item1
d[item2['corid']]=item2
d[item3['corid']]=item3

newinp={'corid':'d02d5ec4-1559-4318-97a2-4a29a01cf963','newpolicy':'newpolicy3'}

comp(newinp)


