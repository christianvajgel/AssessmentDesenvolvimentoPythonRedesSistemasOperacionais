# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_6_cliente

import os, subprocess, socket, pickle

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname() 
PORT = 12345
HP = (HOST, PORT)
quant = 4096

try:
    cliente.connect(HP)
    req = " "
    cliente.send(req.encode('utf-8'))
    
    while True:
        print("")
        req = input("Digite o caminho absoluto do diretório: ")
        cliente.send(req.encode('utf-8'))
        
        bytes_resp = cliente.recv(quant)
        resposta = pickle.loads(bytes_resp)
        print("")
        print("Arquivo(s) presente(s) no diretório escolhido:")
        for arq in resposta:
            print("\r", "-", str(arq), "\r")
        print("")
        break
            
except Exception as erro:
    print(str(erro))

cliente.close()
input("Conexão encerrada. Para sair pressione qualquer tecla...")