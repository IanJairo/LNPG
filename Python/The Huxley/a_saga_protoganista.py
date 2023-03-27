def factorizar(n):
    fatores = 0
    valor = n

    while True:
        if (valor % 3 == 1 or valor % 3 == 2):
            valor = valor - 2
            fatores = fatores + 1
        elif (valor % 3 == 0):
            fatores += valor // 3
            break

    return fatores


entrada = input().split()

dif = int(entrada[1]) - int(entrada[0])

if dif < 0:
    dif = dif * -1

retorno = factorizar(dif)
print(retorno)
