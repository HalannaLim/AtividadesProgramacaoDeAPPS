#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora= float(input("O quanto você ganha por hora? :"))
horas= float(input("Quantas horas você trabalha no dia? :"))
dia = (hora * horas)

print("Você ganha por mês o seguinte salário R$:", dia * 20)
