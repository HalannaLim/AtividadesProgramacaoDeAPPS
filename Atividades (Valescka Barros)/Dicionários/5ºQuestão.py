#5. Faça um programa, utilizando Dicionários, que:

    #1° Passo: Peça para o usuário inserir o nome de três funcionários e os mostre na tela.

    #2° Passo: Peça para o usuário demitir um funcionário e mostre na tela os funcionários restantes.


funcionarios = {}

for i in range(3):
    funcionario = input("Digite o nome do funcionário: ")
    funcionarios[f'Funcionário{i+1}'] = funcionario

print("Funcionários:", funcionarios)

demissao = input("Digite o nome do funcionário a ser demitido: ")

chaves_para_remover = [chave for chave, valor in funcionarios.items() if valor == demissao]

for chave in chaves_para_remover:
    del funcionarios[chave]
    print(f'{demissao} foi demitido.')

if not chaves_para_remover:
    print(f'{demissao} não encontrado na lista de funcionários.')

print("Funcionários restantes:", funcionarios)