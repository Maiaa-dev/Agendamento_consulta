class Medico:
    def __init__(self, id_medico, nome, sobrenome, especialidade):
        self.id_medico = id_medico
        self.nome = nome
        self.sobrenome = sobrenome
        self.especialidade = especialidade
    def __str__(self):
        return f"ID: {self.id_medico} | Nome: {self.nome} | Sobrenome: {self.sobrenome} | Especialidade: {self.especialidade}"


