import random
import threading
import time

garfo1 = threading.Semaphore()
garfo2 = threading.Semaphore()
garfo3 = threading.Semaphore()
garfo4 = threading.Semaphore()
garfo5 = threading.Semaphore()

lista = [0, 0, 0, 0, 0]
class filosofo(threading.Thread):
    def __init__(self,  GarfoDireito, GarfoEsquerdo, nome , index):
        threading.Thread.__init__(self)
        self.GarfoDireito = GarfoDireito
        self.GarfoEsquerdo = GarfoEsquerdo
        self.nome = nome
        self.index = index

    def Pensar(self):
        random1 = random.uniform(5, 15)
        print(f'Pensando {self.nome}')
        time.sleep(random1);

    def Comer(self):
        print(f"{self.nome} Tenta pegar o garfo direito")
        self.GarfoDireito.acquire()
        print(f"{self.nome} Tenta pegar o garfo esquerdo")
        locked = self.GarfoEsquerdo.acquire(False)
        if locked:
            print(f"{self.nome} Devolve o garfo direito")
            self.GarfoDireito.release()
            return
        print(f"{self.nome} Comendo")
        lista[self.index] = 1
        print(lista)
        time.sleep(random.uniform(5, 15)) 
        self.GarfoDireito.release()
        self.GarfoEsquerdo.release()
        lista[self.index] = 0
        
    def run(self):
        while(True):
           
            self.Pensar()
            self.Comer()
            
  


filosofo1 = filosofo(garfo1, garfo2, "f1", 0)
filosofo1.start()
filosofo2 = filosofo(garfo2, garfo3, "f2", 1)
filosofo2.start()
filosofo3 = filosofo(garfo3, garfo4, "f3", 2)
filosofo3.start()
filosofo4 = filosofo(garfo4, garfo5, "f4", 3)
filosofo4.start()
filosofo5 = filosofo(garfo5, garfo1, "f5", 4)
filosofo5.start()
