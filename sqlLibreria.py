import sqlite3

def conectar_bd(nombre_bd):
    try:
        conexion=sqlite3.Connection(nombre_bd)
        cursor=conexion.cursor()
        return conexion, cursor
    
    except sqlite3.Error as error:
        print('Error al abrir la base de datos: ', error)
        return None, None

def desconectar_bd(conexion,cursor):
    if conexion:
        cursor.close()
        conexion.close()
        print("conexion cerrada correctamente")