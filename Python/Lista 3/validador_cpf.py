def validador(cpf, fatiamento, fator):
    fator_inicial = fator
    soma = 0
    cpf_cortado = cpf[:-fatiamento]
        
    for i in cpf_cortado:
        soma += int(i) * fator
        fator -= 1
    
    calculo = 11 - (soma % 11)
    
    if (calculo == int(cpf[fator_inicial-1])) or (int(cpf[fator_inicial-1]) == 0):
        return True
    else:
        return False  
def valida_cpf():
    etapa = 1
    cpf = input("Digite o CPF: ")
            
    while etapa < 3:
        fatiamento = 2
        fator = 10
        
        if (etapa == 2):
            fatiamento = 1
            fator = 11
        
        isValido = validador(cpf, fatiamento, fator)
        
        if isValido == False:
            print("CPF inválido")
            break
        if (etapa == 2):        
            print("CPF válido")   
            
        etapa += 1

valida_cpf()