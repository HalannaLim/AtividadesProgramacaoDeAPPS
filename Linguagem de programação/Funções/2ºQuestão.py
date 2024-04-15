# 2° Questão

def fatorial(num):
  fat = 1
  for i in range(num, 1, -1):
    fat *= i
  return fat

numero = int(input("Insira um número pfvr: "))
resultado = fatorial(numero)
print("O fatorial de {} é: {}".format(numero, resultado))