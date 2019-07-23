# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_3

import os, subprocess, psutil, operator

path = input("Entre com o caminho absoluto do diretório: ").strip()

workspace = os.getcwd()
diretorio = os.listdir(path)
dicionario = {}

for arquivo in diretorio:
    if os.path.isfile(os.path.join(path,arquivo)):
        tamanho = round(os.stat(os.path.join(path,arquivo)).st_size / 1024) 
        dicionario [arquivo] = tamanho

dicionario_sortido = sorted(dicionario.items(), key = operator.itemgetter(1), reverse = True)

try:
    nome = "arquivos.txt"
    arq = open(nome, "w")
    for i in dicionario_sortido:
        arq.write("Nome: ")
        arq.write(str(i[0]))
        arq.write(" | Tamanho: ")
        arq.write(str(i[1]))
        arq.write(" byte(s)\n")
    arq.close()
    
    print("Arquivo de texto '", nome, "' salvo com sucesso em:", workspace)

except Exception as erro:
    print(str(erro))