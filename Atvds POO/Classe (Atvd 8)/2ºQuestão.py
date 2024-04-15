# Questão 2

class Aluno:
  def __init__(self, nome_aluno, matricula, curso):
    self.nome_aluno = nome_aluno
    self.matricula = matricula
    self.curso = curso
  def mostrar_curso(self):
    print(f"Curso: {self.curso}")
  def alterar_curso(self, novo_curso):
    self.curso = novo_curso
    print("Curso alterado com sucesso.")

aluno1 = Aluno(nome_aluno = "Carla", matricula = 1, curso = "Desenvolvimento de Sistemas")
aluno1.mostrar_curso()
aluno1.alterar_curso("Psicologia")
aluno1.mostrar_curso()