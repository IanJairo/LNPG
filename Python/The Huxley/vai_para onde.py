orcamento = 300
longe = 0
destino = ""
while True:
    cidade = input()
    
    if (cidade.upper() == "FIM"):
        break  
    
    distancia = int(input())
    valor = float(input())
    
    if  (valor*2) > orcamento:  
        continue     
    
    if distancia > longe:
        longe = distancia
        destino = cidade           
     
if not destino:
    destino = "SEM DESTINO"   
print(destino.upper())     