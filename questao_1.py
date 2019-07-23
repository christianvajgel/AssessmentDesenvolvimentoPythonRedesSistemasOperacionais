# ASSESSMENT - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 04/04/2019 - Thonny IDE - Conceito DML (10/10).
# questao_1

import psutil

for proc in psutil.process_iter():
    if psutil.pid_exists(proc.pid):
        processID = proc.pid
            
        try:
            processName = proc.name() 
            processCpuPercent = proc.cpu_percent(interval = 2.0) 
            processMemoryPercent = round(proc.memory_percent("rss"),2)
            
            print("Nome do processo:", processName, " | PID:", processID, " | CPU (%):", processCpuPercent, " | Memória (%):", processMemoryPercent)
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
    else:
        print("Processo não existe mais.")