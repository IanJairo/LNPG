qttd_clubes = int(input())

ranking = {}

for i in range(qttd_clubes):
    pontos = 0
    nome_clube = input()
    entrada = input().split(' ')
    valor_mercado = float(entrada[0])
    quantidade_jogadores = int(entrada[1])
    quantidade_titulos = int(entrada[2])
    tem_neymar = input().lower()
    eh_flamengo_2019 = input().lower()

    if tem_neymar == 'sim':
        pontos += 10000
    if eh_flamengo_2019 == 'sim':
        pontos += 20000

    pontos += valor_mercado + \
        (quantidade_jogadores * 100) + (quantidade_titulos * 2000)
    ranking[nome_clube] = pontos

sorted_ranking = dict(
    sorted(
        ranking.items(),
        key=lambda item: item[1], reverse=True
    ))

for i in sorted_ranking:
    print(f'{i} {sorted_ranking[i]:.2f}')
