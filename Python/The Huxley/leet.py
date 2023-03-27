qttd_trocas = 0
invert = []


caracteres = {
    'A': '@',
    'E': '3',
    'I': '1',
    'O': '0',
    'T': '7',
    'S': '5'
}


def tem_numeros(string):
    return any(char.isdigit() for char in string)


def efetua(palavra):
    if len(eh_errado) > 0:
        return eh_errado
    return True


entrada = input().split()
eh_errado = ""

if (entrada == []):
    eh_errado = "vazia"

for palavra in entrada:
    if (tem_numeros(palavra)):
        eh_errado = "numeros"
        qttd_trocas = 0
        break

    t = ''
    for letra in palavra:
        if letra.upper() in caracteres:
            t += caracteres[letra.upper()]
            qttd_trocas = qttd_trocas + 1
            continue
        t = t + letra

    invert.append(t)

if len(eh_errado) == 0:
    print((' '.join(invert))[::-1])
    print(qttd_trocas)
else:
    print(eh_errado)
    print(qttd_trocas)
