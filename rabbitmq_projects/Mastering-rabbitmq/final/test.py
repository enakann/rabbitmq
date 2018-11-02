from CM_pre_process_workingcopy import PreProcess
import tes2
#import PreProcess

#def func(msg):
#    print(msg)


msg3={'corrid':3,'service_type':'generate','msg_type':'new_policy','msg':'hello kannan','status':'pending'}

p3=PreProcess()
p3.start(msg3)
print(p3)
