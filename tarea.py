from datetime import datetime, date
from src.conexion_postgresql import connection

cursor = connection.cursor()



carnet = int(input("Ingresa tu carnet:\n"))
nombres = input("Ingresa tus nombres:\n")
apellidos = input("Ingresa tus apellidos:\n")
correo_electronico = input("Ingresa tu correo electronico:\n")
fecha_nacimiento_str = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

# Validar la cadena introducida...

fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()

edad = (date.today() - fecha_nacimiento).days / 365.25

print(f"Tu edad es: {edad:.2f} años")

def insertar_alumno(carnet, nombres, apellidos, correo_electronico, fecha_nacimiento,edad):

    cursor.execute(

        (carnet, nombres, apellidos, correo_electronico, fecha_nacimiento,edad),
    )
    connection.commit()
    connection.close()

insertar_alumno(carnet,nombres,apellidos,correo_electronico,fecha_nacimiento,edad)