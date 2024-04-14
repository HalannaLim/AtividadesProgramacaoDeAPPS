# 5° Questão

def maior_valor(lista):
    if not lista:
        return None
    return max(lista)

lista_numeros = [14, 17, 20, 23, 26]
print(maior_valor(lista_numeros))
