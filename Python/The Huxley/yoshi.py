yoshis = [
    {"raca": "Verde", "velocidade": 80},
    {"raca": "Vermelho", "velocidade": 100},
    {"raca": "Roxo", "velocidade": 120},
    {"raca": "Amarelo", "velocidade": 80},
]

orcamento = float(input())
preco_yoshi = input().split(' ')
beneficio = 0
melhor_yoshi = ""
for i in range(len(preco_yoshi)):

    if (int(preco_yoshi[i]) > orcamento):
        continue

    custo = yoshis[i]["velocidade"] / int(preco_yoshi[i])

    if (custo > beneficio):
        beneficio = custo
        melhor_yoshi = yoshis[i]["raca"]

if melhor_yoshi == "":
    print("Acho que vou a pe :(")
else:
    print(melhor_yoshi)
