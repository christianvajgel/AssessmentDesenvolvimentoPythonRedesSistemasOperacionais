# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_2

import subprocess

file = input("Entre com o nome do arquivo: ") + ".txt"

subprocess.run(["notepad", file])