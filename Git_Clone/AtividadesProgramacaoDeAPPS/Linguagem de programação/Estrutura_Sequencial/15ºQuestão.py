#15 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    #   comprar apenas latas de 18 litros;
    #   comprar apenas galões de 3,6 litros;
    #   misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

metros_quadrados = float(input("Digite o tamanho em metros quadrados da áreaque você deseja pintar: "))

litros_necessarios = metros_quadrados / 6

latas_necessarias_opcao1 = math.ceil(litros_necessarios / 18)
preco_total_opcao1 = latas_necessarias_opcao1 * 80

galoes_necessarios_opcao2 = math.ceil(litros_necessarios / 3.6)
preco_total_opcao2 = galoes_necessarios_opcao2 * 25

latas_necessarias_opcao3 = latas_necessarias_mistura = math.floor(litros_necessarios / 18)
galoes_necessarios_mistura = math.ceil((litros_necessarios % 18) / 3.6)

preco_total_opcao3 = (latas_necessarias_mistura + galoes_necessarios_mistura) * 80

print(f"Opção 1 - Latas de 18 litros: {latas_necessarias_opcao1} latas, Preço total: R${preco_total_opcao1:.2f}")
print(f"Opção 2 - Galões de 3,6 litros: {galoes_necessarios_opcao2} galões, Preço total: R${preco_total_opcao2:.2f}")
print(f"Opção 3 - Mistura de latas e galões: {latas_necessarias_opcao3} latas e {galoes_necessarios_mistura} galões, Preço total: R${preco_total_opcao3:.2f}")

