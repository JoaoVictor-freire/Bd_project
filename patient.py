from secrets import token_urlsafe

class Patiente:
    def __int__ (self, name, age, history, contact, address):
        self.id = token_urlsafe(10)
        self.name = name
        self.age = age
        self.history = history
        self.contact = contact
        self.address = address

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
        self.adress = address

    def cadastrar(self, name, age,history, contact, address):
        self.setName(name)
        self.setAge(age)
        self.setHistory(history)
        self.setContact(contact)
        self.setAddress(address)

    def uptade(self, name = None, age = None, history = None, contact = None, address = None):
        if(name != None): self.name = name
        if(age != None): self.age = age
        if(history != None): self.history = history
        if(contact != None): self.contact = contact
        if(address != None): self.address = address

    def consult(self, id):
        if(self.id == id):
            print(f'Nome: {self.name} | Idade: {self.age} | Endereço: {self.address} | Contato: {self.contact}')
    