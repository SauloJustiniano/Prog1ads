# Saulo Justiniano
# Unifip - Patos-PB
# Dia 21 de Abril de 2020

'''
7 - Faça um programa que leia 5 números e informe o maior número.
'''

larger = -99999999
cont = 1

while cont <= 5:
  number = int(input('Digite um número: '))

  if number > larger:
    larger = number

  cont = cont + 1

print(f'O maior número é {larger}')
