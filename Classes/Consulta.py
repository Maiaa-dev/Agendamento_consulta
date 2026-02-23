class Consulta:
    def __init__(self, id_consulta, id_paciente, id_medico, horario):
        self.id_consulta = id_consulta
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.horario = horario
    def __str__(self):
        return f"ID: {self.id_consulta} | ID do médico: {self.id_medico} | ID do paciente: {self.id_paciente} | Horário: {self.horario}"