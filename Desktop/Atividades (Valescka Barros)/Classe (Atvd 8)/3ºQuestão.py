# Questão 3

class Curso_alunos:
    def __init__(self, matricula, nome_aluno, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome_aluno = nome_aluno
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def acesso_nome(self):
        return self.nome_aluno

    def acesso_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3


alunos = []
for i in range(5):
    matricula = int(input(f"Digite a matrícula do aluno {i + 1}: "))
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))
    nota3 = float(input("Digite a nota da terceira prova: "))

    aluno = Curso_alunos(matricula, nome, nota1, nota2, nota3)
    alunos.append(aluno)

aluno_maior_media = max(alunos, key=lambda x: x.acesso_media())
print(f"\nAluno com maior média geral: {aluno_maior_media.acesso_nome()} - Média: {aluno_maior_media.acesso_media()}")

aluno_menor_media = min(alunos, key=lambda x: x.acesso_media())
print(f"Aluno com menor média geral: {aluno_menor_media.acesso_nome()} - Média: {aluno_menor_media.acesso_media()}")

for aluno in alunos:
    if aluno.acesso_media() >= 6:
        print(f"{aluno.acesso_nome()} foi aprovado.")
    else:
        print(f"{aluno.acesso_nome()} foi reprovado.")