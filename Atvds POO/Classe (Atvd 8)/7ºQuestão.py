# Questão 7

class Macaco:
  def __init__(self, nome):
      self.nome = nome
      self.bucho = []

  def comer(self, comida):
      self.bucho.append(comida)
      print(f"{self.nome} comeu {comida}.")

  def ver_bucho(self):
      print(f"{self.nome} tem no estômago: {', '.join(self.bucho)}.")

  def digerir(self):
      if self.bucho:
          comida = self.bucho.pop(0)
          print(f"{self.nome} digeriu {comida}.")
      else:
          print(f"{self.nome} não tem nada no estômago.")

macaco1 = Macaco(nome = "Luffy")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Nozes")

macaco1.ver_bucho()

macaco1.digerir()

macaco1.ver_bucho()

print ("\n")
macaco2 = Macaco(nome = "Zoro")

macaco2.comer("Carne")
macaco2.comer("Maçã")
macaco2.comer("Luffy")

macaco2.ver_bucho()

macaco2.digerir()

macaco2.ver_bucho()

print("O Zoro comeu o Luffy!!!  Ele é um canibal AAAA!!!")
