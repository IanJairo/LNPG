# inicialização das variáveis
menor_ipca = float('inf')
maior_ipca = float('-inf')
soma_ipca = 0
qtd_ipca = 0
mes_menor = ''
mes_maior = ''

# leitura dos dados de entrada
while True:
    entrada = input().strip()
    if entrada == '*':
        break
    ano_mes, ipca = entrada.split()
    ipca = float(ipca.replace(',', '.')) # converte o número para float usando o '.' como separador decimal
    # atualiza os valores mínimo e máximo
    if ipca < menor_ipca:
        menor_ipca = ipca
        mes_menor = ano_mes
    if ipca > maior_ipca:
        maior_ipca = ipca
        mes_maior = ano_mes
    # atualiza a soma e quantidade de IPCA's
    soma_ipca += ipca
    qtd_ipca += 1

# cálculo da média
media_ipca = soma_ipca / qtd_ipca

# saída dos resultados
print(f'{menor_ipca:.2f} ({mes_menor})')
print(f'{maior_ipca:.2f} ({mes_maior})')
print(f'{media_ipca:.2f}')
