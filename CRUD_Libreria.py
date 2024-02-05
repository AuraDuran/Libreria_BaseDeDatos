from sqlLibreria import conectar_bd, desconectar_bd
from modulo_clientes import*
from modulo_libros import*
from modulo_venta import*
from modulo_estadisticas import*


clientes = [ ]
libros = [ ]
ventas = [()]

def menu_principal():
    while True:
        print(" ")
        print("---Menu Principal---")
        print("1. Clientes")
        print("2. Libros")
        print("3. Ventas")
        print("4. Estadisticas")
        print("5. Salir")
        print()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            menu_clientes()
        elif opcion == 2:
            menu_libros()
        elif opcion == 3:
            menu_ventas()
        elif opcion == 4:
            menu_estadisticas()
        elif opcion == 5:
            print("Ha salido exitosamente.")
            break
        else:
            print("Ingrese una opción válida.")

#__________________________________________________
def menu_clientes():
    while True:
        print(" ")
        print("---Clientes---")
        print("1. Ingresar Clientes")
        print("2. Lista de Clientes")
        print("3. Actualizar Cliente")
        print("4. Buscar Cliente")
        print("5. Eliminar Cliente")
        print("6. Volver a Menu Principal")
        print()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            ingresar_cliente()
        elif opcion == 2:
            lista_clientes()
        elif opcion == 3:
            actualizar_cliente()
        elif opcion == 4:
            buscar_cliente()
        elif opcion == 5:
            eliminar_cliente()
        elif opcion == 6:
            break
        else:
            print("Ingrese una opción válida.")

#__________________________________________________

def menu_libros():
    while True:
        print(" ")
        print("---Libros---")
        print("1. Ingresar Libro")
        print("2. Lista de Libros")
        print("3. Actualizar Libro")
        print("4. Buscar Libro")
        print("5. Eliminar Libro")
        print("6. Volver a Menu Principal")
        print()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            ingresar_libro()
        elif opcion == 2:
            lista_libros()
        elif opcion == 3:
            actualizar_libro()
        elif opcion == 4:
            buscar_libro()
        elif opcion == 5:
            eliminar_libro()
        elif opcion == 6:
            break
        else:
            print("Ingrese una opción válida.")

#__________________________________________________

def menu_ventas():
    while True:
        print(" ")
        print("---Ventas---")
        print("1. Realizar Venta")
        print("2. Lista de Ventas")
        print("3. Actualizar Venta")
        print("4. Buscar Venta")
        print("5. Eliminar Venta")
        print("6. Volver a Menu Principal")
        print()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            realizar_venta()
        elif opcion == 2:
            lista_ventas()
        elif opcion == 3:
            actualizar_venta()
        elif opcion == 4:
            buscar_venta()
        elif opcion == 5:
            eliminar_venta()
        elif opcion == 6:
            break
        else:
            print("Ingrese una opción válida.")

#__________________________________________________

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

#__________________________________________________

def mostrar_menu_principal():
    while True:
        print(" ")
        print("----- Menu Principal -----")
        print("1. Clientes")
        print("2. Libros")
        print("3. Ventas")
        print("4. Estadísticas")
        print("5. Salir")
        print()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_libros()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            menu_estadisticas()
        elif opcion == "5":
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")


mostrar_menu_principal()


