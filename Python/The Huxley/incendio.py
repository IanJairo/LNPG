qttd_teste = int(input())
for i in range(qttd_teste):
    sensores = []
    qttd_sprinkler = int(input())
    soma = 0
    for j in range(1, qttd_sprinkler + 1):

        valor = input().split()
        soma += float(valor[1])

        info = {
            'id': int(valor[0]),
            'temp': float(valor[1]),
            'eh_fogo': valor[2]
        }

        sensores.append(info)

    # calcula a media da temperatura
    media_temp = soma / qttd_sprinkler
    print(f'TESTE {i + 1}')
    for s in sensores:
        if s['eh_fogo'] == 'S':
            print(f'{s["id"]}')
        elif s['temp'] >= 40:
            print(f'{s["id"]}')
        else:
            if (s['temp'] > 1.15 * media_temp):
                print(f'{s["id"]}')
