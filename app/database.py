import os
import psycopg2 # type: ignore
from flask import g # type: ignore
from dotenv import load_dotenv # type: ignore
import json


# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos usando variables de entorno
DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),        
    'password': os.getenv('DB_PASSWORD'),     
    'host': os.getenv('DB_HOST'),            
    'database': os.getenv('DB_NAME'),        
    'port': os.getenv('DB_PORT', 5432)        
}

def test_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    conn.commit()
    cur.close()
    conn.close()

    print("TEST CONECTION - OK")


def create_table_users():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Users (
            Id         VARCHAR(10) PRIMARY KEY,
            NomApe     VARCHAR(30) NOT NULL,
            Direccion  VARCHAR(30) NOT NULL,
            Contacto   VARCHAR(25) NOT NULL
        );
        """
    )
    conn.commit()
   
    cur.close()
    conn.close()


def create_table_userAccess():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS UserAccess (
            Id         VARCHAR(10) PRIMARY KEY,
            Password   VARCHAR(20) NOT NULL 
        );
        """
    )

    conn.commit()
   
    cur.close()
    conn.close()

def load_users():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute("select count(*) from Users")
    result = cur.fetchone()
    row_count = result[0]
    if (row_count == 0):
        f = open('users.db')
        data = json.load(f)
        f.close()
        query_base = "INSERT INTO Users VALUES ('{}', '{}', '{}', '{}')"
        for user in data:
            query = query_base.format(user['Id'],user['NomApe'],user['Direccion'],user['Contacto'])
            cur.execute(query)

    conn.commit()
    cur.close()
    conn.close()

def load_access():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute("select count(*) from UserAccess")
    result = cur.fetchone()
    row_count = result[0]
    if (row_count == 0):
        f = open('userAccess.db')
        data = json.load(f)
        f.close()
        query_base = "INSERT INTO UserAccess VALUES ('{}', '{}')"
        for access in data:
            query = query_base.format(access['Id'],access['Password'])
            cur.execute(query)

    conn.commit()
    cur.close()
    conn.close()

# Función para obtener la conexión a la base de datos
def get_db():
    # Si 'db' no está en el contexto global de Flask 'g'
    if 'db' not in g:
        # Crear una nueva conexión a la base de datos y guardarla en 'g'
        g.db = psycopg2.connect(**DATABASE_CONFIG)
    # Retornar la conexión a la base de datos
    return g.db

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Extraer la conexión a la base de datos de 'g' y eliminarla
    db = g.pop('db', None)
    # Si la conexión existe, cerrarla
    if db is not None:
        db.close()

# Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
    # Registrar 'close_db' para que se ejecute al final del contexto de la aplicación
    app.teardown_appcontext(close_db)