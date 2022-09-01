import threading
import time

# Código desenvolvido por Larissa Roque


# Controlar a área a ser acessada
area_semaforo = threading.Semaphore()
# Controlar o acesso ao número de leitores
contador_leitores_semaforo = threading.Semaphore()

# Total de leitores por vez
contador_leitores = 0

# Área que será lida ou alterada
livro = "000"
# Valor base para alterar o texto
texto = 0

def leitor():
    global area_semaforo, contador_leitores_semaforo
    global contador_leitores, livro

    while(True):
        # Acesso exclusivo ao contador
        contador_leitores_semaforo.acquire()
        contador_leitores += 1

        # Se for o primeiro Leitor...
        if contador_leitores == 1:
            # Requer acesso ao livro
            area_semaforo.acquire()
        # Liberar o contador
        contador_leitores_semaforo.release()

        # Leitura do livro
        print("Leitor ", contador_leitores, "leu: ", livro)

        # Acesso exclusivo ao contador
        contador_leitores_semaforo.acquire()
        contador_leitores -= 1

        # Se for o último Leitor...
        if contador_leitores == 0:
            # Libera acesso ao livro
            area_semaforo.release()
        # Liberar o contador
        contador_leitores_semaforo.release()

        time.sleep(1)

def escritor():
    global area_semaforo, contador_leitores_semaforo
    global contador_leitores, livro, texto

    while(True):
        # Requer acesso ao livro
        area_semaforo.acquire()

        # Realiza alteração no livro
        texto += 1
        livro = str(texto%10)*3
        print("Escritor alterou o livro: ", livro)

        # Libera acesso ao livro
        area_semaforo.release()

        time.sleep(1)

################################################
'''
Main
'''
###############################################

Leitor1 = threading.Thread(target=leitor).start()
Leitor2 = threading.Thread(target=leitor).start()
Leitor3 = threading.Thread(target=leitor).start()
Leitor4 = threading.Thread(target=leitor).start()
Escritor = threading.Thread(target=escritor).start()