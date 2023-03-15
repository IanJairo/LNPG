while True:
    entrada = int(input())
    
    if entrada == 0:
        break
    
    if 1 < entrada <= 11:
        print("Você é uma criança.")
    elif 11 < entrada <= 17:
        print("Você é um adolescente.")
    elif 17 < entrada <= 35:
        print("Você é um jovem.")
    elif 35 < entrada <= 64:
        print("Você é um adulto.")
    elif entrada > 64:
        print("Você é um idoso.")
    else: 
        print("A pessoa ainda não nasceu.")

        