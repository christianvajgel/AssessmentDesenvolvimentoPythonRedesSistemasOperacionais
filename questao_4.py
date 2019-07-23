# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_4

nome = input("Digite o nome do arquivo (questao_4_arquivo_texto.txt): ")

try:
    arq = open(nome, "r")  
    texto = arq.read()
    reverso = texto[::-1]  
    arq.close()
    
    print("")
    print("Conteúdo original:")
    print(">", texto)
    print("")
    print("Conteúdo invertido:")
    print(">>", reverso)
    
except:
    print("O arquivo não foi encontrado.")