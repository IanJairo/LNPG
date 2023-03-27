num_jogos = int(input())

for jogador in range(num_jogos):
    tam_senha = int(input())
    senha = input()
    senha_copia = senha
    eh_ganhador = False

    dic = {}

    while eh_ganhador == False:
        try:
            excelentes = 0
            bons = 0
            chute = input()

            excelente_arr = []

            if (len(chute) != len(senha)):
                continue

            if (chute == ('0' * tam_senha)):
                print("entrasse")
                break
            for i in senha:
                dic[i] = senha.count(i)

            if chute == senha:
                print(f"({len(chute)},0)")
                eh_ganhador = True
                continue

            for i in range(len(chute)):
                if (chute[i] == senha[i]):
                    excelentes += 1
                    dic[chute[i]] -= 1
                    excelente_arr.append(i)

            for i in range(len(chute)):
                if (chute[i] in senha) and (chute[i] not in excelente_arr):
                    if dic[chute[i]] > 0:
                        bons += 1
                        dic[chute[i]] -= 1
        except:
            break

        print(f'({excelentes},{bons})')
