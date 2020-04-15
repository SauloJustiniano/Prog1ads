# Saulo Justiniano
# Unifip - Patos-PB
# 16 de Março de 2020

'''
8 - Faça um programa que pergunte o preço de três produtos e informe qual produto
 você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

pre1 = float(input('Informe o valor de um produto: R$'))
pre2 = float(input('Informe o valor de outro pruduto: R$'))
pre3 = float(input('Informe o valor de mais um pruduto: R$'))

if pre1 == pre2 and pre1 < pre3:
    print(f'Você pode comprar o Produto 1 ou Produto 2, pois ambos custam {pre1:.2f}.')
    exit()
if pre1 == pre3 and pre1 < pre2:
    print(f'Você pode comprar o Produto 1 ou Produto 3, pois ambos custam {pre1:.2f}.')
    exit()
if pre2 == pre3 and pre2 < pre1:
    print(f'Você pode comprar o Produto 2 ou Produto 3, pois ambos custam {pre2:.2f}.')
    exit()
if pre1 == pre2 == pre3:
    print(f'Você pode comprar o Produto 1 , 2 , 3. pois ambos custam {pre1:.2f}')
    exit()

if pre1 < pre2 and pre1 < pre3: 
    print(f'Você deve comprar o 1 pruduto, ele é o mas barato e custa {pre1:.2f}')
elif pre2 < pre1 and pre2 < pre3:
    print(f'Você deve comprar o 2 pruduto, ele é o mas barato e custa {pre2:.2f}')
elif pre3 < pre1 and pre3 < pre2:
    print(f'Você deve comprar o 3 pruduto, ele é o mas barato e custa {pre3:.2f}')
