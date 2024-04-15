## Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

a = [int(input("Digite o {}º elemento do primeiro vetor: ".format(i + 1))) for i in range(10)]
b = [int(input("Digite o {}º elemento do segundo vetor: ".format(i + 1))) for i in range(10)]
c = [int(input("Digite o {}º elemento do terceiro vetor: ".format(i + 1))) for i in range(10)]

d = [None] * 30

for i in range(10):
    d[3 * i] = a[i]
    d[3 * i + 1] = b[i]
    d[3 * i + 2] = c[i]

print("\nAgora observe o terceiro vetor intercalado:", d)
