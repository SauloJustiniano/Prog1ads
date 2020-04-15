# Saulo Justiniano
# Unifip - Patos-PB
# Dia 05 de Março de 2020.

'''
3. Faça um programa que calcule a média de consumo de combustível de um veículo.
O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos
litros foram gastos no percurso.
'''

km_inicial = int(input("Quantos KM INICIAL: "))
km_final = int(input("Quantos KM FINAL: "))

km_medio = km_final - km_inicial
consumo_litros = km_medio / 10

print(f"Levando em consideração que um carro 10km em 1 litro de combustível, você gastará aproximadamente {consumo_litros:.0f} litros de combustível para percorer {km_medio:.0f}km.")
