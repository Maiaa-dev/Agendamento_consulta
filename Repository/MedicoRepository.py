medicos = []

class MedicoRepository:
    def CadastrarMedico(medico):
        medicos.append(medico)

    def ListarMedicos():
        return medicos
    