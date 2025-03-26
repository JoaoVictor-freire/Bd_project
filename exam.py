import psycopg2
from psycopg2 import sql
from doctor import Doctor
from patient import Patient
from secrets import token_urlsafe
from db import get_connection

class Exam:
    def __init__(self, doctor: Doctor = None, patient: Patient = None, status: str = "", date: str = "", hour: str = "", id: str = None):
        self.id = id or token_urlsafe(8)  # Gera um ID único se não for fornecido
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
        print(f"Paciente: {self.patient.name} | Médico: {self.doctor.name}")
        print(f"Data: {self.date} | Hora: {self.hour} | Status: {self.status}")

    def register_exam(self):
        # Registra um exame no banco de dados
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO exams (id, doctor_id, patient_id, status, exam_date, exam_time)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (self.id, self.doctor.id, self.patient.id, self.status, self.date, self.hour))
            conn.commit()
            print(f"Exame cadastrado para {self.patient.name} com {self.doctor.name} em {self.date} às {self.hour}.")
        except Exception as e:
            print(f"Erro ao registrar exame: {e}")
        finally:
            cursor.close()
            conn.close()

    def update_exam(self):
        # Atualiza o status de um exame no banco de dados
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
                UPDATE exams 
                SET status = %s
                WHERE id = %s
            """
            cursor.execute(query, (self.status, self.id))
            conn.commit()
            print(f"Exame de {self.patient.name} com {self.doctor.name} atualizado para '{self.status}'.")
        except Exception as e:
            print(f"Erro ao atualizar exame: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def list_all():
        # Lista todos os exames no banco de dados
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        SELECT e.id, p.name, d.name, e.exam_date, e.exam_time, e.status
                        FROM exams e
                        JOIN patients p ON e.patient_id = p.id
                        JOIN doctors d ON e.doctor_id = d.id
                    """)
                    exams = cursor.fetchall()

                    if not exams:
                        print("Nenhum exame registrado.")
                    else:
                        print("\nLista de Exames:")
                        for exam in exams:
                            print(f"ID: {exam[0]} | Paciente: {exam[1]} | Médico: {exam[2]} | Data: {exam[3]} | Hora: {exam[4]} | Status: {exam[5]}")
        except Exception as e:
            print(f"Erro ao listar exames: {e}")

    @staticmethod
    def remove(exam_id: str):
        # Remove um exame do banco de dados
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM exams WHERE id = %s", (exam_id,))
            conn.commit()
            print(f"Exame com ID '{exam_id}' removido com sucesso!")
        except Exception as e:
            print(f"Erro ao remover exame: {e}")
        finally:
            cursor.close()
            conn.close()
