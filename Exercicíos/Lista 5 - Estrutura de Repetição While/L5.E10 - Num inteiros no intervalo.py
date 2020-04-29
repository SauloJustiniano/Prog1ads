# Saulo Justiniano
# Unifip - Patos-PB
# Dia 21 de Abril de 2020

'''
10 - Faça um programa que receba dois números inteiros e gere os números inteiros 
que estão no intervalo compreendido por eles.
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while num2 <= num1: 
    print('ERRO! O número 2 tem que ser maior que o número 1.')
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
else:
  for n in range(num1+1, num2):
    print(n, end=' ')
