class Animal:
    def _init_(self, nome, idade, porte, peso, genero, quantidade_patas, especie, deslocamento, alimentacao, cor):
        self.nome = nome
        self.idade = int(idade)
        self.porte = str(porte)
        self.peso = str(peso)
        self.genero = str(genero)
        self.quantidade_patas = int(quantidade_patas)
        self.especie = str(especie)
        self.deslocamento = str(deslocamento)
        self.alimentacao = str(alimentacao)
        self.cor = str(cor)

    def abanda_rabo(self):
        print(f"{self.nome} está abanando o rabinho!")

    def mimir(self):
        print(f"{self.nome} está dormindo!")

    def barulho(self):
        print(f"{self.nome} está fazendo barulho!")

    def comendo(self):
        print(f"{self.nome} está comendo!")


    def info(self):
        print("\n Informações do animal:")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"porte: {self.porte}")
        print(f"Peso: {self.peso}")
        print(f"Gênero: {self.genero}")
        print(f"Quantidade de patas: {self.quantidade_patas}")
        print(f"Espécie: {self.especie}")
        print(f"Deslocamento: {self.deslocamento}")
        print(f"Alimentação: {self.alimentacao}")
        print(f"Cor: {self.cor}")

class Cachorro(Animal):
    def __init__(self, nome, idade, porte, peso, genero, quantidade_patas, especie, deslocamento, alimentacao, raca, cor):
        super()._init_(nome, idade, porte, peso, genero, quantidade_patas, especie, deslocamento, alimentacao, cor)
        self.raca = raca

    def abanda_rabo(self):
        print(f"\n{self.nome} está abanando o rabinho!")

    def mimir(self):
        print(f"\n{self.nome} está dormindo!")

    def barulho(self):
        print(f"\n{self.nome} está latindo!")

    def comendo(self):
        print(f"\n{self.nome} está comendo sua ração!")

    def brincando(self):
        print(f"\n{self.nome} está brincando com seu dono!")

    def passear(self):
        print(f"\n{self.nome} quer passear!, leve ele para rua")

    def emitir_som(self):
        print("\nAuAu Humano 🐶🐶🐶!")

nome = input("Digite o nome do seu animal: ")
idade = input("Digite a idade do seu animal: ")
porte = input("Digite o porte do seu animal: ")
peso = input("Digite o peso do seu animal: ")
genero = input("Digite o gênero do seu animal: ")
quantidade_patas = input("Digite a quantidade de patas do seu animal: ")
especie = input("Digite a espécie do seu animal: ")
deslocamento = input("Digite o tipo de deslocamento do seu animal (Anda, Voa e nada): ")
alimentacao = input("Digite o tipo de alimentação do seu animal (Onívoro, Carnívoro e Herbívoro): ")
raca = input("Digite a raça do seu animal: ")
cor = input("Digite a cor do seu animal:")

cachorro = Cachorro(nome, idade, porte, peso, genero, quantidade_patas, especie, deslocamento, alimentacao, raca, cor)

cachorro.info()

cachorro.emitir_som()
cachorro.abanda_rabo()
cachorro.mimir()
cachorro.barulho()
cachorro.brincando()
cachorro.mimir()
cachorro.comendo()