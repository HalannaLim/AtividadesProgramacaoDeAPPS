#Questão 4

class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def incrementar_segundos(self, segundos):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo + segundos
        self.hora = total_segundos // 3600
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60

    def diferenca_entre_horarios(self, outro_horario):
        segundos_atual = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        diferenca = abs(segundos_atual - segundos_outro)

        horas = diferenca // 3600
        minutos = (diferenca % 3600) // 60
        segundos = diferenca % 60

        return f"{horas} horas, {minutos} minutos, {segundos} segundos"



horario_atual = Horario(hora=10, minuto=30, segundo=45)

print(f"Horário Atual: {horario_atual.hora:02d}:{horario_atual.minuto:02d}:{horario_atual.segundo:02d}")

horario_atual.incrementar_segundos(120)

print(f"Horário Após Incremento: {horario_atual.hora:02d}:{horario_atual.minuto:02d}:{horario_atual.segundo:02d}")

outro_horario = Horario(10, 30, 45)

diferenca = horario_atual.diferenca_entre_horarios(outro_horario)
print(f"Diferença entre os horários: {diferenca}")