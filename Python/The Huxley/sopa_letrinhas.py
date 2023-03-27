
conjunto = input()

qtdd_checagem = int(input())
certas = 0

for i in range(qtdd_checagem):
    palavra = input()
    letras_palavras = ''
    for j in range(len(palavra)):
        if palavra[j] in conjunto:
            letras_palavras += palavra[j]

    if letras_palavras == palavra:
        certas = certas + 1
        for l in letras_palavras:
            ix = conjunto.index(l)
            conjunto = conjunto[:ix] + conjunto[ix + 1:]

print(f'E possivel formar {certas} palavras com esse conjunto')
