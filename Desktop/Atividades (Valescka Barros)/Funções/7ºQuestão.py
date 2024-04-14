# 7° Questão

def soma_quadrados(lista):
  soma = sum(i ** 2 for i in lista)
  return soma

sequencia = [2, 3, 5, 7, 8]
somatorio = soma_quadrados(sequencia)
print(somatorio)