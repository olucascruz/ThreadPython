import random
import threading
import time

garfo1 = threading.Semaphore()
garfo2 = threading.Semaphore()
garfo3 = threading.Semaphore()
garfo4 = threading.Semaphore()
garfo5 = threading.Semaphore()

garfo1.release
lista = []

class filosofo(threading.Thread):
    def __init__(self,  GarfoDireito, GarfoEsquerdo, nome):
        threading.Thread.__init__(self)
        self.GarfoDireito = GarfoDireito
        self.GarfoEsquerdo = GarfoEsquerdo
        self.nome = nome

    def Pensar(self):
        random1 = random.randint(1, 3)
        print(f'{self.nome} Pensando por {random1} segundos')
        time.sleep(random1);

    def Comer(self):
        print(f"{self.nome} Tenta pegar o garfo direito")
        self.GarfoDireito.acquire()
        
        print(f"{self.nome} Tenta pegar o garfo esquerdo")
        print(self.GarfoEsquerdo.acquire(True, 5))
        
        print(f"{self.nome} Comendo")
        time.sleep(random.randint(1, 3)) 
        
        print(f"{self.nome} larga garfo direito")
        self.GarfoDireito.release()
        
        print(f"{self.nome} larga garfo esquerdo")
        self.GarfoEsquerdo.release()
        
        
    def run(self):
        for i in range(10):
            self.Comer()
            self.Pensar()
            
            
  


filosofo1 = filosofo(garfo1, garfo2, "f1")
filosofo1.start()
filosofo2 = filosofo(garfo2, garfo3, "f2")
filosofo2.start()
filosofo3 = filosofo(garfo3, garfo4, "f3")
filosofo3.start()
filosofo4 = filosofo(garfo4, garfo5, "f4")
filosofo4.start()
filosofo5 = filosofo(garfo5, garfo1, "f5")
filosofo5.start()
