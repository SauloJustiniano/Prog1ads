# Saulo Justiniano
# Unifip - Patos-PB
# Dia 21 de Abril de 2020

'''
4 - Suponha que a população de um país A seja da ordem de 80.000 habitantes com 
uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes 
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
número de anos necessários para que a população do país A ultrapasse ou iguale a
população do país B, mantidas as taxas de crescimento.
'''

hab_a = 80000
hab_b = 200000
ano = 0

while hab_a <= hab_b:
  hab_a = hab_a + (hab_a * 0.03)
  hab_b = hab_b + (hab_b * 0.015)
  ano = ano + 1

print(f'Vai precisa de {ano} anos para que a Polulação B ultapasse a Polulação A.')

