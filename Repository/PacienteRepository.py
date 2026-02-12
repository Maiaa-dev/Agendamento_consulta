pacientes = []

#def -> para definir funções
#pacientes é uma lista, onde armazenaremos os objetos/dados
#cada paciente tem seus atributos na classe Paciente, onde enviaremos para lá, 
# meio que pacientes é uma lista temporária para guardar os dados do objeto em questão

def CadastrarPaciente(paciente):
    pacientes.append(paciente)

def ListarPacientes():
    return pacientes

