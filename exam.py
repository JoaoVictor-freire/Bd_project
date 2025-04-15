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

    def cancel(self):
        if self.id is None:
            print("ID do exame não definido.")
            return
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = sql.SQL("""
                UPDATE exams
                SET status = {}
                WHERE id = %s
            """).format(sql.Literal("Cancelado"))

            cur.execute(query, (self.id,))  # Usa o id armazenado na instância
            conn.commit()
            print(f"Exame com ID {self.id} atualizado para status 'Cancelado'.")
        except Exception as e:
            print(f"Erro ao atualizar status do exame: {e}")
        finally:
            cur.close()
            conn.close()


    def confirm(self):
        if self.id is None:
            print("ID do exame não definido.")
            return
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = sql.SQL("""
                UPDATE exams
                SET status = {}
                WHERE id = %s
            """).format(sql.Literal("Confirmado"))

            cur.execute(query, (self.id,))  # Usa o id armazenado na instância
            conn.commit()
            print(f"Exame com ID {self.id} atualizado para status 'Confirmado'.")
        except Exception as e:
            print(f"Erro ao atualizar status do exame: {e}")
        finally:
            cur.close()
            conn.close()


    def details(self):
        print(f"Exame ID: {self.id}")
        print(f"Paciente: {self.patient_name} | Médico: {self.doctor_name}")
        print(f"Data: {self.date} | Hora: {self.hour} | Status: {self.status}")

    # Método para registrar um exame no banco de dados
    def register_exam(self):
    # Insere um novo exame no banco de dados
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = sql.SQL("""
                INSERT INTO exams (doctor_id, doctor_name, patient_id, patient_name, status, exam_date, exam_hour)
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id
            """)
            cur.execute(query, (self.doctor_id, self.doctor_name, self.patient_id, self.patient_name, self.status, self.date, self.hour))
            exam_id = cur.fetchone()[0]  # Obtém o ID do exame recém-criado
            conn.commit()
            print(f"Exame cadastrado com ID {exam_id} para {self.patient_name} com {self.doctor_name} em {self.date} às {self.hour}.")
            return exam_id
        except Exception as e:
            print(f"Erro ao cadastrar exame: {e}")
        finally:
            cur.close()
            conn.close()


    def update_exam(self, exam_id, new_date, new_hour):
        conn = get_connection()
        cur = conn.cursor()
        try:
            # Atualiza data, hora e status do exame com base no ID
            query = sql.SQL("""
                UPDATE exams
                SET exam_date = %s, exam_hour = %s, status = 'Remarcado'
                WHERE id = %s
            """)
            # Passa os novos parâmetros: data e hora
            cur.execute(query, (new_date, new_hour, exam_id))
            conn.commit()
            print(f"Exame remarcado para data '{new_date}' e hora '{new_hour}' com status 'Remarcado'.")
        except Exception as e:
            print(f"Erro ao atualizar exame: {e}")
        finally:
            cur.close()
            conn.close()


    # Método para listar todos os exames do banco de dados
    @staticmethod
    def list_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.id, p.name, d.name, e.exam_date, e.exam_hour, e.status
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


    @staticmethod
    def search_by_patient_name(patient_name):
        """Lista todos os exames cujo nome do paciente contenha a string informada (case insensitive)."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT id, doctor_id, doctor_name, patient_id, patient_name, exam_date, exam_hour, status
                FROM exams
                WHERE patient_name ILIKE %s
            """, ('%' + patient_name + '%',))
            exams = cur.fetchall()

            if exams:
                print("\nExames encontrados:")
                for exam in exams:
                    print(f"ID: {exam[0]} | Paciente: {exam[4]} | Médico: {exam[2]} | Data: {exam[5]} | Hora: {exam[6]} | Status: {exam[7]}")
                return True
            else:
                print(f"Nenhum exame encontrado com nome do paciente contendo '{patient_name}'.")
                return False

        except Exception as e:
            print(f"Erro ao buscar exames: {e}")
            return False
        finally: 
            cur.close()
            conn.close()

    @staticmethod
    def search_by_id(exam_id):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT id, doctor_id, doctor_name, patient_id, patient_name, status, exam_date, exam_hour 
                FROM exams 
                WHERE id = %s
            """, (exam_id,))
            exam_data = cur.fetchone()
            if exam_data:
                # Cria a instância do Exam com os dados obtidos
                exam = Exam(
                    exam_data[1],  # doctor_id
                    exam_data[2],  # doctor_name
                    exam_data[3],  # patient_id
                    exam_data[4],  # patient_name
                    exam_data[5],  # status
                    exam_data[6],  # exam_date
                    exam_data[7]   # exam_hour
                )
                exam.id = exam_data[0]  # Atribui o ID retornado à instância
                return exam
            else:
                return None
        except Exception as e:
            print(f"Erro ao buscar exame: {e}")
            return None
        finally:
            cur.close()
            conn.close()
