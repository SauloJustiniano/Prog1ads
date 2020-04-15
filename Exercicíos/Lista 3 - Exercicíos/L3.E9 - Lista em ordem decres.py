# Saulo Justiniano
# Unifip - Patos-PB
# 16 de Março de 2020

'''
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
if num1 == num2:
    print(f'Você não pode colocar 2 números Iguais.')
    exit()
num3 = int(input('Informe mais um número: '))
if num3 == num1 or num3 == num2:
    print(f'Você não pode colocar 2 números Iguais.')
    exit()

lista = num1, num2, num3
lista_nova = sorted(lista, reverse=True)
print('Os números em ordem decrescente:', str(lista_nova).strip('[]') + '.')
