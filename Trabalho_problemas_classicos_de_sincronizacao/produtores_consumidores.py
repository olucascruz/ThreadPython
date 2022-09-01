import threading
import time
import random

# Código desenvolvido por Adriano Henrique

sem1 = threading.Semaphore(1)
sem2 = threading.Semaphore(1)
buffer = [0,0,0,0,0,0,0,0,0]
espera_c = False
espera_p = False

def produtor():
  while True:
    sem1.acquire()
    for i in range(len(buffer)):
      if buffer[i] == 0:
        buffer[i] = 1
        print("\n item adicionado \n" + str(buffer))
        break
      elif i == len(buffer)-1:
        espera_p = True
        print("\n produtor entrou em espera")
        while espera_p == True:
          for i in range(len(buffer)):
            if buffer[i] == 0:
              buffer[i] = 1
              print("\n item em espera adicionado \n" + str(buffer))
              espera_p = False
        print("\n produtor saiu do modo espera")
    time.sleep(random.randrange(1,4))
    sem1.release()
      

def consumidor():
  while True:
    sem2.acquire()
    for i in range(len(buffer)):
      if buffer[i] == 1:
        buffer[i] = 0
        print("\n item removido \n" + str(buffer))
        break
      elif i == len(buffer)-1:
        espera_c = True
        print("\n consumidor entrou em espera")
        while espera_c == True:
          for i in range(len(buffer)):
            if buffer[i] == 1:
              buffer[i] = 0
              print("\n item em espera removido \n" + str(buffer))
              espera_c = False
        print("\n consumidor saiu do modo espera")
    time.sleep(random.randrange(1,4))
    sem2.release()

p0 = threading.Thread(target=produtor)
p1 = threading.Thread(target=produtor)
p2 = threading.Thread(target=produtor)
c0 = threading.Thread(target=consumidor)
c1 = threading.Thread(target=consumidor)
c2 = threading.Thread(target=consumidor)

p0.start()
p1.start()
p2.start()
c0.start()
c1.start()
c2.start()