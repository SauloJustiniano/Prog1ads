# Saulo Justiniano
# Unifip - Patos-PB
# Dia 05 de Março de 2020.

'''
1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e
quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível
o usuário obterá com esses valores.
'''

combustivel = float(input("Digite o valor em reais do litro do combustível: R$"))
dinheiro = float(input("Digite o valor em reais do que deseja abastecer: R$"))

total = dinheiro / combustivel

print(f"Você Abastecerá {total:.2f} Litros.")
