import psycopg2
from secrets import token_urlsafe
from db import get_connection

class Patient:
    # Método para criar um paciente no banco de dados
    def __init__(self, name: str = "", age: int = 0, history: str = "", contact: str = "", address: str = "", id: str = None):
        self.id = id or token_urlsafe(10)
        self.name = name
        self.age = int(age)
        self.history = history
        self.contact = contact
        self.address = address

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHistory(self):
        return self.history

    def getContact(self):
        return self.contact

    def getAddress(self):
        return self.address

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setHistory(self, history):
        self.history = history

    def setContact(self, contact):
        self.contact = contact

    def setAddress(self, address):
        self.address = address

    # Método para registrar o paciente no banco de dados
    def cadastrar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO patients (id, name, age, history, contact, address)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (self.id, self.name, self.age, self.history, self.contact, self.address))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Paciente {self.name} cadastrado com sucesso.")

    # Método para atualizar o paciente no banco de dados
    def update_patient(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE patients
            SET name = %s, age = %s, history = %s, contact = %s, address = %s
            WHERE id = %s
        """, (self.name, self.age, self.history, self.contact, self.address, self.id))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Paciente {self.name} atualizado com sucesso.")

    # Método para consultar pacientes pelo nome
    @staticmethod
    def consult(name: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, name, age, history, contact, address
            FROM patients
            WHERE name ILIKE %s
        """, ('%' + name + '%',))
        patients = cursor.fetchall()
        cursor.close()
        conn.close()

        if patients:
            print(f"\nPacientes encontrados com o nome contendo '{name}':")
            for patient in patients:
                print(f"ID: {patient[0]} | Nome: {patient[1]} | Idade: {patient[2]} | Histórico: {patient[3]} | Contato: {patient[4]}")
        else:
            print(f"Nenhum paciente com nome contendo '{name}' foi encontrado.")

    # Método para listar todos os pacientes
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

    # Método para remover um paciente do banco de dados
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

    # Método para listar um paciente pelo nome exato
    @staticmethod
    def listOne(name: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, name, age, history, contact, address
            FROM patients
            WHERE name = %s
        """, (name,))
        patient = cursor.fetchone()
        cursor.close()
        conn.close()

        if patient:
            print(f"\nPaciente encontrado:\nID: {patient[0]} | Nome: {patient[1]} | Idade: {patient[2]} | Histórico: {patient[3]} | Contato: {patient[4]}")
        else:
            print(f"Paciente '{name}' não encontrado.")

    # Método para buscar um paciente pelo ID
    @staticmethod
    def search_by_id(patient_id: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, name, age, history, contact, address
            FROM patients
            WHERE id = %s
        """, (patient_id,))
        patient = cursor.fetchone()
        cursor.close()
        conn.close()

        if patient:
            return Patient(patient[1], patient[2], patient[3], patient[4], patient[5], patient[0])
        return None  # Retorna None se não encontrar
