import psycopg2
from psycopg2 import sql
from doctor import Doctor
from patient import Patient
from db import get_connection

class Exam:
    def __init__(self, doctor: Doctor = None, patient: Patient = None, status: str = "", date: str = "", hour: str = "", id: str = None):
        self.id = id
        self.doctor = doctor
        self.patient = patient
        self.status = status
        self.date = date
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

    def register_exam(self, doctor_id, patient_id, exam_date, exam_time, status):
    # Registra um exame no banco de dados
        conn = get_connection()
        if conn is None:
            print("Erro: não foi possível conectar ao banco de dados.")
            return

        cursor = conn.cursor()
        try:
            # Query para inserir o exame
            query = """
                INSERT INTO exams (doctor_id, patient_id, exam_date, exam_time, status)
                VALUES (%s, %s, %s, %s, %s) RETURNING id
            """
            cursor.execute(query, (self.doctor.id, self.patient.id, self.date, self.hour, self.status))
            conn.commit()

            # Captura o id gerado pelo banco de dados
            exam_id = cursor.fetchone()[0]
            self.id = exam_id  # Atribui o id gerado ao objeto

            print(f"Exame cadastrado para {self.patient.name} com {self.doctor.name} em {self.date} às {self.hour}. ID: {exam_id}")

        except Exception as e:
            print(f"Erro ao registrar exame: {e}")
            conn.rollback()  # Caso ocorra algum erro, faz rollback da transação
        finally:
            cursor.close()
            conn.close()


    def update_exam(self):
        # Atualiza o status de um exame no banco de dados
        conn = get_connection()
        if conn is None:
            print("Erro: não foi possível conectar ao banco de dados.")
            return

        cursor = conn.cursor()
        try:
            query_update = """
                UPDATE exams 
                SET status = %s
                WHERE id = %s
            """
            cursor.execute(query_update, (self.status, self.id))  # Corrigido aqui
            conn.commit()
            print(f"Exame de {self.patient.name} com {self.doctor.name} atualizado para '{self.status}'.")

        except Exception as e:
            print(f"Erro ao atualizar exame: {e}")
            conn.rollback()  # Faz rollback em caso de erro
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
            conn.rollback()  # Faz rollback em caso de erro
        finally:
            cursor.close()
            conn.close()
