def achar_manuela(passos):
    matriz = [[0 for i in range(4)] for j in range(4)]

    x = 0
    y = 0

    for passo in passos:
        if passo == 'c':
            y = max(0, y - 1)
        elif passo == 'b':
            y = min(3, y + 1)
        elif passo == 'e':
            x = max(0, x - 1)
        elif passo == 'd':
            x = min(3, x + 1)

        matriz[y][x] += 1

    max_count = -1
    localizacao_manu = None
    for i in range(4):
        for j in range(4):
            if matriz[i][j] > max_count:
                max_count = matriz[i][j]
                localizacao_manu = (j, i)

    return f"Coordenada X:{localizacao_manu[0]}, Y:{localizacao_manu[1]}"


passos = input().split()
print(achar_manuela(passos))
