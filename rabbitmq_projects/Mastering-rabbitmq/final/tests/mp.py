from multiprocessing import Process,Queue
from threading import Thread
d={}

class c1:
    def run(self,q):
        d['a']=1
        q.put(d)

class c2:
    def run(self,q):
        d=q.get()
        d['b']=2
        print(d)


subscriber_list = []
subscriber_list.append(c1())
subscriber_list.append(c2())
def mp():
    q=Queue()
    process_list = []
    for sub in subscriber_list:
        process = Process(target=sub.run,args=(q,))
        process.start()
        process_list.append(process)
# wait for all process to finish
    for process in process_list:
        process.join()



def thread():
    threads=[]
    for sub in subscriber_list:
        t=Thread(target=sub.run)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


mp()
#thread()

#if __name__ == '__main__':
#    subscriber_list = []
#    subscriber_list.append(c1())
#    subscriber_list.append(c2())
#    process_list = []
#    for sub in subscriber_list:
#        process = Process(target=sub.run)
#        process.start()
#        process_list.append(process)
# wait for all process to finish
#    for process in process_list:
#        process.join()

