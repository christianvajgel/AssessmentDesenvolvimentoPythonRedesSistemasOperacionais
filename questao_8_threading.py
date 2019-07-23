# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_8_threading

import threading

a = [1, 2, 3, 4, 5]
b = []

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

def exe_threading(a, fatorial, b):
    for n in a:
        b.append(fatorial(n))
  
tamanho = len(a)

t0 = threading.Thread(target=exe_threading, args=(a[0:int(tamanho/4)], fatorial, b))
t0.start() 

t1 = threading.Thread(target=exe_threading, args=(a[int(tamanho/4):int(tamanho/3)], fatorial, b))
t1.start() 

t2 = threading.Thread(target=exe_threading, args=(a[int(tamanho/3):int(tamanho/2)], fatorial, b))
t2.start() 

t3 = threading.Thread(target=exe_threading, args=(a[int(tamanho/2):tamanho], fatorial, b))
t3.start() 

t0.join() 
t1.join() 
t2.join()
t3.join()

print("Módulo Threading com 4 threads:")
print("Vetor A =", a)
print("Vetor A! =", b)