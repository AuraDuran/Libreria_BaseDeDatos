from sqlLibreria import conectar_bd, desconectar_bd

def ingresar_cliente():
    while True:
        conexion, cursor = conectar_bd("LibrerA.db")

        print("Para volver al menú, ingrese '0' en el campo")
        print("_______________________________________")
        id = int(input("Ingrese el ID del Cliente: "))
        if id == 0:
            break

        # Verificar si el ID ya existe en la base de datos
        cursor.execute("SELECT id FROM clientes WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        if resultado is not None:
            print("__________________________________________")
            print("El código ya se encuentra registrado, intente nuevamente.")
            print("__________________________________________")
            desconectar_bd(conexion, cursor)
            continue  # Regresar al inicio del ciclo para volver a solicitar el ID

        nombre = input("Ingrese el nombre del Cliente: ")
        if nombre == '0':
            break

        nuevo_cliente = (id, nombre)
        print("_____________________")
        sentencia = """INSERT INTO clientes (id, nombre)
                       VALUES (?, ?)"""
        cursor.execute(sentencia, nuevo_cliente)
        conexion.commit()
        desconectar_bd(conexion, cursor)
        print("Cliente registrado exitosamente")


def lista_clientes():
  conexion,cursor=conectar_bd("LibrerA.db")

  print("---Lista de Clientes---")

  sentencia="""SELECT id,nombre
                FROM clientes"""
                
  cursor.execute(sentencia)

  clientes=cursor.fetchall()
  for id, nombre in clientes:
        print(f"ID: {id}, Nombre del cliente: {nombre}")
        print("______________________________________")

  desconectar_bd(conexion, cursor)


def actualizar_cliente():
    conexion, cursor = conectar_bd("LibrerA.db")

    sentencia = """SELECT id, nombre
                FROM clientes"""
    cursor.execute(sentencia)
    clientes = cursor.fetchall()

    for id, nombre in clientes:
        print(f"ID: {id}, Nombre del cliente: {nombre}")
        print("______________________________________")

    id_actualizar = int(input("Ingrese el ID del Cliente a actualizar: "))

    nuevo_id = None
    while nuevo_id is None:
        try:
            nuevo_id = int(input("Si desea, ingrese un nuevo ID para el Cliente: "))
        except ValueError:
            print("Error: El ID debe ser un número entero. Inténtelo nuevamente.")

    nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
    print()

    sentencia = """UPDATE clientes
             SET id=?, nombre=?
             WHERE id=?"""

    parametros = [nuevo_id, nuevo_nombre, id_actualizar]
    cursor.execute(sentencia, parametros)
    conexion.commit()

    sentencia = """SELECT id, nombre
                FROM clientes"""
    cursor.execute(sentencia)
    clientes = cursor.fetchall()

    for id, nombre in clientes:
        if id == nuevo_id:
            print(f"ID: {id}, Nombre del cliente: {nombre}")
            print("______________________________________")
            break

    desconectar_bd(conexion, cursor)


def buscar_cliente():
    conexion, cursor = conectar_bd("LibrerA.db")

    id = int(input("Ingrese el ID del Cliente a buscar: "))

    sentencia = """SELECT * FROM clientes
                 WHERE id=?"""
    parametros = [id]

    cursor.execute(sentencia, parametros)

    clientes = cursor.fetchall()
    if len(clientes) == 0:
        print("No se encontró ningún cliente con el ID Ingresado.")
    else:
        for id, nombre in clientes:
            print(f"ID: {id}, Nombre del cliente: {nombre}")
            print("______________________________________")

    desconectar_bd(conexion, cursor)


def eliminar_cliente():
    conexion, cursor = conectar_bd("LibrerA.db")

    sentencia = """SELECT * FROM clientes"""
    cursor.execute(sentencia)
    clientes = cursor.fetchall()
    for id, nombre in clientes:
        print(f"ID: {id}, Nombre del cliente: {nombre}")
        print("______________________________________")

    id = None
    while id is None:
        try:
            id_input = input("Ingrese ID del Cliente a eliminar (0 para salir): ")
            if id_input == "0":
                desconectar_bd(conexion, cursor)
                return
            id = int(id_input)
        except ValueError:
            print("Error: El ID debe ser un número entero. Inténtelo nuevamente.")

    sentencia_compras = """SELECT COUNT(*) FROM ventas WHERE id_clientes = ?"""
    cursor.execute(sentencia_compras, [id])
    resultado = cursor.fetchone()
    if resultado[0] > 0:
        print("No se puede eliminar el cliente. Ha realizado una o más compras.")
        desconectar_bd(conexion, cursor)
        return

    sentencia_cliente = """SELECT * FROM clientes WHERE id = ?"""
    cursor.execute(sentencia_cliente, [id])
    cliente = cursor.fetchone()

    print(f"Cliente encontrado: ID: {cliente[0]}, Nombre: {cliente[1]}")
    confirmacion = input("¿Está seguro de que desea eliminar a este cliente? (S/N): ")

    if confirmacion.upper() != "S":
        print("Operación cancelada. No se ha eliminado al cliente.")
        desconectar_bd(conexion, cursor)
        return

    sentencia = """DELETE FROM clientes WHERE id = ?;"""
    parametros = [id]
    cursor.execute(sentencia, parametros)
    conexion.commit()

    print(f"Cliente {cliente[0]} - {cliente[1]} eliminado con éxito")
    print()

    desconectar_bd(conexion, cursor)