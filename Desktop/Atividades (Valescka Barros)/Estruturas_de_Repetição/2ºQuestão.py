#2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario != senha:
        print("Usuário e senha cadastrados com sucesso.")
        break
    else:
        print("Erro: Usuário e senha não podem ser iguais. Tente novamente.")
