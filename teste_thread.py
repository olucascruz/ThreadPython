import threading
import time

sem1 = threading.Semaphore()
sem2 = threading.Semaphore()


def Thread_one():
    sem1.acquire()
    for i in range(10):
        print("Thread 1 - " + str(i) + "\n")
        time.sleep(1)
    sem1.release()

def Thread_two():
    sem1.acquire()
    for i in range(10):
        print("Thread 2 - " + str(i) + "\n")
        time.sleep(2)
    sem1.release()

def Thread_three():
    sem2.acquire()
    for i in range(10):
        print("Thread 3 - " + str(i) + "\n")
        time.sleep(3)
    sem2.release()



t0 = threading.Thread(target=Thread_one)
t0.start()
t1 = threading.Thread(target=Thread_two)
t1.start()
t2 = threading.Thread(target=Thread_three)



    