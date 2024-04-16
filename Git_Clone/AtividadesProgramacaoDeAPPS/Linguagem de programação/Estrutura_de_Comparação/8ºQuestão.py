#8 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1= float(input("Insira o primeiro número:"))
num2= float(input("Insira o segundo número"))
num3= float(input("Insira o terceiro número"))

numeros = [num1, num2, num3]
numeros.sort(reverse=True)

print("Os números em ordem decrescente são:",numeros)

