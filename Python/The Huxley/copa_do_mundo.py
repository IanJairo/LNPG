equipes = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M',  'N', 'O', 'P']

rodadas = [8, 4, 2, 1]

for r in rodadas:
    ganhadores = []
    for i in range(0, r):
        resultado_jogo = input().split(' ')

        if resultado_jogo[0] > resultado_jogo[1]:
            ganhadores.append(equipes[i*2])
        else:
            ganhadores.append(equipes[i*2+1])

    equipes = ganhadores


print(equipes[0])
