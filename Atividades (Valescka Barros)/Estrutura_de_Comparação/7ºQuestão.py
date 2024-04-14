#7 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1= float(input("Insira o preço do primeiro produto: R$"))
produto2= float(input("Insira o preço do segundo produto: R$"))
produto3= float(input("Insira o preço do terceiro produto: R$"))

maisbarato = min(produto1, produto2, produto3)
print("O produto que você deve comprar é o produto que custa: R$",maisbarato)
