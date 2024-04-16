# 4° Questão

def inverte_string(frase):
  frase = frase[::-1]
  return frase

oracao = str(input("Insira uma frase aí: "))
resultado = inverte_string(oracao)
print("A frase '{}' invertida é: '{}'".format(oracao, resultado))