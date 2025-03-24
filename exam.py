import psycopg2
from psycopg2 import sql
from doctor import Doctor
from patient import Patient
from secrets import token_urlsafe
from db import get_connection  # Supondo que a função de conexão com o banco está no arquivo db.py

class Exam:
    # Método para cadastrar um exame no banco de dados
    def __init__(self, doctor: Doctor = None, patient: Patient = None, status: str = "", date: str = "", hour: str = "", id: str = None):
        self.id = id or token_urlsafe(8)
        self.doctor = doctor
        self.patient = patient
        self.status = status
        self.date = date
        self.hour = hour

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
        self.register_exam()

    def cancel(self):
        self.status = "Canceled"
        self.update_exam()

    def confirm(self):
        self.status = "Confirmed"
        self.update_exam()

    def details(self):
        print(f"Exame ID: {self.id}")
        print(f"Paciente: {self.patient.getName()} | Médico: {self.doctor.getName()}")
        print(f"Data: {self.date} | Hora: {self.hour} | Status: {self.status}")

    # Método para registrar um exame no banco de dados
    def register_exam(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO exams (id, doctor_id, patient_id, status, date, hour)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (self.id, self.doctor.id, self.patient.id, self.status, self.date, self.hour))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Exame cadastrado para {self.patient.getName()} com {self.doctor.getName()} em {self.date} às {self.hour}.")

    # Método para atualizar um exame no banco de dados
    def update_exam(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE exams 
            SET status = %s
            WHERE id = %s
        """, (self.status, self.id))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Exame de {self.patient.getName()} com {self.doctor.getName()} foi atualizado para status '{self.status}'.")

    # Método para listar todos os exames do banco de dados
    @staticmethod
    def list_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.id, p.name, d.name, e.date, e.hour, e.status
            FROM exams e
            JOIN patients p ON e.patient_id = p.id
            JOIN doctors d ON e.doctor_id = d.id
        """)
        exams = cursor.fetchall()
        cursor.close()
        conn.close()

        print("\nLista de Exames:")
        for exam in exams:
            print(f"ID: {exam[0]} | Paciente: {exam[1]} | Médico: {exam[2]} | Data: {exam[3]} | Hora: {exam[4]} | Status: {exam[5]}")

    # Método para remover um exame do banco de dados
    @staticmethod
    def remove(exam_id: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM exams WHERE id = %s
        """, (exam_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Exame com ID '{exam_id}' removido com sucesso!")
