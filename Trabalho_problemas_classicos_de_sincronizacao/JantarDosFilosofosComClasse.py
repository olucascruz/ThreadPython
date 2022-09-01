import random
import threading
import time

#Código produzido por Lucas Cruz

# Cada garfo é um semaforo
garfo1 = threading.Semaphore()
garfo2 = threading.Semaphore()
garfo3 = threading.Semaphore()
garfo4 = threading.Semaphore()
garfo5 = threading.Semaphore()

class filosofo(threading.Thread):                           #Classe filosofo
    def __init__(self,  GarfoDireito, GarfoEsquerdo, nome): 
        threading.Thread.__init__(self)
        self.GarfoDireito = GarfoDireito
        self.GarfoEsquerdo = GarfoEsquerdo
        self.nome = nome
    #Função pensar
    def Pensar(self):                                        
        #O filósofo pensa por um tempo aleatório-
        tempo_pensando = random.randint(1, 3)
        print(f'{self.nome} Pensando por {tempo_pensando} segundos ')
        time.sleep(tempo_pensando);
    #Função comer
    def Comer(self):
        #Sinaliza está usando o garfo a direita
        print(f"{self.nome} pega o garfo direito ")             
        self.GarfoDireito.acquire()                        
        
        # Tenta usar o garfo a esquerda caso esteja ocupado  espera por 2 segundos 
        # caso não libere larga o garfo direito
        print(f"{self.nome} Tenta pegar o garfo esquerdo ")
        tempo_esperando_liberar_garfo = 2
        pegar_garfo_esquerdo = self.GarfoEsquerdo.acquire(True,  tempo_esperando_liberar_garfo) 

        if(not pegar_garfo_esquerdo):
            print(f"{self.nome} larga garfo direito ")
            self.GarfoDireito.release()

        # Se consegue pegar os dois garfos come por um tempo aleatorio
        tempo_comendo = random.randint(1, 3)
        print(f"{self.nome} Comendo por {tempo_comendo} segundos ")
        time.sleep(tempo_comendo) 
        
        # Ao acabar de comer larga os garfos permitindo
        # que os filósofos ao seu lado possam comer (usar os recursos)
        print(f"{self.nome} larga garfo direito ")
        self.GarfoDireito.release()
        
        print(f"{self.nome} larga garfo esquerdo ")
        self.GarfoEsquerdo.release()
    #Função que mantém a rotina comer e pensar.           
    def run(self):
        #Alterna entre comer e pensar
        while True:
            self.Comer()
            self.Pensar()
            
            
  
#Instancia ss filosofos e determina quais 
#os garfos de cada um.
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
