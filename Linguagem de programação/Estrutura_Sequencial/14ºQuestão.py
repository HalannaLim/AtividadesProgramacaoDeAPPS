#14 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a qual você deseja pintar: "))

qntdnecessaria = metros_quadrados / 3
latanecessaria = math.ceil(qntdnecessaria / 18)
preco_total = latanecessaria * 80

print(f"A quantidade de latas necessárias para esse procedimento é: {latanecessaria}")
print(f"Preço total: R${preco_total:.2f}")

