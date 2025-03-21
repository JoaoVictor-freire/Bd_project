from doctor import Doctor
from patient import Patient
from exam import Exam
import os

def limpar_cmd():
    os.system('cls' if os.name == 'nt' else 'clear')


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
            print("Opção inválida! Tente novamente.")

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
            Doctor.listOne(name)

        elif option_m == "2":
            limpar_cmd()
            Doctor.list_all()

        elif option_m == "3":
            limpar_cmd()
            name = input("Nome: ")
            specialty = input("Especialidade: ")
            service_hour = input("Horário de Serviço: ")
            contact = input("Contato: ")
            salary = float(input("Salário: "))

            Doctor().cadastrar(name, specialty, service_hour, contact, salary)
            print("Médico cadastrado com sucesso!")

        elif option_m == "4":
            limpar_cmd()
            doctor_id = int(input("Digite o ID do médico: "))
            Doctor.update(doctor_id)

        elif option_m == "5":
            limpar_cmd()
            doctor_id = int(input("Digite o ID do médico: "))
            Doctor.remove(doctor_id)

        elif option_m == "6":
            limpar_cmd()
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida! Tente novamente.")


def menu_patients():
    patient = Patient()
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
            patient.listOne(name)

        elif option_p == "2":
            limpar_cmd()
            patient.list_all()

        elif option_p == "3":
            limpar_cmd()
            name = input("Nome: ")
            age = input("Idade: ")
            history = input("Histórico médico: ")
            contact = input("Contato: ")
            adress = input("Endereço: ")

            patient.cadastrar(name, age, history, contact, adress)
            print("Paciente cadastrado com sucesso!")

        elif option_p == "4":
            limpar_cmd()
            name = input("Digite o nome do paciente que deseja atualizar: ")
            patient = Patient.search_Name(name)

            if patient:
                new_name = input("Nome: ")
                new_age = input("Idade: ")
                new_history = input("Histórico médico: ")
                new_contact = input("Contato: ")
                new_adress = input("Endereço: ")

            patient.update(new_name, new_age, new_history, new_contact, new_adress)
            print("Paciente atualizado com sucesso!")

        elif option_p == "5":
            limpar_cmd()
            patient_id = input("Digite o ID do paciente: ")
            patient.remove(patient_id)

        elif option_p == "6":
            limpar_cmd()
            print("Voltando ao menu principal...")
            break

        else:
            limpar_cmd()
            print("Opção inválida! Tente novamente.")

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
            name = input("Nome do exame: ")
            description = input("Descrição do exame: ")
            price = float(input("Preço do exame: "))
            date = input("Data do exame (DD/MM/AAAA): ")
            hour = input("Horário do exame (HH:MM): ")
            exam = Exam(name, description, price, date, hour)
            exam.register_exam()

        elif option_e == "2":
            limpar_cmd()
            exam_id = input("Digite o ID do exame: ")
            Exam.schedule(exam_id)

        elif option_e == "3":
            limpar_cmd()
            exam_id = input("Digite o ID do exame: ")
            Exam.confirm(exam_id)

        elif option_e == "4":
            limpar_cmd()
            exam_id = input("Digite o ID do exame: ")
            Exam.cancel(exam_id)

        elif option_e == "5":
            limpar_cmd()
            Exam.list_all()

        elif option_e == "6":
            limpar_cmd()
            print("Voltando ao menu principal...")
            break

        else:
            limpar_cmd()
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
