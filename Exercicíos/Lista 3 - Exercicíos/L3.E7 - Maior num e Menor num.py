# Saulo Justiniano
# Unifip - Patos-PB
# 15 de Março de 2020

'''
7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 == num2:
    print(f'Você colocou dois números Iguais!')
    exit()
num3 = int(input('Digite mais um número: '))
if num3 == num1 or num3 == num2:
    print(f'Você colocou dois números Iguais!')
    exit()
elif num1 == num2 == num3:
    print(f'Você colocou 3 números Iguais!')
    exit()
    
if num1 < num2 and num1 < num3:
    if num2 > num3:
        print(f'O maior número foi o {num2}')
        print(f'O menor número foi o {num1}')
    if num2 < num3:
        print(f'O maior número foi o {num3}')
        print(f'O menor número foi o {num1}')
if num2 < num1 and num2 < num3:
    if num1 > num3:
        print(f'O maior número foi o {num1}')
        print(f'O menor número foi o {num2}')
    if num1 < num3:
        print(f'O maior número foi o {num3}')
        print(f'O menor número foi o {num2}')
if num3 < num1 and num3 < num2:
    if num1 > num2:
        print(f'O maior número foi o {num1}')
        print(f'O menor número foi o {num3}')
    if num1 < num2:
        print(f'O maior número foi o {num2}')
        print(f'O menor número foi o {num3}')
