# Saulo Justiniano
# Unifip - Patos-PB
# Dia 06 de Março de 2020.

'''
Questão 9. Escreva um programa que converte valores de polegadas em centímetros utilizando a
seguinte fórmula para conversão: 1 polegada = 2,54 cm;
'''

polegadas = float(input("Digite quantas polegadas: "))

valor_polegadas = float(polegadas * 2.54)

print(f"O Valor {polegadas} em centímetros de uma polegadas é {valor_polegadas:.2f}cm")
