from secrets import token_urlsafe

class Patient:
    patients_list = []

    def __init__ (self, name: str = "", age: int = 0, history: str = "", contact: str = "", address: str = ""):
        self.id = token_urlsafe(10)
        self.name = name
        self.age = age
        self.history = history
        self.contact = contact
        self.address = address
        Patient.patients_list.append(self)

    def defId(self):
        return self.id
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getHistory(self):
        return self.history
    def getContact(self):
        return self.contact
    def getAddress(self):
        return self.address
        
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def setHistory(self, hist):
        self.history = hist
    def setContact(self, contact):
        self.contact = contact
    def setAddress(self, address):
        self.address = address

    def cadastrar(self, name, age,history, contact, address):
        self.setName(name)
        self.setAge(age)
        self.setHistory(history)
        self.setContact(contact)
        self.setAddress(address)

    def update(self, name = None, age = None, history = None, contact = None, address = None):
        if(name != None): self.name = name
        if(age != None): self.age = age
        if(history != None): self.history = history
        if(contact != None): self.contact = contact
        if(address != None): self.address = address

    def consult(self, id):
        if(self.id == id):
            print(f'Nome: {self.name} | Idade: {self.age} | Endereço: {self.address} | Contato: {self.contact}')
    
    def list_all():
        print("\nLista de Pacientes:")
        for patient in Patient.patients_list:
            print(f"ID: {patient.id} | Nome: {patient.name} | Idade: {patient.age} | Histórico: {patient.history} | Contato: {patient.contact}")

    def remove(patient_id: str):
        for patient in Patient.patients_list:
            if patient.id == patient_id:
                Patient.patients_list.remove(patient)
                print(f"Paciente {patient.name} removido com sucesso!")
                return
        print(f"Paciente com ID '{patient_id}' não encontrado.")

    def listOne(name: str):
        for patient in Patient.patients_list:
            if patient.name.lower() == name.lower():
                print(f"\nPaciente encontrado:\nID: {patient.id} | Nome: {patient.name} | Idade: {patient.age} | Histórico: {patient.history} | Contato: {patient.contact}")
                return
        print(f"Paciente '{name}' não encontrado.")

    def search_Name(name: str):
        for patient in Patient.patients_list:
            if patient.name.lower() == name.lower():
                return patient
        return None  # Retorna None se o paciente não for encontrado