# 3° Questão

def verifica_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

num_primo = int(input("Digite um número para verificar se é primo: "))
resultado_primo = verifica_primo(num_primo)
print(f'O número {num_primo} é primo: {resultado_primo}')