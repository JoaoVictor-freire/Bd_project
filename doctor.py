class Doctor:
    def __init__(self, name, specialty, service_hour, contact, salary):
        self.name = name
        self.speciality = specialty
        self.service_hour = service_hour
        self.contact = contact
        self.salary = salary

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

    def uptade(self, name = None, specialty = None, service_hour = None, contact = None, salary = None):
        if(name != None): self.name = name
        if(specialty != None): self.age = specialty
        if(service_hour != None): self.history = service_hour
        if(contact != None): self.contact = contact
        if(salary != None): self.address = salary