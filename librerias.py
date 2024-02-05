from sql_librerias import conectar_db,desconectar_db
from prettytable import PrettyTable

clientes=[["juan",3100]]
#nombre del cliente, codigo del cliente
libros=[]
#codigo del libro ISBN, titulo del libro,precio del libro, unidades de libros disponibles
ventas=[]
#codigo de venta (generado automaticamente),codigo del cliente,codigo del libro,cantidad vendida,valor de la venta

#["maria",3101],["pedro",3102],["laura",3103]
#[12552,"iliada",5300,25],[12553,"platero",2500,16],[12554,"cien",3600,35]
def menu_clientes():
    while True:
        print("==== Menú clientes ====")
        print("1 - Ingresar clientes")
        print("2 - Lista de clientes")
        print("3 - Borrar cliente")
        print("4 - Buscar cliente")
        print("5 - Actualizar cliente")
        print("6 - Salir")
        opcion1 = input("Ingrese una opción: ")

        if opcion1 == '1':
            ingresar_clientes(clientes)
        elif opcion1 == '2':
            lista_clientes(clientes)
        elif opcion1 == '3':
            borrar_cliente(clientes)
        elif opcion1 == '4':
            buscar_cliente(clientes)
        elif opcion1 == '5':
            actualizar_cliente(clientes)
        elif opcion1 == '6':
            break
        else:
            print("Opción inválida - intente nuevamente")

def ingresar_clientes(clientes):
    while True:
        conexion, cursor = conectar_db("librerias.db")
        print("===============================================")
        print("Para salir, ingrese '0' en ambos campos.")
        nombre = input("Ingrese el nombre del cliente: ")
        if nombre == '0':
            break
        while True:
            id_cliente = int(input("Ingrese el código del cliente: "))
            if id_cliente == 0:
                break
            
            codigo_repetido = False
            for cliente in clientes:
                if id_cliente == cliente[0]:  
                    codigo_repetido = True
                    print("================================================")
                    print()
                    print("El código ya ha sido registrado - intente nuevamente.")
                    print()
                    print("================================================")
                    break
            if not codigo_repetido:
                break
        if id_cliente == 0:
            break
        lista_clientes = []
        lista_clientes.append(id_cliente)
        lista_clientes.append(nombre)
        print("===============================================")
        sentencia = """INSERT INTO clientes(id_cliente, nombre)
                        VALUES (?, ?)
        """
        cursor.execute(sentencia, lista_clientes)
        conexion.commit()
        desconectar_db(conexion, cursor)
        print("Cliente registrado exitosamente.")

def lista_clientes(clientes):
    conexion, cursor = conectar_db("librerias.db")
    print("=========================================")
    sentencia = """SELECT *
                FROM  clientes
    """
    cursor.execute(sentencia)
    clientes = cursor.fetchall()
    tabla_clientes = PrettyTable(("id_cliente", "nombre"))
    for id_cliente, nombre in clientes:
        tabla_clientes.add_row([id_cliente, nombre])
    print(tabla_clientes)  
    desconectar_db(conexion, cursor)
    print("=========================================")

def borrar_cliente(clientes):
    while True:
        print("=======================================")
        print("Para salir, ingrese '0'")
        codigo = int(input("Ingrese el código del cliente a borrar: "))
        if codigo == 0:
            break
        conexion, cursor = conectar_db("librerias.db")
        print("=======================================")
        sentencia = """DELETE FROM clientes
                    WHERE id_cliente = ?
        """
        cursor.execute(sentencia, (codigo,))
        conexion.commit()
        desconectar_db(conexion, cursor)
        print("Cliente borrado exitosamente.")

def buscar_cliente(clientes):
    while True:
        print("=======================================")
        print("Para salir, ingrese '0'")
        codigo = int(input("Ingrese el código del cliente a buscar: "))
        if codigo == 0:
            break
        conexion, cursor = conectar_db("librerias.db")
        print("=======================================")
        sentencia = """SELECT *
                    FROM clientes
                    WHERE id_cliente = ?
        """
        cursor.execute(sentencia, (codigo,))
        cliente = cursor.fetchone()
        if cliente:
            print(f"Cliente encontrado: Código: {cliente[0]}, Nombre: {cliente[1]}")
        else:
            print("Cliente no encontrado.")
        desconectar_db(conexion, cursor)

