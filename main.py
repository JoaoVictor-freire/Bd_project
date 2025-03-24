from doctor import Doctor
from patient import Patient
from exam import Exam
import os

def limpar_cmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione Enter para continuar...")

def main():
    while True:
        limpar_cmd()
        print("\nClínica NovaMed - A clínica que cuida da saúde da sua família")
        print("1. Médicos")
        print("2. Pacientes")
        print("3. Exames")
        print("4. Sair")
        
        option = input("Qual opção deseja seguir? ")

        if option == "1":
            menu_doctors()
        elif option == "2":
            menu_patients()
        elif option == "3":
            menu_exams()
        elif option == "4":
            print("Até breve!")
            break
        else:
            limpar_cmd()
            print("Opção inválida! Tente novamente.")
            pausar()

def menu_doctors():
    while True:
        limpar_cmd()
        print("\nMédicos da Clínica NovaMed")
        print("1. Buscar médico pelo nome")
        print("2. Listar médicos")
        print("3. Cadastrar novo médico")
        print("4. Atualizar médico")
        print("5. Remover médico")
        print("6. Voltar ao menu principal")

        option_m = input("Qual opção deseja realizar? ")

        if option_m == "1":
            limpar_cmd()
            name = input("Digite o nome do médico: ")
            Doctor.list_all()
            pausar()

        elif option_m == "2":
            limpar_cmd()
            Doctor.list_all()
            pausar()

        elif option_m == "3":
            limpar_cmd()
            name = input("Nome: ")
            specialty = input("Especialidade: ")
            service_hour = input("Horário de Serviço: ")
            contact = input("Contato: ")
            salary = float(input("Salário: "))

            doctor1 = Doctor(name, specialty, service_hour, contact, salary)
            Doctor.cadastrar(doctor1)
            print("Médico cadastrado com sucesso!")
            pausar()

        elif option_m == "4":
            limpar_cmd()
            doctor_id = input("Digite o ID do médico: ")
            
            try:
                doctor_id = int(doctor_id)  # Garantir que o ID seja um número inteiro
            except ValueError:
                print("Erro: ID inválido. O ID deve ser um número.")
                return
            
            doctor = Doctor.search_by_id(doctor_id)  # Retorna uma tupla com os dados do médico

            if doctor:
                new_name = input(f"Nome ({doctor[1]}): ") or doctor[1]
                new_specialty = input(f"Especialidade ({doctor[2]}): ") or doctor[2]
                new_service_hour = input(f"Horário de atendimento ({doctor[3]}): ") or doctor[3]
                new_contact = input(f"Contato ({doctor[4]}): ") or doctor[4]
                new_salary = input(f"Salário ({doctor[5]}): ") or doctor[5]

                # Passando os 6 parâmetros diretamente para o método update
                Doctor.update(doctor[0], new_name, new_specialty, new_service_hour, new_contact, new_salary)
                print("Médico atualizado com sucesso!")
            else:
                print("Médico não encontrado!")

            pausar()



        elif option_m == "5":
            limpar_cmd()
            doctor_id = input("Digite o ID do médico: ")
            Doctor.remove(int(doctor_id))
            pausar()

        elif option_m == "6":
            limpar_cmd()
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida! Tente novamente.")
            pausar()

def menu_patients():
    while True:
        limpar_cmd()
        print("\nPacientes da Clínica NovaMed")
        print("1. Buscar paciente pelo nome")
        print("2. Listar pacientes")
        print("3. Cadastrar novo paciente")
        print("4. Atualizar paciente")
        print("5. Remover paciente")
        print("6. Voltar ao menu principal")

        option_p = input("Qual opção deseja realizar? ")

        if option_p == "1":
            limpar_cmd()
            name = input("Digite o nome do paciente: ")
            Patient.list_all()
            pausar()

        elif option_p == "2":
            limpar_cmd()
            Patient.list_all()
            pausar()

        elif option_p == "3":
            limpar_cmd()
            name = input("Nome: ")
            age = input("Idade: ")
            history = input("Histórico médico: ")
            contact = input("Contato: ")
            address = input("Endereço: ")

            patient1 = Patient(name, age, history, contact, address)
            Patient.cadastrar(patient1)
            print("Paciente cadastrado com sucesso!")
            pausar()

        elif option_p == "4":
            limpar_cmd()
            name = input("Digite o nome do paciente a realizar alterações: ")
            patient_id = input("Digite o ID do paciente que deseja atualizar: ")
            patient = Patient.search_by_id(int(patient_id))

            if patient:
                # Implementar a atualização, se necessário
                print("Paciente atualizado com sucesso!")
            else:
                print("Paciente não encontrado.")

            pausar()

        elif option_p == "5":
            limpar_cmd()
            patient_id = input("Digite o ID do paciente: ")
            Patient.remove(int(patient_id))
            pausar()

        elif option_p == "6":
            limpar_cmd()
            print("Voltando ao menu principal...")
            break

        else:
            limpar_cmd()
            print("Opção inválida! Tente novamente.")
            pausar()

def menu_exams():
    while True:
        limpar_cmd()
        print("\nExames da Clínica NovaMed")
        print("1. Cadastrar exame")
        print("2. Agendar exame")
        print("3. Confirmar exame")
        print("4. Cancelar exame")
        print("5. Listar exames")
        print("6. Voltar ao menu principal")

        option_e = input("Qual opção deseja realizar? ")

        if option_e == "1":
            limpar_cmd()
            doctor_id = input("Digite o ID do médico: ")
            doctor = Doctor.search_by_id(int(doctor_id))
            if not doctor:
                print("Médico não encontrado!")
                pausar()
                continue

            patient_id = input("Digite o ID do paciente: ")
            patient = Patient.search_by_id(int(patient_id))
            if not patient:
                print("Paciente não encontrado!")
                pausar()
                continue

            date = input("Data do exame (DD/MM/AAAA): ")
            hour = input("Hora do exame (HH:MM): ")

            exam = Exam(doctor, patient, "Pending", date, hour)
            print("Exame cadastrado com sucesso!")
            pausar()

        elif option_e == "2":
            limpar_cmd()
            exam_id = input("Digite o ID do exame: ")
            Exam.schedule(int(exam_id))
            pausar()

        elif option_e == "3":
            limpar_cmd()
            exam_id = input("Digite o ID do exame: ")
            Exam.confirm(int(exam_id))
            pausar()

        elif option_e == "4":
            limpar_cmd()
            exam_id = input("Digite o ID do exame: ")
            Exam.cancel(int(exam_id))
            pausar()

        elif option_e == "5":
            limpar_cmd()
            Exam.list_all()
            pausar()

        elif option_e == "6":
            limpar_cmd()
            print("Voltando ao menu principal...")
            break

        else:
            limpar_cmd()
            print("Opção inválida! Tente novamente.")
            pausar()

if __name__ == "__main__":
    main()
