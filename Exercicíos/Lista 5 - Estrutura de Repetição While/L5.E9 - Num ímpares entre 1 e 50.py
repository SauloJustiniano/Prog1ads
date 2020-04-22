# Saulo Justiniano
# Unifip - Patos-PB
# Dia 21 de Abril de 2020

'''
9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''

num = 0

while num >= 0 and num <= 50:
  num = num + 1
  if num >= 0 and num <= 50:
    if (num % 2) != 0:
      print(num, end=' ')

