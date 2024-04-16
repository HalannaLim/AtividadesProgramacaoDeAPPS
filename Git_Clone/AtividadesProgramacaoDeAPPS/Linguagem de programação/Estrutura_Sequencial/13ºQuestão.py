#13 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   .salário bruto.
#   .Quanto pagou ao INSS.
#   .quanto pagou ao sindicato.
#   .o salário líquido.

#   calcule os descontos e o salário líquido, conforme a fórmula abaixo:
#   + Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%) : R$  = Salário Liquido : R$
#   Obs.: Salário Bruto - Descontos = Salário Líquido.

hora= float(input("O quanto você ganha por hora? :"))
horas= float(input("Quantas horas você trabalha no dia? :"))
dia = (hora * horas)
salariomensal = dia *20

Salariobruto = salariomensal * 0.11
INSS = salariomensal * 0.08
Sindicato = salariomensal * 0.05
Salarioliquido = salariomensal - Sindicato - Salariobruto -INSS

print("O seu salário Bruto é: R$" , Salariobruto,"O INSS é R$:", INSS ,"O valor pago ao sindicato é: R$",Sindicato ,"O Seu salário líquido é R$:",Salarioliquido)
