texto = []
def remover_especiais(palavra):
    caracteres_especiais = '."(*$#:'
    
    for i in range(0, len(palavra)):
        if palavra[i] in caracteres_especiais:
            palavra = palavra.replace(palavra[i], '')
    return palavra

while True:
    linha = input().split()
    
    print('linha', linha)
    
    for palavra in linha:
        formatada = remover_especiais(palavra)
        texto.append(formatada)
    
    print(texto)
        
        
        
        