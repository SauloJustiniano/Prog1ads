# Saulo Justiniano
# Unifip - Patos-PB
# 15 de Março de 2020

'''
6 - Faça um Programa que leia três números e mostre o maior deles.
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Para finalizar, digite mais um número: '))

if num1 == num2 == num3:
    print(f'Você digitou todos os números iguais.')
    exit()

if num1 < num2 and num1 < num3:
    if num2 > num3:
        print(f'O maior número é o {num2}')
    if num2 < num3:
        print(f'O maior número é o {num3}')
if num2 < num1 and num2 < num3:
    if num1 > num3:
        print(f'O maior número é o {num1}')
    if num1 < num3:
        print(f'O maior número é o {num3}')
if num3 < num1 and num3 < num2:
    if num1 > num2:
        print(f' O maior número é o {num1}')
    if num1 < num2:
        print(f'O maior número é o {num2}')
