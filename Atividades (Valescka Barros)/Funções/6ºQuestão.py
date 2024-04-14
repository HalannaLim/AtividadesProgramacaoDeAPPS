# 6° Questão

def conta_vogal(string):
  string = string.lower()
  quantidade = 0
  for i in string:
    if i in "aeiou":
      quantidade += 1
  return quantidade

frase = str(input("Insira uma frase: "))
vogais = conta_vogal(frase)
print(f"A quantidade de vogais na frase {frase} é: {vogais}")