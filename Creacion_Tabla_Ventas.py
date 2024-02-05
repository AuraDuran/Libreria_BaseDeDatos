from sqlLibreria import conectar_bd, desconectar_bd 

conexion,cursor=conectar_bd("LibrerA.db")

cursor.execute("""CREATE TABLE ventas(
                      id INTERGER PRIMARY KEY,
                      id_clientes INTERGER NOT NULL,
                      id_libros INTERGER NOT NULL,
                      cantidad INTERGER NOT NULL,
                      valor_Total REAL NOT NULL)""")

desconectar_bd(conexion,cursor)