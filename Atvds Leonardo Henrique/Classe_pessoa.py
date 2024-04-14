import time

def tela_de_carregamento():

    for _ in range(20):

        time.sleep(0.3)

        print(("★"), end=' ', flush=True)


class Pessoa:

    def __init__(self, nome, idade, altura, peso, genero):

        self.nome = nome

        self.idade = int(idade)

        self.altura = float(altura)

        self.peso = float(peso)

        self.genero = genero

        self.esta_falando = False

        self.esta_andando = False

        self.esta_dormindo = False

        self.esta_comendo = False


    def falar(self, mensagem):

        if not self.esta_dormindo and not self.esta_comendo:

            print(f"        {self.nome} falou: {mensagem}")

            time.sleep(3)

            self.esta_falando = True

        else:

            print(f"        {self.nome} não pode falar enquanto está dormindo ou comendo.")

            time.sleep(3)


    def andar(self, lugar):

        if not self.esta_dormindo:

            time.sleep(3)

            print(f"        {self.nome} está andando para {lugar}.")

            self.esta_andando = True

        else:

            print(f"        {self.nome} não pode andar enquanto está dormindo.")

            time.sleep(3)


    def dormir(self, canto):

        if not self.esta_falando and not self.esta_comendo and not self.esta_andando:

            time.sleep(3)

            print(f"        {self.nome} está dormindo na/o {canto}.")

            self.esta_dormindo = True

        else:

            print(f"        {self.nome} não pode dormir enquanto está falando, comendo ou andando.")

            time.sleep(3)


    def comer(self, comida):

        if not self.esta_falando and not self.esta_dormindo:

            time.sleep(3)

            print(f"        {self.nome} está comendo {comida}.")

            self.esta_comendo = True

        else:

            print(f"        {self.nome} não pode comer enquanto está falando ou dormindo.")

            time.sleep(3)


    def parar_falar(self):

        self.esta_falando = False

        time.sleep(2)


    def parar_andar(self):

        self.esta_andando = False

        time.sleep(2)


    def parar_dormir(self):

        self.esta_dormindo = False

        time.sleep(2)


    def parar_comer(self):

        self.esta_comendo = False

        time.sleep(2)


    def menu(self):

        while True:

            time.sleep(3)

            print("""\n            ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

            ★                                   Bem vindo ao Menu                                     ★

            ★                                                                                         ★

            ★  1. Falar                                                    6. Parar de Comer          ★

            ★  2. Comer                                                    7. Parar de Andar          ★

            ★  3. Andar                                                    8. Parar de Dormir         ★

            ★  4. Dormir                                                   9. Fechar o Programa       ★

            ★  5. Parar de Falar                                                                      ★              

            ★                                                                                         ★

            ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★""")

            opcao = input("\n        Escolha uma opção do menu: ")


            if opcao == "1":

                mensagem = input("        Digite a mensagem que deseja falar: ")

                self.falar(mensagem)

            elif opcao == "2":

                comida = input("        O que você quer comer? : ")

                self.comer(comida)

            elif opcao == "3":

                lugar = input("        Para onde você irá andar? : ")

                self.andar(lugar)

            elif opcao == "4":

                canto = input("        Onde você irá dormir? : ")

                self.dormir(canto)

            elif opcao == "5":

                self.parar_falar()

            elif opcao == "6":

                self.parar_comer()

            elif opcao == "7":

                self.parar_andar()

            elif opcao == "8":

                self.parar_dormir()

            elif opcao == "9":

                print("\n        Encerrando o programa, aguarde...")

                tela_de_carregamento()

                exit()

            else:

                print("\n Opção inválida. Por favor, escolha novamente.")


nome = input("Digite seu nome: ")

idade = input("Digite sua idade: ")

altura = input("Digite sua altura: ")

peso = input("Digite seu peso: ")

genero = input("Digite seu gênero: ")


pessoa = Pessoa(nome, idade, altura, peso, genero)


print(f"\nBem-vindo, {nome}!")


time.sleep(2)

pessoa.menu()