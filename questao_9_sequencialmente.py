# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_9_sequencialmente

import random, time

t0_epoch = float(time.time())
t0 = time.strftime("%S", time.localtime(t0_epoch))

a = []
b = []

N = 1000000 # N = 5000000 (5 milhões) ou N = 10000000 (10 milhões)

for i in range (N):
    a.append(random.randint(0,100))

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

for n in a:
    b.append(fatorial(n))

t1_epoch = float(time.time())
t1 = time.strftime("%S", time.localtime(t1_epoch))

tf = round((t1_epoch - t0_epoch),2)

print("Tempo total de execucao: ", tf, "segundos.")
