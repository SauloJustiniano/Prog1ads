# Saulo Justiniano
# Unifip - Patos-PB
# Dia 15 de Abril de 2020

'''
3 - Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
  nome = input('Nome: ')
  if len(nome) >= 4:
    print('Validado!')
    break
  else:
    continue
  
while True:
  idade = int(input('Idade: '))
  if idade > 0 and idade <= 150:
    print('Validado!')
    break
  else:
    continue

while True:
  salario = float(input('Salário: '))
  if salario > 0:
    print('Validado!')
    break
  else:
    continue

while True:
  sexo = input('Sexo: ')
  if sexo in ['f', 'feminino', 'm', 'masculino']:
    print('Validado!')
    break
  else:
    continue

while True:
  estado_civil = input('Estado Civil: ')
  if estado_civil in ['s', 'solteiro', 'c', 'casado', 'v', 'viúvo', 'viúva', 'd', 'divorciado']:
    print('Validado!')
    break
  else:
    continue

print('Cadastro Confirmado')