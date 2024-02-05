from sqlLibreria import conectar_bd, desconectar_bd 

conexion,cursor=conectar_bd("LibrerA.db")

cursor.execute("""CREATE TABLE libros(
                      id INTERGER PRIMARY KEY,
                      nombre_Libro TEXT NOT NULL,
                      valor REAL NOT NULL,
                      cantidad INTERGER NOT NULL)""")

desconectar_bd(conexion,cursor)
