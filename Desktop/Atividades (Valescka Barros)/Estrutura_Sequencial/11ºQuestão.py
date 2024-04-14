#11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    #.O produto do dobro do primeiro com metade do segundo .
    #.A soma do triplo do primeiro com o terceiro.
    #.O terceiro elevado ao cubo.

Inteiroum = int(input("Insira um número inteiro:" ))
Inteirodois = int(input("um número inteiro:" ))
Realum = float(input("Insira um número real:" ))
Questaoum = (Inteiroum * 2) * (Inteirodois/2)
Questaodois = (Inteiroum * 3) + Realum
Questaotres = Realum ** 3

print("O produto do dobro do primeiro com metade do segundo: ", Questaoum)
print("A soma do triplo do primeiro com o terceiro: ", Questaodois)
print("O terceiro elevado ao cubo:", Questaotres)
