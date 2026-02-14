#self é equivalente ao this em c#
class Paciente:
    def __init__(self, id_paciente, nome, sobrenome, idade, email):
        self.id_paciente = id_paciente
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.email = email
    def __str__(self):
        return f"ID: {self.id_paciente} | Nome: {self.nome} | Sobrenome: {self.sobrenome} | Idade: {self.idade} | Email: {self.email}"