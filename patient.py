import psycopg2
from secrets import token_urlsafe
from db import get_connection
from psycopg2 import sql

class Patient:
    # Método para criar um paciente no banco de dados
    def __init__(self, name: str = "", age: int = 0, history: str = "", contact: str = "", address: str = "", id: str = None):
        self.name = name
        self.age = age
        self.history = history
        self.contact = contact
        self.address = address


    # Método para registrar o paciente no banco de dados
    def cadastrar(self):
        """Insere um novo paciente no banco de dados."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = sql.SQL("""
                INSERT INTO patients (name, age, history, contact, address)
                VALUES (%s, %s, %s, %s, %s)
            """)
            cur.execute(query, (self.name, self.age, self.history, self.contact, self.address))
            conn.commit()
            print(f"Paciente {self.name} cadastrado com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir paciente: {e}")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def update(patient_id, name, age, history, contact, address):
        """Atualiza os dados do paciente no banco de dados."""
        conn = get_connection()
        if conn is None:
            print("Erro: não foi possível conectar ao banco de dados.")
            return

        cur = conn.cursor()
        try:
            query = """
                UPDATE patients
                SET name = %s, age = %s, history = %s, contact = %s, address = %s
                WHERE id = %s
            """
            cur.execute(query, (name, age, history, contact, address, patient_id))

            if cur.rowcount == 0:
                print(f"Nenhum registro atualizado. Verifique se o ID {patient_id} existe.")
            else:
                print("Paciente atualizado com sucesso!")

            conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar paciente: {e}")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def remove(patient_id: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM patients WHERE id = %s
        """, (patient_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Paciente com ID '{patient_id}' removido com sucesso!")

    @staticmethod
    def list_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, name, age, history, contact, address
            FROM patients
        """)
        patients = cursor.fetchall()
        cursor.close()
        conn.close()

        print("\nLista de Pacientes:")
        for patient in patients:
            print(f"ID: {patient[0]} | Nome: {patient[1]} | Idade: {patient[2]} | Histórico: {patient[3]} | Contato: {patient[4]}")


    @staticmethod
    def list_by_name(name: str):
        """Lista todos os pacientes cujo nome contenha a string informada."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = """
                SELECT id, name, age, history, contact, address
                FROM patients
                WHERE name ILIKE %s
            """
            cur.execute(query, (f"%{name}%",))
            patients = cur.fetchall()
            
            if patients:
                print("\nPacientes encontrados:")
                for p in patients:
                    print(f"ID: {p[0]} | Nome: {p[1]} | Idade: {p[2]} | Histórico: {p[3]} | Contato: {p[4]}")
                    return True
            else:
                print(f"Nenhum paciente encontrado com nome contendo '{name}'.")
                return False
            
        except Exception as e:
            print(f"Erro ao buscar pacientes: {e}")
            return False
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def search_by_id(patient_id: str):
        """Busca um paciente pelo ID no banco de dados."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = """
                SELECT id, name, age, history, contact, address
                FROM patients
                WHERE id = %s
            """
            cur.execute(query, (patient_id,))
            patient = cur.fetchone()
            if patient:
                return patient
            else:
                print(f"Paciente com ID '{patient_id}' não encontrado.")
                return None
        except Exception as e:
            print(f"Erro ao buscar paciente: {e}")
        finally:
            cur.close()
            conn.close()
