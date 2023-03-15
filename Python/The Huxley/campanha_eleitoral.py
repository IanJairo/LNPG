anuncios_geral = {
    'INTERNET': 3000,
    'REVISTA': 750,
    'OUTDOOR': 1500
}
radio = {'AM': 300, 'FM': 500}
tv = {'REGULAR': 1200, 'NOBRE': 2000}

valores = []
while True:
    entrada = input().split()
    total_valor_candidato = 0
    
    if entrada[0].upper() == "FIM":
        break
    
    for i in range(1, int(entrada[1]) +1):
        tipo_anuncio = input().upper()
        
        if tipo_anuncio == "RADIO":
            tipo_radio = input().upper()
            total_valor_candidato += radio[tipo_radio]
        
        elif tipo_anuncio == "TV":
            horario = int(input())
            if horario > 20:
                total_valor_candidato += tv['NOBRE']
            else:
                total_valor_candidato += tv['REGULAR']
                
        else:
            total_valor_candidato += anuncios_geral[tipo_anuncio]
    
    print(f'{entrada[0]}: {total_valor_candidato:.2f}')         