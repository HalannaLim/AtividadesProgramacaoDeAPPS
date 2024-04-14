#16 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoarquivomb = float(input("Digite o tamanho do arquivo para download (em MB por favor): "))
velocidadembps = float(input("Digite a velocidade do link de Internet (em Mbps por favor :)): "))

tempominutos = (tamanhoarquivomb / (velocidadembps / 8)) / 60

print(f"O tempo aproximado para realizar o download é de: {tempominutos:.2f} minutos")

