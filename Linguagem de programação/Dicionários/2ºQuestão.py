#2. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

mercado = {}
for i in range(3):
  produto = str(input("Insira o nome do {}° produto: ".format(i+1)))
  preco = float(input("Insira o preço do(a) {}: R$ ".format(produto)))
  mercado[produto] = preco

print("Mercado: \n", mercado)
