import psycopg2
from psycopg2 import sql

# Função de conexão com o banco de dados
def get_connection():
    return psycopg2.connect(
        dbname="clinica_novamed",
        user="clinica_novamed_user",
        password="ho0RF4vnf0J7h6ItO9CvXOrIDYj3L5RD",
        host="dpg-cvg5d1lds78s73fqpbgg-a.oregon-postgres.render.com",
        port="5432"
    )
