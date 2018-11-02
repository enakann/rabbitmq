from collections import OrderedDict
from weakref import WeakValueDictionary
import varsa 
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

class Singleton(type):
    #_instance = {}
    _instance=WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance=super(Singleton, cls).__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]

#hold=varsa.d

class PreProcess:
    #__metaclass__ = Singleton
    #global hold
    hold=varsa.d
    def __init__(self,msg,func):
        self.message=Message(msg)
        self.func=func

    def add(self):
         if self.message.corrid in self.hold:
               self.hold[self.message.corrid].append(self.message)
         else:
               self.hold[self.message.corrid]=[self.message]

    def start(self):
        self.add()
        if self.message.status == 'done':
           result=self.func(hold['corrid'])
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
    pass



p1=PreProcess({'corrid':1,'service_type':'generate','msg_type':'new_policy','msg':'hello kannan','status':'pending'},func)
p2=PreProcess({'corrid':2,'service_type':'Approver','msg_type':'Approver_matching','msg':'idiot divi','status':'pending'},func)

#p1.start()
#print(p1)
#p2.start()

#import pdb;pdb.set_trace()
#print(p2)





