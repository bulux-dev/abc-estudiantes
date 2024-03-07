from datetime import datetime, date

#import psycopg2

#conexion = psycopg2.connect(
 #   host='localhost',
 #   port='5432',
 #   database='tarea_ing_software',
 #   user='',
 #   password='admin'
#)



carnet = input("Ingresa tu carnet:\n")
nombres = input("Ingresa tus nombres:\n")
apellidos = input("Ingresa tus apellidos:\n")
correo = input("Ingresa tu correo electronico:\n")
fecha_nacimiento_str = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

# Validar la cadena introducida...

fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()

edad = (date.today() - fecha_nacimiento).days / 365.25

print(f"Tu edad es: {edad:.2f} años")
