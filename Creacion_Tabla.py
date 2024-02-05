import sqlite3

try:
    conexion=sqlite3.Connection("LibrerA.db")
    cursor=conexion.cursor()
    cursor.execute("""CREATE TABLE clientes(
                      id INTERGER PRIMARY KEY,
                      nombre TEXT NOT NULL)""")
                       
    conexion.commit()
    
    cursor.close()
    conexion.close()


except sqlite3.OperationalError as error:
    print('Error al abrir la base de datos:', error)