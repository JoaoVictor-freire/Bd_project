import psycopg2
from psycopg2 import sql
from doctor import Doctor
from patient import Patient
from db import get_connection  # Supondo que a função de conexão com o banco está no arquivo db.py

class Exam:
    # Método para cadastrar um exame no banco de dados
    def __init__(self, doctor_id: str = "", doctor_name: str = "",  patient_id: str = "", patient_name: str = "" , status: str = "", date: str = "", hour: str = ""):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.status = status
        self.date = date
        self.hour = hour


    def schedule(self, doctor: Doctor, patient: Patient, date: str, hour: str, status: str = "Agendado"):
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
        """Insere um novo exame no banco de dados."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = sql.SQL("""
                INSERT INTO exams (doctor_id, doctor_name, patient_id, patient_name, status, exam_date, exam_hour)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """)
            cur.execute(query, (self.doctor_id, self.doctor_name, self.patient_id, self.patient_name, self.status, self.date, self.hour))
            conn.commit()
            print(f"Exame cadastrado para {self.patient_name} com {self.doctor_name} em {self.date} às {self.hour}.")
        except Exception as e:
            print(f"Erro ao cadastrar exame: {e}")
        finally:
            cur.close()
            conn.close()


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
