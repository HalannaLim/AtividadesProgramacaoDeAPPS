#1. Faça um programa que possua um , adicione elementos ao dicionário e os mostre na tela.

dicionario = {}

dicionario['Palavra1'] = "Pudim"
dicionario['Palavra2'] = "Bolo"
dicionario['Palavra3'] = "Torta"

for Chave, Valor in dicionario.items():
  print(f'{Chave}:{Valor}')