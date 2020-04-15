# Saulo Justiniano
# Unifip - Patos-PB
# Dia 06 de Março de 2020.

'''
Questão 5. Faça um programa que calcule o valor a ser pago por uma dívida em atraso.
O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em
atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).
'''

divida = float(input("Digite o valor da Divida: R$"))
dias = int(input("Digite a quantidades de dias em atraso: "))
multa = float(input("Digite o valor da multa por dia de atraso: R$"))

divida_total = float(divida + (dias * multa))

print(f"A Divida Total é de R$ {divida_total:.2f} reais.")
