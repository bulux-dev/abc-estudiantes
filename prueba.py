from datetime import datetime, date
import psycopg2
try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
        port='5433',
        database='ingenieria'
    )
    print("Conexion exitosa")
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM tb_ingenieria")
except Exception as ex:
    print(ex)
