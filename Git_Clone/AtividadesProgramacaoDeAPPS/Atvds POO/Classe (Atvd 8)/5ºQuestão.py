# Questão 5

class Carro:
  def __init__(self, marca, ano, preco):
    self.marca = marca
    self.ano = ano
    self.preco = preco
  def mostrar_preco(self):
    print(f"Preço: {self.preco}")
  def exibir_dados(self):
    print(
      f"Marca: {self.marca}\n"
      f"Ano: {self.ano}\n"
      f"Preço: {self.preco}"
    )

carro1 = Carro(marca = "Lamborguini", ano = 2030, preco = "R$10.000.000,00")
carro1.mostrar_preco()
carro1.exibir_dados()