from sqlLibreria import conectar_bd, desconectar_bd
def realizar_venta():
    while True:
        conexion, cursor = conectar_bd("LibrerA.db")

        print("Para volver al menú principal, ingrese '0'")
        
        try:
            id_clientes = int(input("Ingrese el ID del Cliente: "))
        except ValueError:
            print("El ID debe ser un número entero.")
            desconectar_bd(conexion, cursor)
            continue

        if id_clientes == 0:
            desconectar_bd(conexion, cursor)
            break

        sentencia = """SELECT id
                       FROM clientes
                       WHERE id = ?"""
        cursor.execute(sentencia, (id_clientes,))
        cliente = cursor.fetchone()

        if cliente is None:
            print("El cliente no existe.")
            desconectar_bd(conexion, cursor)
            continue

        while True:
            try:
                id_libros = int(input("Ingrese el ID del Libro: "))
            except ValueError:
                print("El ID debe ser un número entero.")
                continue

            sentencia = """SELECT id
                           FROM libros
                           WHERE id = ?"""
            cursor.execute(sentencia, (id_libros,))
            libro = cursor.fetchone()

            if libro is None:
                print("El libro no existe.")
            else:
                break

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad vendida: "))
            except ValueError:
                print("La cantidad debe ser un número entero.")
                continue

            if cantidad <= 0:
                print("Ingrese una cantidad válida.")
                continue

            sentencia = """SELECT cantidad, valor 
                           FROM libros 
                           WHERE id = ?"""
            cursor.execute(sentencia, (id_libros,))
            libro = cursor.fetchone()

            if libro is None:
                print("El libro no existe.")
            elif cantidad > libro[0]:
                print(f"No hay suficientes cantidades disponibles. Stock disponible: {libro[0]}")
            else:
                break

        sentencia = """SELECT MAX(id) FROM ventas"""
        cursor.execute(sentencia)
        last_id = cursor.fetchone()[0]
        if last_id is None:
            id_venta = 1020
        else:
            id_venta = last_id + 5

        valor_total = cantidad * libro[1]
        nueva_cantidad = libro[0] - cantidad

        sentencia = """INSERT INTO ventas (id, id_clientes, id_libros, cantidad, valor_Total) 
                       VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(sentencia, (id_venta, id_clientes, id_libros, cantidad, valor_total))
        conexion.commit()

        sentencia = """UPDATE libros 
                       SET cantidad = ? 
                       WHERE id = ?"""
        cursor.execute(sentencia, (nueva_cantidad, id_libros))
        conexion.commit()

        desconectar_bd(conexion, cursor)
        print("Venta realizada exitosamente.")
        print(f"Código de venta: V-{id_venta}")


def actualizar_venta():
    codigo_venta = int(input("Ingrese el código de la venta (0 para salir): "))
    while codigo_venta != 0:
        conexion, cursor = conectar_bd("LibrerA.db")
        sentencia = """SELECT *
                        FROM ventas
                        WHERE id = ?"""
        cursor.execute(sentencia, (codigo_venta,))
        venta = cursor.fetchone()

        if venta is not None:
            cantidad_anterior = venta[3]
            unidades_anteriores_libro = obtener_unidades_libro(venta[2])
            precio_libro = obtener_precio_libro(venta[2])

            print("Datos de la venta:")
            print("Código de Venta:", venta[0])
            print("Código de Libro:", venta[2])
            print("Cantidad Vendida anterior:", cantidad_anterior)
            print("Unidades anteriores del Libro:", unidades_anteriores_libro)
            print("Precio del Libro:", precio_libro)
            print("=====================================")

            codigo_libro = int(input("Ingrese el codigo del libro: "))
            if codigo_libro == 0:
                codigo_libro = venta[2]

            nuevas_unidades = int(input("Ingrese la nueva cantidad vendida: "))
            print("=====================================")
            valor_Total = precio_libro * nuevas_unidades

            sentencia = """UPDATE ventas
                            SET id_libros = ?, cantidad = ?, valor_Total = ?
                            WHERE id = ?"""
            cursor.execute(sentencia, (codigo_libro, nuevas_unidades, valor_Total, codigo_venta))
            conexion.commit()
            

            utilizar_unidades_libro(venta[2], cantidad_anterior)  # Restauramos las unidades anteriores
            utilizar_unidades_libro(codigo_libro, -nuevas_unidades)  # Restamos las nuevas unidades

            print("_________________________________")
            print("Venta actualizada correctamente.")
            print("__________________________________")
        else:
            print("El ID de venta no se encuentra en la lista.")

        desconectar_bd(conexion, cursor)

        codigo_venta = int(input("Ingrese el código de la venta (0 para salir): "))



def obtener_unidades_libro(codigo_libro):
    conexion, cursor = conectar_bd("LibrerA.db")
    sentencia = """SELECT cantidad
                    FROM libros
                    WHERE id = ?"""
    cursor.execute(sentencia, (codigo_libro,))
    unidades_libro = cursor.fetchone()
    desconectar_bd(conexion, cursor)
    if unidades_libro is not None:
        return unidades_libro[0]
    return 0

def obtener_precio_libro(codigo_libro):
    conexion, cursor = conectar_bd("LibrerA.db")
    sentencia = """SELECT valor
                    FROM libros
                    WHERE id_libros = ?"""
    cursor.execute(sentencia, (codigo_libro,))
    precio_libro = cursor.fetchone()
    desconectar_bd(conexion, cursor)
    if precio_libro is not None:
        return precio_libro[0]
    return 0

def obtener_ultimo_id_venta():
    conexion, cursor = conectar_bd("LibrerA.db")
    sentencia = """SELECT MAX(id)
                    FROM ventas"""
    cursor.execute(sentencia)
    ultimo_codigo_venta = cursor.fetchone()[0]
    desconectar_bd(conexion, cursor)
    if ultimo_codigo_venta is not None:
        return ultimo_codigo_venta
    return 0

def obtener_unidades_libro(codigo_libro):
    conexion, cursor = conectar_bd("LibrerA.db")
    sentencia = """SELECT cantidad
                    FROM libros
                    WHERE id = ?"""
    cursor.execute(sentencia, (codigo_libro,))
    unidades_libro = cursor.fetchone()
    desconectar_bd(conexion, cursor)
    if unidades_libro is not None:
        return unidades_libro[0]
    return 0

def obtener_precio_libro(codigo_libro):
    conexion, cursor = conectar_bd("LibrerA.db")
    sentencia = """SELECT valor
                    FROM libros
                    WHERE id = ?"""
    cursor.execute(sentencia, (codigo_libro,))
    precio_libro = cursor.fetchone()
    desconectar_bd(conexion, cursor)
    if precio_libro is not None:
        return precio_libro[0]
    return 0

def obtener_ultimo_codigo_venta():
    conexion, cursor = conectar_bd("LibrerA.db")
    sentencia = """SELECT MAX(id)
                    FROM ventas"""
    cursor.execute(sentencia)
    ultimo_codigo_venta = cursor.fetchone()[0]
    desconectar_bd(conexion, cursor)
    if ultimo_codigo_venta is not None:
        return ultimo_codigo_venta
    return 0

def utilizar_unidades_libro(codigo_libro, nuevas_unidades):
    conexion, cursor = conectar_bd("LibrerA.db")
    unidades_anteriores = obtener_unidades_libro(codigo_libro)
    nuevas_unidades_totales = unidades_anteriores + nuevas_unidades
    sentencia = """UPDATE libros
                    SET cantidad = ?
                    WHERE id = ?"""
    cursor.execute(sentencia, (nuevas_unidades_totales, codigo_libro))
    conexion.commit()
    desconectar_bd(conexion, cursor)


def buscar_venta():
    conexion, cursor = conectar_bd("LibrerA.db")

    id_venta = input("Ingrese el ID de la venta: ")

    sentencia = """SELECT id, id_clientes, id_libros, cantidad, valor_Total
                   FROM ventas
                   WHERE id = ?"""
    cursor.execute(sentencia, (id_venta,))
    venta = cursor.fetchone()

    if venta:
        print("Información de la venta:")
        print("-----------------------")
        print(f"Código de venta: V-{venta[0]}")
        print(f"ID del Cliente: {venta[1]}")
        print(f"ID del Libro: {venta[2]}")
        print(f"Cantidad vendida: {venta[3]}")
        valor_total = int(venta[4])  # Convertir a entero
        print(f"Valor total: {valor_total}")
        print("-----------------------")
    else:
        print("La venta no existe.")

    desconectar_bd(conexion, cursor)


def lista_ventas():
    conexion, cursor = conectar_bd("LibrerA.db")

    sentencia = """SELECT id, id_clientes, id_libros, cantidad, valor_Total
                   FROM ventas"""
    cursor.execute(sentencia)
    ventas = cursor.fetchall()

    if ventas:
        print("Listado de Ventas:")
        print("------------------")
        for venta in ventas:
            print(f"Código de venta: V-{venta[0]}")
            print(f"ID del Cliente: {venta[1]}")
            print(f"ID del Libro: {venta[2]}")
            print(f"Cantidad vendida: {venta[3]}")
            print(f"Valor total: {venta[4]}")
            print("------------------")
    else:
        print("No hay ventas registradas.")

    desconectar_bd(conexion, cursor)


def eliminar_venta():
    codigo_venta = int(input("Ingrese el código de la venta que desea eliminar (0 para salir): "))
    while codigo_venta != 0:
        conexion, cursor = conectar_bd("LibrerA.db")
        sentencia = """SELECT *
                        FROM ventas
                        WHERE id = ?"""
        cursor.execute(sentencia, (codigo_venta,))
        venta = cursor.fetchone()

        if venta is not None:
            cantidad_vendida = venta[3]
            codigo_libro = venta[2]

            print("Datos de la venta a eliminar:")
            print("Código de Venta:", venta[0])
            print("Código de Libro:", codigo_libro)
            print("Cantidad Vendida:", cantidad_vendida)

            confirmacion = input("¿Está seguro/a de que desea eliminar esta venta? (s/n): ")
            if confirmacion == "s" or confirmacion == "S":
                restaurar_unidades = input("¿Desea restaurar las unidades del libro? (s/n): ")
                if restaurar_unidades == "s" or restaurar_unidades == "S":
                    utilizar_unidades_libro(codigo_libro, cantidad_vendida)  # Restaurar las unidades eliminadas

                sentencia = """DELETE FROM ventas WHERE id = ?"""
                cursor.execute(sentencia, (codigo_venta,))
                conexion.commit()

                print("Venta eliminada correctamente.")
            else:
                print("Operación cancelada.")

        else:
            print("El ID de venta no se encuentra en la lista.")

        desconectar_bd(conexion, cursor)

        codigo_venta = int(input("Ingrese el código de la venta que desea eliminar (0 para salir): "))
