# Saulo Justiniano
# Unifip - Patos-PB
# Dia 17 de Abril de 2020

'''
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
cont = 1

while cont <= 5:
  number = int(input('Digite um número: '))

  soma = number * 5
  media = soma / 5

  cont = cont + 1

print(f'Soma: {soma}')
print(f'Média: {media}')

