# Saulo Justiniano
# Unifip - Patos-PB
# Dia 21 de Abril de 2020


'''
5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de
crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

hab_a = float(input('Informe a quantidade de habitantes da população A: '))
hab_b = float(input('Informe a quantidade de habitantes da população B: '))

cres_a = float(input('Informe a taxa anual de crescimento da polulação A: '))
cres_b = float(input('Informe a taxa anual de crescimento da população B: '))

cres_a = cres_a / 100
cres_b = cres_b / 100

ano = 0

while hab_a <= hab_b:
  hab_a = hab_a + (hab_a * cres_a)
  hab_b = hab_b + (hab_b * cres_b)
  ano = ano + 1

print(f'Vai precisa de {ano} anos para que a Polulação B ultapasse a Polulação A.')

