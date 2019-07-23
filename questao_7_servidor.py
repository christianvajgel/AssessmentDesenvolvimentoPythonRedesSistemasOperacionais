# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_7_servidor

import socket, psutil, pickle, time

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()      
PORT = 12345
orig = (HOST, PORT)
quant = 1024

memoria_total = round(psutil.virtual_memory().total/1024**3, 3) 
memoria_livre = round(psutil.virtual_memory().free/1024**3, 3)

servidor.bind(orig)

while True:
    
    (msg, cliente) = servidor.recvfrom(quant)
    print(msg.decode('utf-8'))
    
    if msg.decode('utf-8') == "fim":
        break
    
    else:
        resposta = []
        resposta.append(memoria_total)
        resposta.append(memoria_livre)
            
        bytes_resp = pickle.dumps(resposta)
        servidor.sendto(bytes_resp, cliente)
    print("Resposta enviada para o Cliente:", resposta)
    hora = time.asctime(time.localtime(time.time()))
    print ("Resposta enviada:", hora)
    print("")

servidor.close()
print("Conexão encerrada com o Cliente.")