import time
def tela_de_carregamento():
    for _ in range (10):
        time.sleep(0.3)
        print(("★"), end=' ',flush=True)

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

tela_de_carregamento()
print("")
print("")

print("""\033[95m\033[40m_____________________________________________________________________________
|                           Welcome to the Main Menu:                          |
|                                                                              |
|   Digite 1 para ver os números de 1 até 10.                                  |
|   Digite 2 para escolher o intervalo que desejas visualizar.                 |
|   Digite 3 para encerrar o programa.                                         |
|   Digite 4 para imprimir apenas números primos.                              |
|______________________________________________________________________________|""")

while True :
 decisaocrucial = str(input("\nDigite o número correspondente a função que você deseja realizar: "))
 print("\nCarregando...")
 tela_de_carregamento()

 if decisaocrucial == "1":
    for i in range(1,11):
        print(i)

 elif decisaocrucial == "2":
    decisaocrucial2 = int(input("\n\nQual o número que você deseja que o contador estipule como limite: "))
    for i in range(1,decisaocrucial2 + 1):
     print(i)

 elif decisaocrucial == "3":
    print("\n\nEncerrando o programa, aguarde...")
    print("")
    print("")
    tela_de_carregamento()
    exit()

 elif decisaocrucial == "4":
     decisaocrucial3 = int(input("\nQual o número que você deseja que o contador estipule como limite para mostrar os números primos?: "))
     print("\nNúmeros primos até", decisaocrucial3, ":")
     for numero in range(2, decisaocrucial3 + 1):
         if eh_primo(numero):
             print(numero, end=" ")

 else:
    print("\nMensagem invalida, meu fi :(")