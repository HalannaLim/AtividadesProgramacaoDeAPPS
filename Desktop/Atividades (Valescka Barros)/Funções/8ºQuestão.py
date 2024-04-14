# 8° Questão

def imprime_tabuada(numero):
    if not isinstance(numero, int):
        print("Digite um número para calcularmos a tabuada.")
        return

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero_tabuada = int(input("Digite um número para calcularmos a tabuada:"))
imprime_tabuada(numero_tabuada)