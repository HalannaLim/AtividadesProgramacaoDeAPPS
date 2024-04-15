# Crie uma classe que modele uma pessoa:

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            # A cada ano que a pessoa envelhece, ela cresce 0,5 cm
            self.crescer(0.5 * anos)

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_ganha):
        self.altura += altura_ganha

    def _str_(self):
        return f"{self.nome}, {self.idade} anos, {self.peso} kg, {self.altura} cm"


# Exemplo de uso da classe
pessoa1 = Pessoa(nome = "Ana", idade=18, peso=60, altura=160)
print("A idade antes:", pessoa1.idade)
print("O peso antes:", pessoa1.peso)
print("A altura antes:", pessoa1.altura)

pessoa1.envelhecer(3)
pessoa1.engordar(5)
pessoa1.crescer(2)

print("\nA idade depois:", pessoa1.idade)
print("O peso depois:", pessoa1.peso)
print("A altura depois:", pessoa1.altura)