def actualizar_cliente(clientes):
    while True:
        print("=======================================")
        print("Para salir, ingrese '0'")
        codigo = int(input("Ingrese el código del cliente a actualizar: "))
        if codigo == 0:
            break
        conexion, cursor = conectar_db("librerias.db")
        sentencia = """SELECT *
                    FROM clientes
                    WHERE id_cliente = ?
        """
        cursor.execute(sentencia, (codigo,))
        cliente = cursor.fetchone()
        if cliente:
            print("=======================================")
            print(f"Cliente encontrado: Código: {cliente[0]}, Nombre: {cliente[1]}")
            print("=======================================")
            nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
            sentencia = """UPDATE clientes
                        SET nombre = ?
                        WHERE id_cliente = ?
            """
            cursor.execute(sentencia, (nuevo_nombre, codigo))
            conexion.commit()
            desconectar_db(conexion, cursor)
            print("Cliente actualizado exitosamente.")
        else:
            print("Cliente no encontrado.")

def menu_libros():
    while True:
        print("==== Menú libros ====")
        print("1 - Ingresar libros")
        print("2 - Lista de libros")
        print("3 - Borrar libro")
        print("4 - Buscar libro")
        print("5 - Actualizar libro")
        print("6 - Salir")
        opcion1 = input("Ingrese una opción: ")

        if opcion1 == '1':
            ingresar_libros(libros)
        elif opcion1 == '2':
            lista_libros(libros)
        elif opcion1 == '3':
            borrar_libro(libros)
        elif opcion1 == '4':
            buscar_libro(libros)
        elif opcion1 == '5':
            actualizar_libro(libros)
        elif opcion1 == '6':
            break
        else:
            print("Opción inválida - intente nuevamente")

def ingresar_libros(libros):
    while True:
        conexion, cursor = conectar_db("librerias.db")
        print("===============================================")
        print("Para salir, ingrese '0' en ambos campos.")
        codigo = input("Ingrese el código del libro (ISBN): ")
        if codigo == '0':
            break
        titulo = input("Ingrese el título del libro: ")
        if titulo == '0':
            break
        precio = float(input("Ingrese el precio del libro: "))
        if precio == 0:
            break
        unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
        if unidades == 0:
            break
        
        codigo_repetido = False
        for libro in libros:
            if codigo == libro[0]:  
                codigo_repetido = True
                print("================================================")
                print()
                print("El código ISBN ya ha sido registrado - intente nuevamente.")
                print()
                print("================================================")
                break
        if not codigo_repetido:
            libros.append([codigo, titulo, precio, unidades])
            sentencia = """INSERT INTO libros(id_libros,nombre,precio,unidades)
                            VALUES (?, ?, ?, ?)
            """
            cursor.execute(sentencia, (codigo, titulo, precio, unidades))
            conexion.commit()
            desconectar_db(conexion, cursor)
            print("Libro registrado exitosamente.")

def lista_libros(libros):
    conexion, cursor = conectar_db("librerias.db")
    print("=========================================")
    sentencia = """SELECT *
                FROM  libros
    """
    cursor.execute(sentencia)
    libros = cursor.fetchall()
    tabla_libros = PrettyTable(("ISBN", "Título", "Precio", "Unidades"))
    for libro in libros:
        tabla_libros.add_row(libro)
    print(tabla_libros)
    desconectar_db(conexion, cursor)
    print("=========================================")

def borrar_libro(libros):
    while True:
        print("=========================================")
        print("Para salir, ingrese '0'")
        codigo = input("Ingrese el código del libro a borrar: ")
        if codigo == '0':
            break
        conexion, cursor = conectar_db("librerias.db")
        print("=========================================")
        sentencia = """DELETE FROM libros
                    WHERE id_libros = ?
        """
        cursor.execute(sentencia, (codigo,))
        conexion.commit()
        desconectar_db(conexion, cursor)
        if cursor.rowcount > 0:
            libros[:] = [libro for libro in libros if libro[0] != codigo]
            print("Libro borrado exitosamente.")
        else:
            print("No se encontró el libro.")

