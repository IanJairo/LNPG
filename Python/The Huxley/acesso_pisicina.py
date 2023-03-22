max_criancas = int(input())

total_adultos = 0
total_criancas = 0
total_residente = 0 
def mensagem(tipo_permissao, adultos, criancas, excesso):
    if tipo_permissao == 1:
        print("Acesso permitido!")
    elif tipo_permissao == 2:
        print("Acesso permitido devido a presenca de convidado(s).")
    else:
        print("Capacidade maxima de criancas atingida/excedida.")
        print(f"Tem {excesso} crianca(s) a mais que as {max_criancas} permitidas.")        
        

    print(f"Adultos na piscina: {adultos}")
    print(f"Criancas na piscina: {criancas}")
    print("***")

while True: 
    qttd_adultos = int(input())
    
    if qttd_adultos < 0:
        break
    
    qttd_criancas_residentes = int(input())
    qttd_criancas_convidadas = int(input())
    
    adicao = qttd_criancas_residentes + total_criancas + qttd_criancas_convidadas
    
    if (adicao <= max_criancas):
        total_adultos = total_adultos + qttd_adultos
        total_criancas = adicao
        total_residente = total_criancas
        mensagem(1, total_adultos, total_criancas, 0)
    elif (adicao > max_criancas and qttd_criancas_convidadas != 0):
        total_adultos = total_adultos + qttd_adultos
        total_criancas = adicao
        
        mensagem(2, total_adultos, total_criancas, 0)
    else: 
        total_residente = total_residente + qttd_criancas_residentes
                
        mensagem(3, total_adultos, total_criancas,  qttd_criancas_residentes)
        
        
                
    
    