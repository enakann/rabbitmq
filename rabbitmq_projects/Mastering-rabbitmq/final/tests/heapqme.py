import heapq
import uuid
from time import time

ls=[]

def func1():
    return {'priority':time(),'corid':str(uuid.uuid4()),'redflag':'redflag','newpolicy':True}



def add():
    global ls
    item=func1()
    heapq.heappush(ls,item)
    return


q1=add()
print(q1)