def buscar_libro(libros):
    while True:
        print("=========================================")
        print("Para salir, ingrese '0'")
        codigo = input("Ingrese el código del libro a buscar: ")
        if codigo == '0':
            break
        conexion, cursor = conectar_db("librerias.db")
        print("=========================================")
        sentencia = """SELECT *
                    FROM libros
                    WHERE id_libros = ?
        """
        cursor.execute(sentencia, (codigo,))
        libro = cursor.fetchone()
        if libro:
            print(f"Libro encontrado: ISBN: {libro[0]}, Título: {libro[1]}, Precio: {libro[2]}, Unidades: {libro[3]}")
        else:
            print("Libro no encontrado.")
        desconectar_db(conexion, cursor)

def actualizar_libro(libros):
    while True:
        print("=========================================")
        print("Para salir, ingrese '0'")
        codigo = input("Ingrese el código del libro a actualizar: ")
        if codigo == '0':
            break
        conexion, cursor = conectar_db("librerias.db")
        sentencia = """SELECT *
                    FROM libros
                    WHERE id_libros = ?
        """
        cursor.execute(sentencia, (codigo,))
        libro = cursor.fetchone()
        if libro:
            print("=========================================")
            print(f"Libro encontrado: ISBN: {libro[0]}, Título: {libro[1]}, Precio: {libro[2]}, Unidades: {libro[3]}")
            print("=========================================")
            nuevo_titulo = input("Ingrese el nuevo título del libro (deje en blanco para mantener el actual): ")
            if nuevo_titulo == '0':
                break
            nuevo_precio = input("Ingrese el nuevo precio del libro (deje en blanco para mantener el actual): ")
            if nuevo_precio == '0':
                break
            nueva_unidades = input("Ingrese la nueva cantidad de unidades disponibles (deje en blanco para mantener la actual): ")
            if nueva_unidades == '0':
                break

            # Crear una lista temporal y asignar los valores actualizados
            nuevo_libro = list(libro)
            if nuevo_titulo.strip():
                nuevo_libro[1] = nuevo_titulo
            if nuevo_precio.strip():
                nuevo_libro[2] = float(nuevo_precio)
            if nueva_unidades.strip():
                nuevo_libro[3] = int(nueva_unidades)

            # Convertir la lista temporal de nuevo a una tupla
            nuevo_libro = tuple(nuevo_libro)

            sentencia = """UPDATE libros
                        SET nombre = ?, precio = ?, unidades = ?
                        WHERE id_libros = ?
            """
            cursor.execute(sentencia, (nuevo_libro[1], nuevo_libro[2], nuevo_libro[3], codigo))
            conexion.commit()
            desconectar_db(conexion, cursor)
            print("Libro actualizado exitosamente.")
        else:
            print("Libro no encontrado.")

def menu_ventas():
    while True:
        print("==== Menu Ventas ====")
        print("1 - Realizar venta")
        print("2 - Lista de ventas realizadas")
        print("3 - Buscar venta realizada")
        print("4 - Borrar venta")
        print("5 - Actualizar venta")
        print("6 - Salir")
        opcion4 = input("Ingrese una opción: ")
        if opcion4 == '1':
            registrar_venta()
        elif opcion4 == '2':
            mostrar_ventas()
        elif opcion4 == '3':
            buscar_venta_menu()
        elif opcion4 == '4':
            eliminar_venta()
        elif opcion4 == '5':
            actualizar_venta()
        elif opcion4 == '6':
            break
        else:
            print("Opción inválida")

