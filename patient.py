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

    def update(self):
        print("Digite onde deseja ser alterado e caso não deseje alterações pressione enter deixando o item em branco:")
        name = input("Nome: ")
        age = int(input("Idade: "))
        history = input("Histórico: ")
        contact = input("Contato: ")
        address = input("Endereço: ")

        if(name != ""): self.name = name
        if(age > 0 ): self.age = age
        if(history != ""): self.history = history
        if(contact != ""): self.contact = contact
        if(address != ""): self.address = address

    @staticmethod
    def search_by_id(patient_id: str):
        for patient in Patient.patients_list:
            if patient.id == patient_id:
                return patient
        return None  # Retorna None se não encontrar

    @staticmethod
    def consult(name: str):
        encontrados = []

        for patient in Patient.patients_list:
            if name.lower() in patient.name.lower():
                encontrados.append(patient)

        if encontrados:
            print(f"\nPacientes encontrados com o nome contendo '{name}':")
            for patient in encontrados:
                print(f"ID: {patient.id} | Nome: {patient.name} | Idade: {patient.age} | Endereço: {patient.address} | Contato: {patient.contact}")
        else:
            print(f"Nenhum paciente com nome contendo '{name}' foi encontrado.")
    
    @staticmethod
    def list_all():
        print("\nLista de Pacientes:")
        for patient in Patient.patients_list:
            print(f"ID: {patient.id} | Nome: {patient.name} | Idade: {patient.age} | Histórico: {patient.history} | Contato: {patient.contact}")

    @staticmethod
    def remove(patient_id: str):
        for patient in Patient.patients_list:
            if patient.id == patient_id:
                Patient.patients_list.remove(patient)
                print(f"Paciente {patient.name} removido com sucesso!")
                return
        print(f"Paciente com ID '{patient_id}' não encontrado.")

    @staticmethod
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