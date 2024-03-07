import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
        database='tarea_ing_software'
    )
    print("Conexion exitosa")
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM tb_estudiantes")
except Exception as ex:
    print(ex)
    
