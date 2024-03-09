from datetime import datetime, date
import psycopg2
try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
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

def menu():
  opcion = None
  while not opcion:
    print("**Menú**")
    print("1. Agregar")
    print("2. Borrar")
    print("3. Consultar")
    print("0. Salir")
    opcion = input("Ingrese una opción: ")

    if not opcion.isdigit():
      print("Opción inválida. Debe ingresar un número.")
      opcion = None

    elif int(opcion) < 0 or int(opcion) > 3:
      print("Opción fuera de rango. Debe elegir entre 0 y 3.")
      opcion = None

  return int(opcion)

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
            INSERT INTO tb_ingenieria (carnet, nombres, apellidos, correo, fecha_nacimiento_str, edad)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (carnet, nombres, apellidos, correo_electronico, fecha_nacimiento, edad))
        connection.commit()
    except psycopg2.Error as ex:
        print(f"Error al insertar datos: {ex}")
        connection.rollback()

def datos_para_registro():
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
    finally:
       connection.close()



def borrar_datos():
  print("Eliminar estudiante")
  carnet = int(input("Ingrese carnet a eliminar: "))
  try:
    cursor.execute("""
      DELETE FROM tb_ingenieria
      WHERE carnet = %s
    """, (carnet,))
    connection.commit()
    print("Estudiante eliminado.")
  except psycopg2.Error as ex:
    print(f"Error de compilacion: {ex}")
    connection.rollback()
  finally:
     connection.close()





def consulta_de_datos():
    print("**Consultar datos**")

    # Solicitar el campo de búsqueda
    carnet = input("Ingrese carnet de estudiante ")

    # Construir la consulta SQL
    consulta = f"SELECT * FROM tb_ingenieria WHERE carnet = '{carnet}'"

    try:
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        if resultados:
            print("Estudiante encontrado")
            for fila in resultados:
                print(fila)
        else:
            print(f"No se encontraron resultados para la búsqueda: {carnet}")

    except psycopg2.Error as ex:
        print(f"Error al realizar la consulta: {ex}")
    finally:
       connection.close()




def main():
  opcion = menu()

  if opcion == 1:
    datos_para_registro();
    pass
  elif opcion == 2:
    borrar_datos()
    pass
  elif opcion == 3:
    consulta_de_datos();
    pass
  else:
    print("Error")

if __name__ == "__main__":
  main()
