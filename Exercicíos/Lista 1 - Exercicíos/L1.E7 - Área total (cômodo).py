# Saulo Justiniano
# Unifip - Patos-PB
# Dia 06 de Março de 2020.

'''
Questão 7. Faça um programa que calcule a área total (m²) de uma casa com 4 cômodos.
O usuário deve inserir a largura e comprimento de cada um dos cômodos, calcular a área
individual de cada um e por fim exibir a área total da casa.
'''

largura01 = float(input("Digite a largura do Cômodo 01: "))
comprimento01 = float(input("Digite a Largura do Cômodo 01: "))

largura02 = float(input("Digite a largura do Cômodo 02: "))
comprimento02 = float(input("Digite a Largura do Cômodo 02: "))

largura03 = float(input("Digite a largura do Cômodo 03: "))
comprimento03 = float(input("Digite a Largura do Cômodo 03: "))

largura04 = float(input("Digite a largura do Cômodo 04: "))
comprimento04 = float(input("Digite a Largura do Cômodo 04: "))

area_total = float((largura01 * comprimento01)+(largura02 * comprimento02)+(largura03 * comprimento03)+(largura04 * comprimento04))

print(f"A Área da casa é {area_total:.2f}m²")
