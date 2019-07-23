# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_6_servidor

import os, subprocess, socket, pickle

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname() 
PORT = 12345
HP = (HOST, PORT)
quant = 4096

servidor.bind(HP)
servidor.listen()
print("Servidor:", HOST, "esperando na porta", PORT, "*Beep... *beep... *beep!")

(cliente, addr) = servidor.accept()
print("Máquina do cliente conectada:", addr)

def arquivo():
    
    lista = []
    diretorio = os.listdir(path)

    for arq in diretorio:
        if os.path.isfile(os.path.join(path,arq)):
            lista.append(arq)
            
    return lista

while True:
    req = cliente.recv(quant)
    
    if req.decode('utf-8') == " ":
        print("Conexão bem-sucedida.")    
        
    if req.decode('utf-8') != " ":
        path = req.decode('utf-8')
        bytes_resp = pickle.dumps(arquivo())
        cliente.send(bytes_resp)
        break

cliente.close()
servidor.close()

input("Conexão encerrada. Pressione qualquer tecla para sair...")