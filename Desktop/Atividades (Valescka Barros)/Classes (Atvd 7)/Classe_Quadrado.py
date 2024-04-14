# Crie uma classe que modele um quadrado:

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2

# Testando a classe
quadrado_teste = Quadrado(5)

print("Lado do quadrado:", quadrado_teste.retornar_lado())
print("Área do quadrado:", quadrado_teste.calcular_area())

quadrado_teste.mudar_lado(7)

print("Novo lado do quadrado:", quadrado_teste.retornar_lado())
print("Nova área do quadrado:", quadrado_teste.calcular_area())