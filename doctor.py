import psycopg2
from psycopg2 import sql
from db import get_connection

class Doctor:
    def __init__(self, name: str = "", specialty: str = "", service_hour: str = "", contact: str = "", salary: int = 0):
        self.name = name
        self.specialty = specialty
        self.service_hour = service_hour
        self.contact = contact
        self.salary = salary


    def cadastrar(self):
        """Insere um novo médico no banco de dados."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = sql.SQL("""
                INSERT INTO doctors (name, specialty, service_hour, contact, salary)
                VALUES (%s, %s, %s, %s, %s)
            """)
            cur.execute(query, (self.name, self.specialty, self.service_hour, self.contact, self.salary))
            conn.commit()
            print("Médico cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir médico: {e}")
        finally:
            cur.close()
            conn.close()


    @staticmethod
    def update(doctor_id, name, specialty, service_hour, contact, salary):
        """Atualiza os dados do médico no banco de dados."""
        conn = get_connection()
        if conn is None:
            print("Erro: não foi possível conectar ao banco de dados.")
            return

        cur = conn.cursor()
        try:
            query = """
                UPDATE doctors
                SET name = %s, specialty = %s, service_hour = %s, contact = %s, salary = %s
                WHERE id = %s
            """
            cur.execute(query, (name, specialty, service_hour, contact, salary, doctor_id))

            if cur.rowcount == 0:
                print(f"Nenhum registro atualizado. Verifique se o ID {doctor_id} existe.")
            else:
                print("Médico atualizado com sucesso!")
                
            conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar médico: {e}")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def remove(doctor_id: str):
        """Remove um médico pelo ID do banco de dados."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = "DELETE FROM doctors WHERE id = %s"
            cur.execute(query, (doctor_id,))
            conn.commit()
            print(f"Médico com ID '{doctor_id}' removido com sucesso!")
        except Exception as e:
            print(f"Erro ao remover médico: {e}")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def list_all():
        """Lista todos os médicos do banco de dados."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = "SELECT id, name, specialty, contact FROM doctors"
            cur.execute(query)
            doctors = cur.fetchall()
            for doctor in doctors:
                print(f"ID: {doctor[0]} | Nome: {doctor[1]} | Especialidade: {doctor[2]} | Contato: {doctor[3]}")
        except Exception as e:
            print(f"Erro ao listar médicos: {e}")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def list_by_name(name: str):
        """Lista todos os médicos cujo nome contenha a string informada (case insensitive)."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = "SELECT * FROM doctors WHERE name ILIKE %s"
            cur.execute(query, ('%' + name + '%',))
            doctors = cur.fetchall()
            
            if doctors:
                print("\nMédicos encontrados:")
                for doctor in doctors:
                    print(f"ID: {doctor[0]} | Nome: {doctor[1]} | Especialidade: {doctor[2]} | Contato: {doctor[4]}")
                    return True
            else:
                print(f"Nenhum médico encontrado com nome contendo '{name}'.")
                return False
            
        except Exception as e:
            print(f"Erro ao listar médicos: {e}")
            return False
        
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def search_by_id(doctor_id: str):
        """Busca um médico pelo ID no banco de dados."""
        conn = get_connection()
        cur = conn.cursor()
        try:
            query = """
                    SELECT id, name, specialty, service_hour, contact, salary
                    FROM doctors
                    WHERE id = %s
                """
            cur.execute(query, (doctor_id,))
            doctor = cur.fetchone()

            if doctor:
                return doctor
            else:
                print(f"Médico com ID '{doctor_id}' não encontrado.")
                return None
            
        except Exception as e:
            print(f"Erro ao buscar médico: {e}")
        finally:
            cur.close()
            conn.close()
