# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_8_multiprocessing

import multiprocessing

a = [1, 2, 3, 4]
b = []

saida = multiprocessing.Queue()

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
    
    p0 = multiprocessing.Process(target=exe_processing, args=(a[0:1], fatorial, b, saida))
    p0.start()
    
    p1 = multiprocessing.Process(target=exe_processing, args=(a[1:2], fatorial, b, saida))
    p1.start()
    
    p2 = multiprocessing.Process(target=exe_processing, args=(a[2:3], fatorial, b, saida))
    p2.start()
    
    p3 = multiprocessing.Process(target=exe_processing, args=(a[3:tamanho], fatorial, b, saida))
    p3.start() 
    
    while len(a) != len(b):
        b.append(saida.get())
    
    p0.join()
    p1.join()
    p2.join()
    p3.join()

    print("Lista B:", b)