entrada = int(input())
posicao = 1
jogadas = 0


while posicao != entrada:
    for i in range(1, 7):
        posicao += i
        jogadas += 1

        if (posicao > entrada):
            posicao = posicao % entrada
        if posicao == entrada:
            print(jogadas)
            break
