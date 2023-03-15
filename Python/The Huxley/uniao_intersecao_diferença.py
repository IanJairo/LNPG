def diferenca(a, b):
    diff = [x for x in a if x not in b]
    print(diff)

def intercecao(a, b):
    inter = [x for x in a if x  in b]
    print(inter)

def uniao(a, b):
    lista = b.copy()
    for i in a:
        if (i in b):
            continue
        lista.append(i)
    print(lista)
    
def incluir(entrada):
    lista = []
    for i in range(1, entrada +1):
        valor = input()
        lista.append(valor)
    return lista


entrada_a = int(input())
entrada_b = int(input())

a = incluir(entrada_a)
b = incluir(entrada_b)

uniao(a,b)
intercecao(a, b)
diferenca(a, b)

