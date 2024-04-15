#9 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    # salários até R$ 280,00 (incluindo) : aumento de 20%
    # salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    # salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    # o salário antes do reajuste;
    # o percentual de aumento aplicado;
    # o valor do aumento;
    # o novo salário, após o aumento.

salario = float(input("Digite o salário do colaborador: "))

if salario<=280:
  percentualaumento = 20

elif salario <= 700:
  percentualaumento = 15

elif salario <= 1500:
 percentualaumento =10

else:
  percentualaumento = 5

aumento= salario * (percentualaumento/100)
novosalario = salario + aumento

print(f"O salário antes do reajuste era de: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentualaumento}%")
print(f"O valor do aumento foi de: R$ {aumento:.2f}")
print(f" O novo salário após o aumento será de: R$ {novosalario:.2f}")
