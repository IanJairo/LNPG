"""
Criar um programa para calcular o valor da multa a ser paga de anuidade de uma
associação. A anuidade deve ser paga no mês de janeiro. Por mês, é cobrado 5% de juros
(com juros sobre juros). Por exemplo, uma associação de R$100 paga em janeiro, custa R$
100; em fevereiro, custa R$105; em março, custa R$110,25; e, em dezembro, R$171,03.
"""
taxa = 0.05
anuidade = float(input("Digite o valor da anuidade: "))

for i in range(0, 12):
    multa = anuidade * (1 + taxa) ** i
    print(f'Mês {i+1}: R$ {multa:.2f}')