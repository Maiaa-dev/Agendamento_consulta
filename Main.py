from Classes.Paciente import Paciente
from Repository.PacienteRepository import CadastrarPaciente,ListarPacientes

from Classes.Medico import Medico
from Repository.MedicoRepository import CadastrarMedico,ListarMedicos

from Classes.Consulta import Consulta
from Repository.ConsultaRepository import CadastrarConsulta,ListarConsultas

def menu():
    while True:
        print("\nAGENDAMENTO DE CONSULTA")
        print("Selecione uma das opções a seguir:")
        print("1- Paciente")
        print("2- Médico")
        print("3- Consultas")

        escolha = int(input())

        if escolha == 1:
            print("\nPACIENTE")
            print("O que você deseja fazer?")
            print("1- Listar pacientes")
            print("2- Cadastrar paciente")
            print("3- Voltar para o menu")
            print("4- Sair")
            
            escolha = int(input())

            if escolha == 1:
                for paciente in ListarPacientes():
                    print(paciente)
            elif escolha == 2:
                id_paciente = 1
                nome = input("Nome: ")
                sobrenome = input("Sobrenome: ")
                idade = int(input("Idade: "))
                email = input("Email: ")

                paciente = Paciente(id_paciente,nome,sobrenome,idade,email)
                CadastrarPaciente(paciente)
            elif escolha == 3:
                menu()
            elif escolha == 4:
                break

menu()