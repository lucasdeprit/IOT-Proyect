import threading
from timeit import default_timer as timer
import time



while True:

    event = threading.Event()
    condition = False
    
    def myfunction():
        start=timer()
        event.wait()
        end = timer()
        print (end - start)
    
    t1=threading.Thread(target=myfunction)
    t1.start()
    
    if condition==True:
        event.set()


