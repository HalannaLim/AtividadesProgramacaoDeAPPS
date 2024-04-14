class Tamagushi:
  def __init__(self, nome_bixin, fome, saude, idade):
    self.nome_bixin = nome_bixin
    self.fome = fome
    self.saude = saude
    self.idade = idade
  def alterar_nomebixin(self, novo_nomebixin):
    self.nome_bixin = novo_nomebixin
    return novo_nomebixin
  def alterar_fome(self, nova_fome):
    self.fome = nova_fome
    return nova_fome
  def alterar_saude(self, nova_saude):
    self.saude = nova_saude
    return nova_saude
  def alterar_idade(self, nova_idade):
    self.idade = nova_idade
    return nova_idade
  def humor(self):
    humor = (self.fome + self.saude)/2
    return humor

tamagushi1 = Tamagushi(nome_bixin="Chopper", fome=2, saude=8, idade=15)
novo_nome = "Chopper Jr."

tamagushi1.alterar_nomebixin(novo_nome)

print("Nome:", tamagushi1.nome_bixin)
print("Fome:", tamagushi1.fome)
print("Saúde:", tamagushi1.saude)
print("Idade:", tamagushi1.idade)
print("Humor:", tamagushi1.humor())

tamagushi1.alterar_nomebixin("Tammy Jr.")
tamagushi1.alterar_fome(3)
tamagushi1.alterar_saude(9)
tamagushi1.alterar_idade(2)

print("\nApós alterações:")
print("Nome:", tamagushi1.nome_bixin)
print("Fome:", tamagushi1.fome)
print("Saúde:", tamagushi1.saude)
print("Idade:", tamagushi1.idade)
print("Humor:", tamagushi1.humor())