def registrar_venta():
    while True:
        print("===========================================")
        print("Para salir, ingrese '0'")
        id_cliente = int(input("Ingrese el código del cliente: "))
        conexion, cursor = conectar_db("librerias.db")
        if id_cliente == 0:
            break
        sentencia = """SELECT id_cliente
                        FROM clientes"""
        cursor.execute(sentencia)
        clientes = cursor.fetchall()
        cliente_encontrado = False
        for cliente in clientes:
            if cliente[0] == id_cliente:
                cliente_encontrado = True
                break
        if not cliente_encontrado:
            print("El cliente no existe.")
            desconectar_db(conexion, cursor)
            continue
        while True:
            codigo_libro = int(input("Ingrese el código del libro: "))
            sentencia = """SELECT id_libros
                            FROM libros"""
            cursor.execute(sentencia)
            libros = cursor.fetchall()
            libro_encontrado = False
            for libro in libros:
                if libro[0] == codigo_libro:
                    libro_encontrado = True
                    break
            if not libro_encontrado:
                print("El libro no existe.")
            else:
                break
        while True:
            cantidad = int(input("Ingrese la cantidad vendida: "))
            if cantidad <= 0:
                print("Ingrese una cantidad válida.")
            else:
                break
        sentencia = """SELECT unidades, precio
                        FROM libros
                        WHERE id_libros = ?"""
        cursor.execute(sentencia, (codigo_libro,))
        libro = cursor.fetchone()
        if libro is None:
            print("El libro no existe.")
        elif cantidad > libro[0]:
            print("No hay suficientes unidades disponibles.")
        else:
            nuevo_codigo_venta = obtener_ultimo_codigo_venta() + 5
            valor_venta = cantidad * libro[1]
            nuevas_unidades = libro[0] - cantidad

            sentencia = """INSERT INTO Ventas (codigo_venta, id_cliente, id_libro, cantidad, valor_venta)
                            VALUES (?, ?, ?, ?, ?)"""
            cursor.execute(sentencia, (nuevo_codigo_venta, id_cliente, codigo_libro, cantidad, valor_venta))
            conexion.commit()

            sentencia = """UPDATE libros
                            SET unidades = ?
                            WHERE id_libros = ?"""
            cursor.execute(sentencia, (nuevas_unidades, codigo_libro))
            conexion.commit()

            desconectar_db(conexion, cursor)
            print("Venta registrada exitosamente.")
            print(f"Código de venta: V-{nuevo_codigo_venta}")

def mostrar_ventas():
    print("==== Lista de ventas realizadas ====")
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT *
                    FROM Ventas"""
    cursor.execute(sentencia)
    ventas = cursor.fetchall()
    tabla_ventas = PrettyTable(("Código de venta", "Código de cliente", "Código de libro", "Cantidad", "Valor de venta"))
    for venta in ventas:
        tabla_ventas.add_row(venta)
    print(tabla_ventas)
    desconectar_db(conexion, cursor)
    print("======================================")

def buscar_venta_menu():
    while True:
        print("Para salir, ingrese '0'")
        codigo_venta = int(input("Ingrese el código de la venta a buscar: "))
        
        if codigo_venta == 0:
            break
        
        conexion, cursor = conectar_db("librerias.db")
        sentencia = """SELECT *
                        FROM Ventas
                        WHERE codigo_venta = ?"""
        cursor.execute(sentencia, (codigo_venta,))
        venta = cursor.fetchone()

        if venta is not None:
            print("================================")
            print(f"Código de venta: V-{venta[0]}, Código de cliente: {venta[1]}, Código de libro: {venta[2]}, Cantidad vendida: {venta[3]}, Valor de venta: {venta[4]}")
            print("=================================")
        else:
            print("======================================")
            print("La venta no fue encontrada.")

        desconectar_db(conexion, cursor)

def eliminar_venta():
    codigo_venta = int(input("Ingrese el código de venta que desea eliminar: "))
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT *
                    FROM Ventas
                    WHERE codigo_venta = ?"""
    cursor.execute(sentencia, (codigo_venta,))
    venta = cursor.fetchone()

    if venta is not None:
        sentencia = """DELETE FROM Ventas
                        WHERE codigo_venta = ?"""
        cursor.execute(sentencia, (codigo_venta,))
        conexion.commit()
        print("La venta se eliminó correctamente.")
        
        sentencia = """SELECT unidades
                        FROM libros
                        WHERE id_libros = ?"""
        cursor.execute(sentencia, (venta[2],))
        unidades_libro = cursor.fetchone()[0]

        nuevas_unidades = unidades_libro + venta[3]
        sentencia = """UPDATE libros
                        SET unidades = ?
                        WHERE id_libros = ?"""
        cursor.execute(sentencia, (nuevas_unidades, venta[2]))
        conexion.commit()
    else:
        print("No se encontró ninguna venta con ese código.")

    desconectar_db(conexion, cursor)

