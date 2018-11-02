from collections import OrderedDict
from weakref import WeakValueDictionary
from singleton import Singleton
import varsa
#import __builtin__
#__builtin__.PreProcess=PreProcess


class Message:
    def __init__(self,msg):
        self.msg=msg
        self.service_type=self.msg['service_type']
        self.msg_type=self.msg['msg_type']
        self.corrid=self.msg['corrid']
        self.status=self.msg['status']
    def __repr__(self):
        return "{}-{}-{}".format(self.service_type,self.msg_type,self.corrid)

#hold=OrderedDict()

_register = {}

def singleton(cls):
   def wrapper(*args, **kw):
       if cls not in _register:
           instance = cls(*args, **kw)
           _register[cls] = instance
       return _register[cls] 

   wrapper.__name__ = cls.__name__
   return wrapper

#@singleton
class PreProcess:
   # __metaclass__ = Singleton
    #hold=OrderedDict()
    #global hold
    hold=varsa.d
    def __init__(self):
        print("object initated")

    def add(self,msg):
         self.message=Message(msg)
         if self.message.corrid in self.hold:
               self.hold[self.message.corrid].append(self.message)
         else:
               self.hold[self.message.corrid]=[self.message]

    def start(self,msg):
        self.add(msg)
        if self.message.status == 'done':
           result=func(hold['corrid'])
           if result:
               return True
           else:
               return False
               #return the message to the individual queue using  hold['corrid']  if failed
        else:
            pass
    def __getitem__(self,index):
        return self.hold[index]

    def __repr__(self):
       return str(self.hold)

def func(msg):
    print(msg)

#msg1={'corrid':1,'service_type':'generate','msg_type':'new_policy','msg':'hello kannan','status':'pending'}
#msg2={'corrid':2,'service_type':'Approver','msg_type':'Approver_matching','msg':'idiot divi','status':'pending'}

#p1=PreProcess()
#p2=PreProcess()

#p1.start(msg1)
#print(p1)
#p2.start(msg2)

#import pdb;pdb.set_trace()
#print(p2)




#import __builtin__
#__builtin__.PreProcess=PreProcess

