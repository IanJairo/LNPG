texto = []
def remover_especiais(palavra):
    caracteres_especiais = f'."(*$#:'

    for i in caracteres_especiais:
        if (i in palavra):
            palavra = palavra.replace(i, ' ')
            
    palavra = palavra.lower()
    return palavra.split()

while True:
    linha = input().split()
    
    if (linha[0] == '-1'):
        lista = set(texto)
        lista = sorted(lista)

        for l in lista: print(f'{l} {texto.count(l)}')
            
        break
    
    for palavra in linha:
        formatada = remover_especiais(palavra)
        for p in formatada:
            texto.append(p.lower())