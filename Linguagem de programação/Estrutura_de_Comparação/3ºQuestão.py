#3 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digita uma letra ai namoral: ")).lower()

if letra in 'aeiou':
  print("Eita glória, inserisse uma vogal")
else:
  print("UIII, colocasse uma consoante")

