from secrets import token_urlsafe


class Doctor:
    doctors_list = []

    def __init__(self, name: str = "", specialty: str = "", service_hour:str = "", contact:str = "", salary: int = 0):
        self.id = token_urlsafe(5)
        self.name = name
        self.speciality = specialty
        self.service_hour = service_hour
        self.contact = contact
        self.salary = salary
        Doctor.doctors_list.append(self)

    def getName(self):
        return self.name
    def getSpecialty(self):
        return self.speciality
    def getServiceHour(self):
        return self.service_hour
    def getContact(self):
        return self.contact
    def getSalary(self):
        return self.salary
    
    def setName(self, name):
        self.name = name
    def setSpecialty(self, specialty):
        self.speciality = specialty
    def setServiceHour(self, service_hour):
        self.service_hour = service_hour
    def setContact(self, contact):
        self.contact = contact
    def setSalary(self, salary):
        self.salary = salary

    def update(self):
        print("Digite onde deseja ser alterado e caso não deseje alterações pressione enter deixando o item em branco:")
        name = input("Nome: ")
        specialty = input("Especialidade: ")
        service_hour = input("Horário de atendimento: ")
        contact = input("Contato: ")
        salary = int(input("Salario: "))

        if(name != ""): self.name = name
        if(specialty != ""): self.age = specialty
        if(service_hour != ""): self.history = service_hour
        if(contact != ""): self.contact = contact
        if(salary >= 0): self.address = salary

    @staticmethod
    def list_all():
        print("\nLista de Médicos:")
        for doctor in Doctor.doctors_list:
            print(f"ID: {doctor.id} | Nome: {doctor.name} | Especialidade: {doctor.speciality} | Contato: {doctor.contact}")

    @staticmethod
    def remove(doctor_id: str):
        for doctor in Doctor.doctors_list:
            if doctor.id == doctor_id:
                Doctor.doctors_list.remove(doctor)
                print(f"Médico {doctor.name} removido com sucesso!")
                return
        print(f"Médico com ID '{doctor_id}' não encontrado.")

    @staticmethod
    def search_by_id(doctor_id: str):
        for doctor in Doctor.doctors_list:
            if doctor.id == doctor_id:
                return doctor
        return None  # Retorna None se não encontrar

    @staticmethod
    def listOne(name: str):
        for doctor in Doctor.doctors_list:
            if doctor.name.lower() == name.lower():
                print(f"\nMédico encontrado:\nID: {doctor.id} | Nome: {doctor.name} | Especialidade: {doctor.speciality} | Contato: {doctor.contact}")
                return
        print(f"Médico '{name}' não encontrado.")

    @staticmethod
    def search_Name(name: str):
        for doctor in Doctor.doctors_list:
            if doctor.name.lower() == name.lower():
                return doctor
        return None  # Retorna None se o médico não for encontrado
    
    @staticmethod
    def consult(name: str):
        encontrados = []

        for doctor in Doctor.doctors_list:
            if name.lower() in doctor.name.lower():
                encontrados.append(doctor)

        if encontrados:
            print(f"\nMédicos encontrados com o nome contendo '{name}':")
            for doctor in encontrados:
                print(f"ID: {doctor.id} | Nome: {doctor.name} | Especialidade: {doctor.speciality}")
        else:
            print(f"Nenhum médico com nome contendo '{name}' foi encontrado.")