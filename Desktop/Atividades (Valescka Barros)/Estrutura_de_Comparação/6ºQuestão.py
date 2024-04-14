#6 - Faça um Programa que leia três números e mostre o maior e o menor deles.

n1= float(input("Insira o primeiro número:"))
n2= float(input("Insira o segundo número:"))
n3= float(input("Insira o terceiro número:"))

maiornum = max(n1,n2,n3)
menornum = min(n1, n2, n3)
print("O maior número é:", maiornum, " e o menor número é: ", menornum)
