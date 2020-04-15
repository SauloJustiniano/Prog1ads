# Saulo Justiniano
# Unifip - Patos-PB
# 15 de Março de 2020

'''
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

letra = input('Qual seu sexo? Digite F ou M para saber: ')

if letra in ['f', 'F']:
    print(f'Sexo Feminino!')
elif letra in ['m', 'M']:
    print(f'Sexo Masculino!')
else:
    print('"Sexo Inválido.')
