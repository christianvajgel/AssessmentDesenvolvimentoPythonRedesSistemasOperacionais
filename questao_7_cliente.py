# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_7_cliente

import socket, pickle, time

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()      
PORT = 12345
orig = (HOST, PORT)
quant = 1024

try:
    for i in range (6):
        msg = "Cliente: Dados memória (total e livre)"
        cliente.sendto(msg.encode('utf-8'), orig)
    
        data, addr = cliente.recvfrom(quant)
        resposta = pickle.loads(data)
        print("Memória total:", str(resposta[0]), "GB")
        print("Memória livre:", str(resposta[1]), "GB")
        hora = time.asctime(time.localtime(time.time()))
        print ("Resposta recebida:", hora)
        print("")
        time.sleep(5)

    msg = "fim"
    cliente.sendto(msg.encode('utf-8'), orig)

except Exception as erro:
    print(str(erro))

cliente.close()
print("Conexão encerrada com o Servidor.")