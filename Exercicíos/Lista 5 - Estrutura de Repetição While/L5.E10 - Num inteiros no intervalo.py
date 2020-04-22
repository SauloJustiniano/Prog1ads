# Saulo Justiniano
# Unifip - Patos-PB
# Dia 21 de Abril de 2020

'''
10 - Faça um programa que receba dois números inteiros e gere os números inteiros 
que estão no intervalo compreendido por eles.
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while num1 < num2 - 1:
  num1 = num1 + 1
  print(num1, end=' ')
