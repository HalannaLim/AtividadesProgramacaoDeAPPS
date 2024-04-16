
##Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor = [int(input("Insira o {}º número: ".format(i + 1))) for i in range (10)]

somadosquadrados = (sum(x**2 for x in vetor))

print ("A soma dos quadrados é:", somadosquadrados)
