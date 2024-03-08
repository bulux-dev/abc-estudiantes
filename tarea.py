from datetime import datetime, date
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
    cursor.execute("SELECT * FROM ingenieria")
except Exception as ex:
    print(ex)
    
    


def insertar_alumno(carnet, nombres, apellidos, correo_electronico, fecha_nacimiento, edad):


    if not isinstance(carnet, int):
        raise ValueError("El carnet debe ser un número entero")
    if not nombres or not isinstance(nombres, str):
        raise ValueError("Los nombres deben ser una cadena no vacía")
    if not apellidos or not isinstance(apellidos, str):
        raise ValueError("Los apellidos deben ser una cadena no vacía")
    if not correo_electronico or not isinstance(correo_electronico, str):
        raise ValueError("El correo electrónico debe ser una cadena no vacía")
    if not fecha_nacimiento or not isinstance(fecha_nacimiento, date):
        raise ValueError("La fecha de nacimiento debe ser una fecha válida")
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")


    try:
        cursor.execute("""
            INSERT INTO ingenieria (carnet, nombres, apellidos, correo, fecha_nacimiento_str, edad)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (carnet, nombres, apellidos, correo_electronico, fecha_nacimiento, edad))
        connection.commit()
    except psycopg2.Error as ex:
        print(f"Error al insertar datos: {ex}")
        connection.rollback()

carnet = int(input("Ingresa tu carnet:\n"))
nombres = input("Ingresa tus nombres:\n")
apellidos = input("Ingresa tus apellidos:\n")
correo_electronico = input("Ingresa tu correo electronico:\n")
fecha_nacimiento_str = str(input("Introduce tu fecha de nacimiento (YYYY-MM-DD): \n"))
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()

edad = (date.today() - fecha_nacimiento).days / 365.25

try:
    insertar_alumno(carnet, nombres, apellidos, correo_electronico, fecha_nacimiento, edad)
except ValueError as ex:
    print(ex)

print("conexion cerrada")


def obtener_estudiantes_por_carrera(carrera):
    cursor.execute("""
        SELECT * FROM ingenieria
        WHERE carrera = %s
    """, (carrera,))
    return cursor.fetchall()

carrera = input("Ingresa la carrera: ")
estudiantes = obtener_estudiantes_por_carrera(carrera)

for estudiante in estudiantes:
    print(f"Carnet: {estudiante[0]}")
    print(f"Nombres: {estudiante[1]}")
    print(f"Apellidos: {estudiante[2]}")
    print(f"Correo electrónico: {estudiante[3]}")
    print(f"Fecha de nacimiento: {estudiante[4]}")
    print(f"Edad: {estudiante[5]}")

print("conexion cerrada")

