entrada = input().split(' ')
errados = 0

qttd_comidas = int(entrada[0])
qttd_quilos = int(entrada[1])

felicidade_geral = 0
peso_geral = 0

for i in range(qttd_comidas):
    comida = input().split(' ')
    felicidade = int(comida[0])
    peso = int(comida[1])

    if peso > qttd_quilos:
        errados += felicidade
    peso_geral += peso
    felicidade_geral += felicidade

if peso_geral > qttd_quilos:
    felicidade_geral = felicidade_geral - errados
if felicidade_geral < 0:
    felicidade_geral = 0

print(felicidade_geral)
