class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)

lado_a = float(input("Informe a medida do Lado A: "))
lado_b = float(input("Informe a medida do Lado B: "))

local = Retangulo(lado_a, lado_b)

area_local = local.calcular_area()
perimetro_local = local.calcular_perimetro()

quantidade_pisos = area_local
quantidade_rodapes = perimetro_local + 4 
print(f"A área é: {area_local} metros quadrados")
print(f"O perímetro é: {perimetro_local} metros")
print(f"Quantidade de pisos necessários: {quantidade_pisos} metros quadrados")
print(f"Quantidade de rodapés necessários: {quantidade_rodapes} metros")
