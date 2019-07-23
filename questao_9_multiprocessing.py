# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_9_multiprocessing

import multiprocessing, random, time

t0_epoch = float(time.time())
t0 = time.strftime("%S", time.localtime(t0_epoch))

a = []
b = []

saida = multiprocessing.Queue() 

N = 1000000 # N = 5000000 (5 milhões) ou N = 10000000 (10 milhões)

for i in range (N):
    a.append(random.randint(0,100))

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

def exe_processing(a, fatorial, b, saida):
    for n in a:
        saida.put(fatorial(n))

if __name__ == "__main__":
    
    tamanho = len(a)
    
    p0 = multiprocessing.Process(target=exe_processing, args=(a[0:int(tamanho/4)], fatorial, b, saida))
    p0.start()
    
    p1 = multiprocessing.Process(target=exe_processing, args=(a[int(tamanho/4):int(tamanho/2)], fatorial, b, saida))
    p1.start()
    
    p2 = multiprocessing.Process(target=exe_processing, args=(a[int(tamanho/2):int((2*tamanho)/3)], fatorial, b, saida))
    p2.start()
    
    p3 = multiprocessing.Process(target=exe_processing, args=(a[int((2*tamanho)/3):tamanho], fatorial, b, saida))
    p3.start() 
    
    while len(a) != len(b):
        b.append(saida.get())
    
    p0.join()
    p1.join()
    p2.join()
    p3.join()

t1_epoch = float(time.time())
t1 = time.strftime("%S", time.localtime(t1_epoch))

tf = round((t1_epoch - t0_epoch),2)

print("Tempo total de execucao: ", tf, "segundos.")