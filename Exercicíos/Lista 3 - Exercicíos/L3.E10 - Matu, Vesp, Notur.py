# Saulo Justiniano
# Unifip - Patos-PB
# 16 de Março de 2020

'''
10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = input('Qual turno você estudar, Matutino, Vespertino ou Noturno: ')

if turno in ['matutino', 'Matutino', 'MATUTINO', 'm', 'M']:
    print(f'Bom Dia!')
elif turno in ['vespertino', 'Vespertino', 'VESPERTINO', 'v', 'V']:
    print('Boa Tarde!')
elif turno in ['noturno', 'Noturno', 'NOTURNO', 'n', 'N']:
    print(f'Boa Noite!')
else:
    print(f'Valor Inválido!')
