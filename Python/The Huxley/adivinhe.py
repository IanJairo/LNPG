num_jogos = int(input())

for jogador in range(num_jogos):
    tam_senha = int(input())
    
    while tam_senha < 1 or tam_senha > 7:
        tam_senha = int(input())
    
    senha = input()
    while len(senha) != tam_senha:
        
        senha = input()
        
    eh_ganhador = False
    
    while eh_ganhador == False:
        excelentes = 0
        bons = 0
        chute = input()       
        
        if(len(chute) != tam_senha):
            chute = input()

        if chute == senha:
            print(f"({len(chute)},0)")
            eh_ganhador = True
            continue

        for i in range(tam_senha):
            if chute[i] == senha[i]:
                excelentes = excelentes + 1
            elif chute[i] in senha:
                bons = bons + 1

        print(f'({excelentes},{bons})')
