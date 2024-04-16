#2 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Insira um sexo: "))
if sexo == 'M':
  print("O sexo que você digitou é Masculino!")
elif sexo == 'F':
  print("O sexo que você digitou é Feminino!")
else:
  print("Sexo Inválido!")
