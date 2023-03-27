entrada = input().split(' ')
n = int(entrada[0])
m = int(entrada[1])
urb = []
indenizacoes = 0

for i in range(n):
    quadras = input().split(' ')
    urb.append(quadras)

for i in range(m):
    somatorio = 0
    for j in range(n):
        somatorio += int(urb[j][i])

    if i == 0:
        indenizacoes = somatorio
    else:
        if somatorio < indenizacoes:
            indenizacoes = somatorio

print(indenizacoes)
