while True:
    solucao = input()
    
    if (solucao == "-1"):
        break
    
    if float(solucao) < 7:
        print("ACIDA")
    elif float(solucao) > 7:
        print("BASICA")
    else:
        print("NEUTRA")
        
