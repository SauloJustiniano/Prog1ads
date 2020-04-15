# Saulo Justiniano
# Unifip - Patos-PB
# 15 de Março de 2020

'''
5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

nota1 = float(input('Informe sua primeira Nota: '))
if nota1 > 10:
    print(f'Sua nota foi {nota1:.0f}, a nota máxima vai até 10, Verifique!')
    exit()
nota2 = float(input('Informe sua segunda Nota: '))
if nota2 > 10:
    print(f'Sua nota foi {nota2:.0f}, a nota máxima vai até 10, Verifique!')
    exit()
media = float(nota1 + nota2) / 2

if media >= 7 and media < 10:
    print(f'Aprovado!')
    print(f'Sua média foi {media:.1f}!')
    print(f'Parabéns, você passou de ano.')
elif media < 7:
    print(f'Reprovado!')
    print(f'Sua média foi {media:.1f}!')
    print(f'Estude, você tem uma segunda chance!')
elif media == 10:
    print(f'Aprovado com Distinção!')
    print(f'Sua média foi {media:.1f}!')
    print(f'Parabéns você passou com exelência!.')