def actualizar_venta():
    print("=====================================")
    codigo_venta = int(input("Ingrese el código de la venta (0 para salir): "))
    while codigo_venta != 0:
        conexion, cursor = conectar_db("librerias.db")
        sentencia = """SELECT *
                        FROM Ventas
                        WHERE codigo_venta = ?"""
        cursor.execute(sentencia, (codigo_venta,))
        venta = cursor.fetchone()

        if venta is not None:
            cantidad_anterior = venta[3]
            unidades_anteriores = obtener_unidades_libro(venta[2])
            precio_libro = obtener_precio_libro(venta[2])

            nuevas_unidades = int(input("Ingrese la nueva cantidad vendida: "))
            print("=====================================")
            valor_venta = precio_libro * nuevas_unidades

            sentencia = """UPDATE Ventas
                            SET cantidad = ?, valor_venta = ?
                            WHERE codigo_venta = ?"""
            cursor.execute(sentencia, (nuevas_unidades, valor_venta, codigo_venta))
            conexion.commit()

            utilizar_unidades_libro(venta[2], unidades_anteriores + cantidad_anterior - nuevas_unidades)
            print("=====================================")
            print("Venta actualizada correctamente.")
            print("=====================================")
        else:
            print("El código de venta no se encuentra en la lista.")

        desconectar_db(conexion, cursor)

        codigo_venta = int(input("Ingrese el código de la venta (0 para salir): "))

def obtener_unidades_libro(codigo_libro):
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT unidades
                    FROM libros
                    WHERE id_libros = ?"""
    cursor.execute(sentencia, (codigo_libro,))
    unidades_libro = cursor.fetchone()
    desconectar_db(conexion, cursor)
    if unidades_libro is not None:
        return unidades_libro[0]
    return 0

def obtener_precio_libro(codigo_libro):
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT precio
                    FROM libros
                    WHERE id_libros = ?"""
    cursor.execute(sentencia, (codigo_libro,))
    precio_libro = cursor.fetchone()
    desconectar_db(conexion, cursor)
    if precio_libro is not None:
        return precio_libro[0]
    return 0

def obtener_ultimo_codigo_venta():
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT MAX(codigo_venta)
                    FROM Ventas"""
    cursor.execute(sentencia)
    ultimo_codigo_venta = cursor.fetchone()[0]
    desconectar_db(conexion, cursor)
    if ultimo_codigo_venta is not None:
        return ultimo_codigo_venta
    return 0

def utilizar_unidades_libro(codigo_libro, nuevas_unidades):
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """UPDATE libros
                    SET unidades = ?
                    WHERE id_libros = ?"""
    cursor.execute(sentencia, (nuevas_unidades, codigo_libro))
    conexion.commit()
    desconectar_db(conexion, cursor)

def menu_estadisticas():
    while True:
        print("==== Menu estadísticas ====")
        print("1 - Ventas totales de libros por ISBN")
        print("2 - Libro más y menos vendido")
        print("3 - Venta total de la librería")
        print("4 - Cliente con mayor compra por venta")
        print("5 - Cliente con mayor volumen de compra total")
        print("6 - Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            obtener_ventas_totales_por_codigo_libro()
        elif opcion == '2':
            mostrar_libros_mas_y_menos_vendido()
        elif opcion == '3':
            calcular_venta_total_libreria()
        elif opcion == '4':
            cliente_mayor_compra()
        elif opcion == '5':
            volumen_compra()
        elif opcion == '6':
            break
        else:
            print("Opción inválida")

def obtener_ventas_totales_por_codigo_libro():
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT id_libro, SUM(cantidad) AS ventas_totales
                    FROM Ventas
                    GROUP BY id_libro"""
    cursor.execute(sentencia)
    ventas_totales_por_libro = cursor.fetchall()
    

    print("Ventas por libro:")
    for venta in ventas_totales_por_libro:
        codigo_libro = venta[0]
        ventas_totales = venta[1]
        print("Libro con código", codigo_libro, "- Ventas totales:", ventas_totales)
        desconectar_db(conexion, cursor)

