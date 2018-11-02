
from CM_pre_process_workingcopy import PreProcess
#import PreProcess

#def func(msg):
#    print(msg)

msg1={'corrid':1,'service_type':'generate','msg_type':'new_policy','msg':'hello kannan','status':'pending'}
msg2={'corrid':2,'service_type':'Approver','msg_type':'Approver_matching','msg':'idiot divi','status':'pending'}

p1=PreProcess()
p1.start(msg1)
print(p1)

p2=PreProcess()
p1.start(msg2)


print(p2)

#print(PreProcess())

