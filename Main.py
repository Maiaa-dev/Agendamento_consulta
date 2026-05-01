from Classes.Paciente import Paciente
from Repository.PacienteRepository import PacienteRepository

PacienteRepo = PacienteRepository

from Classes.Medico import Medico
from Repository.MedicoRepository import MedicoRepository

MedicoRepo = MedicoRepository

from Classes.Consulta import Consulta
from Repository.ConsultaRepository import ConsultaRepository

ConsultaRepo = ConsultaRepository

def menu():
    while True:
        print("\nAGENDAMENTO DE CONSULTA")
        print("Selecione uma das opções a seguir:")
        print("1- Paciente")
        print("2- Médico")
        print("3- Consultas")
        print("4- Sair")

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
                pacientes = PacienteRepo.ListarPacientes()
                for paciente in pacientes:
                    print(paciente)
            
            elif escolha == 2:
                id_paciente = 1
                nome = input("Nome: ")
                sobrenome = input("Sobrenome: ")
                idade = int(input("Idade: "))
                email = input("Email: ")

                paciente = Paciente(id_paciente,nome,sobrenome,idade,email)
                PacienteRepo.CadastrarPaciente(paciente)
                menu()
            elif escolha == 3:
                menu()
            elif escolha == 4:
                break

        if escolha == 2:
            print("\nMÉDICO")
            print("O que você deseja fazer?")
            print("1- Listar médicos")
            print("2- Cadastrar médico")
            print("3- Voltar para o menu")
            print("4- Sair")
            
            escolha = int(input())

            if escolha == 1:
                for medico in MedicoRepo.ListarMedicos():
                    print(medico)
            elif escolha == 2:
                id_medico = 1
                nome = input("Nome: ")
                sobrenome = input("Sobrenome: ")
                especialidade = input("Especialidade: ")

                medico = Medico(id_medico,nome,sobrenome,especialidade)
                MedicoRepo.CadastrarMedico(medico)
                menu()
            elif escolha == 3:
                menu()
            elif escolha == 4:
                break
        
        if escolha == 3:
            print("\nCONSULTA")
            print("O que você deseja fazer?")
            print("1- Listar consultas")
            print("2- Cadastrar consulta")
            print("3- Voltar para o menu")
            print("4- Sair")
            
            escolha = int(input())

            if escolha == 1:
                for consulta in ConsultaRepo.ListarConsultas():
                    print(consulta)
            elif escolha == 2:
                id_consulta = 1
                id_medico = int(input("ID do médico: "))
                id_paciente = int(input("ID do paciente: "))
                horario = input("Horário da consulta: ")

                consulta = Consulta(id_consulta,id_medico,id_paciente,horario)
                ConsultaRepo.CadastrarConsulta(consulta)
                menu()
            elif escolha == 3:
                menu()
            elif escolha == 4:
                break
        else:
            break
menu()