def mostrar_libros_mas_y_menos_vendido():
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT id_libro, SUM(cantidad) AS unidades_vendidas
                    FROM Ventas
                    GROUP BY id_libro
                    ORDER BY unidades_vendidas DESC"""
    cursor.execute(sentencia)
    libros_vendidos = cursor.fetchall()
    desconectar_db(conexion, cursor)

    if libros_vendidos:
        libro_mas_vendido = libros_vendidos[0]
        libro_menos_vendido = libros_vendidos[-1]

        print("==============================================")
        print("Libro más vendido:")
        print("Código:", libro_mas_vendido[0])
        print("Unidades vendidas:", libro_mas_vendido[1])
        print("==============================================")
        print("Libro menos vendido:")
        print("Código:", libro_menos_vendido[0])
        print("Unidades vendidas:", libro_menos_vendido[1])
        print("==============================================")
    else:
        print("No hay registros de ventas.")

def calcular_venta_total_libreria():
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT SUM(valor_venta) AS venta_total
                    FROM Ventas"""
    cursor.execute(sentencia)
    venta_total_libreria = cursor.fetchone()[0]
    desconectar_db(conexion, cursor)

    print("====================================================")
    print("Venta Total de la librería:", venta_total_libreria)
    print("====================================================")

def cliente_mayor_compra():
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT Clientes.nombre, SUM(Ventas.valor_venta) AS total_compra
                    FROM Ventas
                    JOIN Clientes ON Ventas.id_cliente = Clientes.id_cliente
                    GROUP BY Ventas.id_cliente
                    ORDER BY total_compra DESC
                    LIMIT 1"""
    cursor.execute(sentencia)
    cliente_mayor_compra = cursor.fetchone()
    desconectar_db(conexion, cursor)

    if cliente_mayor_compra is not None:
        nombre_cliente = cliente_mayor_compra[0]
        total_compra = cliente_mayor_compra[1]

        print("====================================================")
        print("El cliente con la mayor compra por venta fue:", nombre_cliente)
        print("Total de compra:", total_compra)
        print("====================================================")
    else:
        print("No se encontró ningún cliente en la base de datos.")

def volumen_compra():
    conexion, cursor = conectar_db("librerias.db")
    sentencia = """SELECT Clientes.nombre, SUM(Ventas.valor_venta) AS volumen_compra
                    FROM Ventas
                    JOIN Clientes ON Ventas.id_cliente = Clientes.id_cliente
                    GROUP BY Ventas.id_cliente
                    ORDER BY volumen_compra DESC
                    LIMIT 1"""
    cursor.execute(sentencia)
    cliente_mayor_volumen_compra = cursor.fetchone()
    desconectar_db(conexion, cursor)

    if cliente_mayor_volumen_compra is not None:
        nombre_cliente = cliente_mayor_volumen_compra[0]
        volumen_compra = cliente_mayor_volumen_compra[1]

        print("===================================================================")
        print("El cliente con el mayor volumen de compra total es:", nombre_cliente)
        print("Volumen de compra:", volumen_compra)
        print("===================================================================")
    else:
        print("No se encontró ningún cliente en la base de datos.")

while True:
        print("====Menu principal====")
        print("1 - clientes")
        print("2 - libros")
        print("3 - ventas")
        print("4 - estadisticas")
        print("5 - salir")
        opcion=input("ingrese una opcipn: ")
        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_libros()
        elif opcion == '3':
            menu_ventas()
        elif opcion == '4':
            menu_estadisticas()
        elif opcion=='5':
            print("fin del programa")
            break
        else:
            print("opcion invalida, intente nuevamente")
