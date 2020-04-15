# Saulo Justiniano
# Unifip - Patos-PB
# Dia 11 de Março de 2020.

'''
10. Faça um programa que calcula o novo valor do salário de um funcionário.
O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).
'''

salario_atual = float(input("Digite o Salátio Atual: R$"))
reajuste = float(input("Digite quantos % foi o reajuste: %"))

valor_reajuste = float(reajuste * salario_atual) / 100
salario_novo = float(salario_atual + valor_reajuste)

print(f"O salário novo foi de R${salario_atual:.0f} reais para R${salario_novo:.0f} reais.")
