#12 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável  (peso de peixes) e calcule o excesso. Gravar na variável  a quantidade de quilos além do limite e na variável  o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Insira o peso:" ))
if peso > 50:
  x = (peso - 50)*4
print("A multa que deverá ser paga é: R$ ", x)
