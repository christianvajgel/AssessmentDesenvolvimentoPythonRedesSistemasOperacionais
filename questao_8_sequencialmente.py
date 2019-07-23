# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_8_sequencialmente

a = [1, 2, 3, 4, 5]
b = []

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

for n in a:
    b.append(fatorial(n))

print("Sequencialmente:")
print("Vetor A =", a)
print("Vetor A! =", b)