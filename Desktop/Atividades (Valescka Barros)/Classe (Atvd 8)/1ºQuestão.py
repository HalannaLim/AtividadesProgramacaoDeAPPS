# Questão 1

class Pessoa:
  def __init__(self, nome, idade, endereco):
    self.nome = nome
    self.idade = idade
    self.endereco = endereco
  def mostrarEndereco(self):
    print(f"Endereço: {self.endereco}")

  def alterar_endereco(self, novo_endereco):
    self.endereco = novo_endereco
  print("Endereço alterado com sucesso.")

pessoa1 = Pessoa(nome = "Bernardo", idade = 17, endereco = "Rua João Lopes")

print("O endereço da pessoa é:")
pessoa1.mostrarEndereco()

pessoa1.alterar_endereco("Rua Dom Basílio")

print("O novo endereço da pessoa é:")
pessoa1.mostrarEndereco()