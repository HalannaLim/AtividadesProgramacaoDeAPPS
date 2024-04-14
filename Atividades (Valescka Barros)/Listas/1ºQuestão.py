## 1) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
##Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite a idade da pessoa {}°: ".format(i + 1)))
    altura = float(input("Digite a altura da pessoa {}°: ".format(i + 1)))
    idades.append(idade)
    alturas.append(altura)

print("\nA seguir veja as idades e alturas na ordem inversa que você digitou:")
for i in range(4, -1, -1):
    print("A Idade foi: {}, A altura foi: {}".format(idades[i], alturas[i]))