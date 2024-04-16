#4. Faça um programa, utilizando Dicionários, que:

    #1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .

    #2° Passo: Peça para o usuário inserir um número.

    #3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.

caixa_misteriosa = {}

for i in range(4):
    item = input(f"Insira o {i+1}º item na Caixa Misteriosa: ")
    caixa_misteriosa[i+1](item)

numero = int(input("Digite um número para revelar o que está na Caixa Misteriosa: "))

if 1 <= numero <= len(caixa_misteriosa):
    print(f'O item na posição {numero} é: {caixa_misteriosa[numero-1]}')
else:
    print("Número inválido.")