'''

Criar um programa para identificar o valor a ser pago por um plano de saúde dada a idade
do conveniado considerando que todos pagam R$ 100 mais um adicional conforme a seguinte
tabela:
1) crianças com menos de 10 anos pagam R$80;
2) conveniados com idade entre 10 e 30 anos pagam R$50;
3) conveniados com idade entre 30 e 60 anos pagam R$ 95; e
4) conveniados com mais de 60 anos pagam R$130.

'''

idade = int(input("Digite a idade do paciente: "))
taxa_inicial = 100
mensalidade = 0

if idade <10:
    mensalidade = taxa_inicial + 80
elif idade >= 10 and idade <= 30:
    mensalidade = taxa_inicial + 50
elif idade > 30 and idade <= 60:
    mensalidade = taxa_inicial + 95
else:
    mensalidade = taxa_inicial + 130

print("O valor da mensalidade é de R$ %.2f" %mensalidade)