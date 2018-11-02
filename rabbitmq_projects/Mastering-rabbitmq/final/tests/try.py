import time
import threading

# based on https://stackoverflow.com/a/2785908/1056345                                                                                                                                                                                                                                                                         
def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
    must_end = time.time() + timeout
    while time.time() < must_end:
        if somepredicate(*args, **kwargs):
            return True
        time.sleep(period)
    return False

def wait_until_par(*args, **kwargs):
    t = threading.Thread(target=wait_until, args=args, kwargs=kwargs)
    t.start()
    print ('wait_until_par exits, thread runs in background')

def test():
    print('test')

wait_until_par(test, 5)
