# 13 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

numero = int(input("Digite um número inteiro para calcular o fatorial: "))
print(f"{numero}! = {fatorial(numero)}")
