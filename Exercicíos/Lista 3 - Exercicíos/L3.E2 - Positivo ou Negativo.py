# Saulo Justiniano
# Unifip - Patos-PB
# 15 de Março de 2020

'''
2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

valor = int(input('Digite um número: '))

if valor > 0:
    print(f'Número Positivo!')
elif valor < 0:
    print(f'Número Negativo!')
elif valor == 0:
    print(f'Número Nulo!')
