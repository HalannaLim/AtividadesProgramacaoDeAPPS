#9 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = float(input("Digite o número para calcularmos a potência: "))
expoente = int(input("Digite o expoente para calcularmos a potência: "))

resultado = 1
for _ in range(expoente):
    resultado *= base

print("{} elevado a {} é igual a {}".format(base, expoente, resultado))
