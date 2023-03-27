doce_disponivel = int(input())
k = []
for i in range(3):
    valor = int(input())
    k.append(valor)

result = 0

for i in range(len(k)):
    dif = doce_disponivel - min(k)
    ix = k.index(min(k))
    k[ix] = min(k) * 2

    if dif >= 0:
        doce_disponivel = dif
        result += 1
print(result)
