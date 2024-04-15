# 1° Questão
def imprime_padrao(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="   ")
        print()

n_padrao = int(input("Digite um número para imprimirmos o padrão:"))
imprime_padrao(n_padrao)