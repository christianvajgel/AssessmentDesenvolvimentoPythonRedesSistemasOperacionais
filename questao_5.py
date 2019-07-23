# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_5

import numpy

arq_A = "a.txt"
arq_B = "b.txt"

lista_A = []
lista_B = []
resultado = []

def imprimir():
    value = (lista_A[i] + lista_B[i])
    print("Posição Lista A","[", i, "]", "=", lista_A[i])
    print("Posição Lista B","[", i, "]", "=", lista_B[i])
    print("A","[", i, "]", "+", "B","[", i, "] =", value)
    resultado.append(value)
    print("")

try:
    arqA = open(arq_A, "r")
    
    dados = numpy.genfromtxt(arq_A, delimiter = " ")

    for i in dados:
        lista_A.append(int(i))
        
    arqA.close()

except Exception as e:
    print("Arquivo não existe.")
    
try:
    arqB = open(arq_B, "r")
    
    dados = numpy.genfromtxt(arq_B, delimiter = " ")

    for i in dados:
        lista_B.append(int(i))
    
    arqB.close()

except Exception as e:
    print("Arquivo não existe.")

print("Arquivo A:", lista_A)
print("Arquivo B:", lista_B)
print("")

a = int(len(lista_A) - 1)
b = int(len(lista_B) - 1)
i = 0

while True:
    
    try:
        if (a < i) & (b >= i):
            lista_A.append(0)
            imprimir()
            
        elif (a >= i) & (b < i):
            lista_B.append(0)
            imprimir()
        
        elif (a >= i) & (b >= i):
            imprimir()
        
        elif (a < i) & (b < i):
            print("Lista A[i] + B[i] = ", resultado)
            break
        
        i = i + 1

    except IndexError as e:
        print(str(e))

        break