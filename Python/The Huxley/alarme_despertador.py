def time_to_seconds(h, m):
    if h == 0:
        h = 24

    return (h * 3600 + m * 60)


while True:
    try:
        entrada = input().split(' ')

        if entrada.count("0") == 4:
            break

        h1 = time_to_seconds(int(entrada[0]), int(entrada[1]))
        h2 = time_to_seconds(int(entrada[2]), int(entrada[3]))

        if h2 < h1:
            h = time_to_seconds(24, 0)

            resul = (h2 + h) - h1
        else:
            resul = h2 - h1

        print(resul // 60)
    except:
        break
