import random
import threading
import time

garfo1 = threading.Semaphore()
garfo2 = threading.Semaphore()
garfo3 = threading.Semaphore()
garfo4 = threading.Semaphore()
garfo5 = threading.Semaphore()


def filosofo():
    while(True):
        pensando()
        comendo()

def pensando():
    for i in range():
        time.sleep(random.randint(5, 15))

def comendo():
    for i in range():
        time.sleep(random.uniform(5, 15))



t1 = threading.Thread(target=filosofo)
t1.start()
t2 = threading.Thread(target=filosofo)
t2.start()
t3 = threading.Thread(target=filosofo)
t3.start()
t4 = threading.Thread(target=filosofo)
t4.start()
t5 = threading.Thread(target=filosofo)
t5.start()
