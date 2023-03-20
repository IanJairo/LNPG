notas_turma = {}
gabarito = ""
maior, menor, soma = 0, 5, 0

def calcular_nota(notas, gabarito):
    nota = 0
    for i in range(len(notas)):
        if notas[i] == gabarito[i]:
            nota += 1
    return nota

while True:
    entrada = input()
    if entrada == "*":
        gabarito = input()
        break

    else: 
        nome, respostas = entrada.split()
        notas_turma[nome] = respostas

for nome, respostas in notas_turma.items():
    nota = calcular_nota(respostas, gabarito)
    soma += nota

    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Media: {soma/len(notas_turma):.2f}')