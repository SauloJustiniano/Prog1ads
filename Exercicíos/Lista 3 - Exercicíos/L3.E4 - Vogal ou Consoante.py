# Saulo Justiniano
# Unifip - Patos-PB
# 15 de Março de 2020

'''
4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input('Digite uma letra do alfabeto para saber se é Vogal ou Consoante: ')

if letra in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
    print(f'A letra {letra} é uma Vogal!')
else:
    print(f'A letra {letra} é uma Consoante!')
