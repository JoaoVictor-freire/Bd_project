from doctor import Doctor
from patient import Patient

from secrets import token_urlsafe

class Exam:
    exams_list = []

    def __init__(self, doctor: Doctor = None, patient: Patient = None, status: str = "", date: str = "", hour: str = ""):
        self.id = token_urlsafe(8)
        self.doctor = doctor
        self.patient = patient
        self.status = status
        self.date = date
        self.hour = hour
        Exam.exams_list.append(self)

    def getId(self):
        return self.id
    def getDoctor(self):
        return self.doctor
    def getPatient(self):
        return self.patient
    def getStatus(self):
        return self.status
    def getDate(self):
        return self.date
    def getHour(self):
        return self.hour
    
    def setStatus(self, status):
        self.status = status
    def setDate(self, date):
        self.date = date
    def setHour(self, hour):
        self.hour = hour

    def schedule(self, doctor: Doctor, patient: Patient, date: str, hour: str, status: str = "Scheduled"):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.hour = hour
        self.status = status
        print(f"Exame agendado para {self.patient.getName()} com {self.doctor.getName()} em {self.date} às {self.hour}.")

    def cancel(self):
        self.status = "Canceled"
        print(f"Exame de {self.patient.getName()} com {self.doctor.getName()} foi cancelado.")

    # Método para confirmar um exame
    def confirm(self):
        self.status = "Confirmed"
        print(f"Exame de {self.patient.getName()} com {self.doctor.getName()} foi confirmado.")

    # Método para listar os detalhes do exame
    def details(self):
        print(f"Exame ID: {self.id}")
        print(f"Paciente: {self.patient.getName()} | Médico: {self.doctor.getName()}")
        print(f"Data: {self.date} | Hora: {self.hour} | Status: {self.status}")

    def register_exam(self, doctor: Doctor, patient: Patient, date: str, hour: str, status: str = "Scheduled"):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.hour = hour
        self.status = status
        print(f"Exame cadastrado para {self.patient.getName()} com {self.doctor.getName()} em {self.date} às {self.hour}.")
    
    def list_all():
        print("\nLista de Exames:")
        for exam in Exam.exams_list:
            print(f"ID: {exam.id} | Paciente: {exam.patient.name} | Médico: {exam.doctor.name} | Data: {exam.date} | Hora: {exam.hour} | Status: {exam.status}")

