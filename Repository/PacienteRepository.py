from db.conexao import CriarConexao

class PacienteRepository:
    def ListarPacientes():
        conexao = CriarConexao()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM pacientes")
        resultado = cursor.fetchall()

        cursor.close()
        conexao.close()

        return resultado
