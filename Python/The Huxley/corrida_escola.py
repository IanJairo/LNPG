info_corrida = list(map(int, input().split())) 
melhor_corredor = 0
ganhador = 0

for i in range(1, info_corrida[0] + 1):
    info_corredor =list(map(int, input().split())) 
    
    if i == 1:
        melhor_corredor = sum(info_corredor)
        ganhador = i
    
    if sum(info_corredor) < melhor_corredor:
        melhor_corredor = sum(info_corredor)
        ganhador = i
        
print(ganhador)