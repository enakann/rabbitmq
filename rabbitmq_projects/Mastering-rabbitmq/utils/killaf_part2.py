import multiprocessing
import time

# bar
def bar():
    for i in range(10):
        print "Tick"
        time.sleep(1)
    return 1

    # Start bar as a process
def run():
   p = multiprocessing.Process(target=bar)
   p.start()

    # Wait for 10 seconds or until process finishes
   p.join(20)

    # If thread is still active
   if p.is_alive():
        print "running... let's kill it..."

        # Terminate
        p.terminate()
        p.join()
   return 0


print(run())
