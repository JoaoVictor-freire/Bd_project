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

    def cadastrar(self, name, specialty, service_hour, contact, salary):
        self.name = name
        self.speciality = specialty
        self.service_hour = service_hour
        self.contact = contact
        self.salary = salary

    def update(self, name = None, specialty = None, service_hour = None, contact = None, salary = None):
        if(name != None): self.name = name
        if(specialty != None): self.age = specialty
        if(service_hour != None): self.history = service_hour
        if(contact != None): self.contact = contact
        if(salary != None): self.address = salary

    def list_all():
        print("\nLista de Médicos:")
        for doctor in Doctor.doctors_list:
            print(f"ID: {doctor.id} | Nome: {doctor.name} | Especialidade: {doctor.speciality} | Contato: {doctor.contact}")

    def remove(doctor_id: str):
        for doctor in Doctor.doctors_list:
            if doctor.id == doctor_id:
                Doctor.doctors_list.remove(doctor)
                print(f"Médico {doctor.name} removido com sucesso!")
                return
        print(f"Médico com ID '{doctor_id}' não encontrado.")

    def listOne(name: str):
        for doctor in Doctor.doctors_list:
            if doctor.name.lower() == name.lower():
                print(f"\nMédico encontrado:\nID: {doctor.id} | Nome: {doctor.name} | Especialidade: {doctor.speciality} | Contato: {doctor.contact}")
                return
        print(f"Médico '{name}' não encontrado.")

    def search_Name(name: str):
        for doctor in Doctor.doctors_list:
            if doctor.name.lower() == name.lower():
                return doctor
        return None  # Retorna None se o médico não for encontrado