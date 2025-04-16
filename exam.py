import psycopg2
from psycopg2 import sql
from doctor import Doctor
from patient import Patient
from db import get_connection  # Supondo que a função de conexão com o banco está no arquivo db.py

class Exam:
    # Método para cadastrar um exame no banco de dados
    def __init__(self, doctor_id: str = "", doctor_name: str = "",  patient_id: str = "", patient_name: str = "" , payment_method: str = "", date: str = "", hour: str = "", price = 100.0):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.payment_method = payment_method
        self.date = date
        self.hour = hour
        self.price = float(price)
        self.discount_applied = False
        self.final_price = self.price

    @staticmethod
    def get_patient_tags_and_city(patient_id):
        """Busca tags e cidade do paciente para verificar se há direito a desconto."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT tags, city FROM patients WHERE id = %s", (patient_id,))
            result = cur.fetchone()
            return result if result else ("", "")
        except Exception as e:
            print(f"Erro ao buscar tags do paciente: {e}")
            return ("", "")
        finally:
            cur.close()
            conn.close()

    def apply_discount_if_eligible(self):
        tags, city = self.get_patient_tags_and_city(self.patient_id)
        tags = tags.lower() if tags else ""
        city = city.lower() if city else ""

        if "flamengo" in tags or "one piece" in tags or "sousa" in city:
            self.discount_applied = True
            self.final_price = round(self.price * 0.9, 2)  # Aplica 10% de desconto
        else:
            self.final_price = self.price


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


    @staticmethod
    def register_exam(exam):
        """Registra o exame no banco, aplicando desconto se for elegível."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            # Aplica regra de desconto
            exam.apply_discount_if_eligible()

            query = """
                INSERT INTO exams (
                    doctor_id, doctor_name, patient_id, patient_name,
                    payment_method, exam_date, exam_hour,
                    price, discount_applied, final_price, payment_status
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (
                exam.doctor_id,
                exam.doctor_name,
                exam.patient_id,
                exam.patient_name,
                exam.payment_method,
                exam.date,
                exam.hour,
                exam.price,
                exam.discount_applied,
                exam.final_price,
                "Agendado"
            ))

            conn.commit()
            print(f"Exame cadastrado com sucesso! Valor final: R$ {exam.final_price:.2f}")
        except Exception as e:
            print(f"Erro ao registrar exame: {e}")
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
        """Lista todos os exames registrados no sistema."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = """
                SELECT 
                    id, doctor_name, patient_name, exam_date, exam_hour,
                    price, discount_applied, final_price, payment_method, payment_status
                FROM exams
            """
            cur.execute(query)
            exams = cur.fetchall()

            print("\nLista de Exames Registrados:")
            for exam in exams:
                print(
                    f"\nID: {exam[0]}\n"
                    f"Médico: {exam[1]}\n"
                    f"Paciente: {exam[2]}\n"
                    f"Data: {exam[3]} | Hora: {exam[4]}\n"
                    f"Valor Original: R$ {exam[5]:.2f}\n"
                    f"Desconto Aplicado: {'Sim' if exam[6] else 'Não'}\n"
                    f"Valor Final: R$ {exam[7]:.2f}\n"
                    f"Pagamento: {exam[8]} ({exam[9]})"
                )
        except Exception as e:
            print(f"Erro ao listar exames: {e}")
        finally:
            cur.close()
            conn.close()

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
    def list_with_discount():
        """Lista todos os exames com desconto aplicado (usando a VIEW)."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = "SELECT * FROM exams_with_discount"
            cur.execute(query)
            exams = cur.fetchall()

            print("\nExames com Desconto Aplicado:")
            for exam in exams:
                print(
                    f"\nID: {exam[0]}\n"
                    f"Médico: {exam[1]}\n"
                    f"Paciente: {exam[2]}\n"
                    f"Data: {exam[3]} | Hora: {exam[4]}\n"
                    f"Valor Original: R$ {exam[5]:.2f}\n"
                    f"Valor Final com Desconto: R$ {exam[6]:.2f}\n"
                    f"Pagamento: {exam[7]} ({exam[8]})"
                )
        except Exception as e:
            print(f"Erro ao listar exames com desconto: {e}")
        finally:
            cur.close()
            conn.close()
    
    @staticmethod
    def relatorio_mensal_por_data():
        """Executa o relatório mensal por médico com mês e ano informados."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            mes = input("Digite o número do mês (1 a 12): ")
            ano = input("Digite o ano (ex: 2025): ")

            mes = int(mes)
            ano = int(ano)

            cur.execute("CALL relatorio_mensal_por_medico(%s, %s);", (mes, ano))
            print(f"Relatório de {mes}/{ano} gerado com sucesso (veja a saída no console SQL).")

        except Exception as e:
            print(f"Erro ao executar o relatório mensal: {e}")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def filter_by_price_range():
        """Filtra exames por uma faixa de preço informada pelo usuário."""
        try:
            min_price = float(input("Digite o valor mínimo: R$ "))
            max_price = float(input("Digite o valor máximo: R$ "))
        except ValueError:
            print("Valores inválidos. Tente novamente com números.")
            return

        conn = get_connection()
        cur = conn.cursor()
        try:
            query = """
                SELECT 
                    id, doctor_name, patient_name, exam_date, exam_hour,
                    price, final_price, discount_applied
                FROM exams
                WHERE price BETWEEN %s AND %s
            """
            cur.execute(query, (min_price, max_price))
            exams = cur.fetchall()

            if exams:
                print(f"\nExames com valor entre R$ {min_price:.2f} e R$ {max_price:.2f}:")
                for exam in exams:
                    print(
                        f"\nID: {exam[0]}\n"
                        f"Médico: {exam[1]}\n"
                        f"Paciente: {exam[2]}\n"
                        f"Data: {exam[3]} | Hora: {exam[4]}\n"
                        f"Valor Original: R$ {exam[5]:.2f}\n"
                        f"Valor Final: R$ {exam[6]:.2f} {'(com desconto)' if exam[7] else ''}"
                    )
            else:
                print("Nenhum exame encontrado na faixa de preço informada.")
        except Exception as e:
            print(f"Erro ao filtrar exames por preço: {e}")
        finally:
            cur.close()
            conn.close()

