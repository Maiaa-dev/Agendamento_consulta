consultas = []

class ConsultaRepository:
    def CadastrarConsulta(consulta):
        consultas.append(consulta)

    def ListarConsultas():
        return consultas