entrada = input()

letras_unicas = set(entrada)
letras = []
for i in letras_unicas:
    obj = {
        "letra": i,
        "frequencia": entrada.count(i)
    }
    letras.append(obj)
    
letras_ordenadas = sorted(letras, key=lambda obj: obj["letra"], reverse=True)

for letra in letras_ordenadas:
    print(letra["letra"] + " " + str(letra["frequencia"]))