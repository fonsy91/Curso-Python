'''
    Python pude manipular y es compatible con SQL Server, Oracle,
    Mysql, SQLite, PostgresSQL..., bases de datos relacionales.

    Tambien con bases de datos orientadas a objetos es importante 
    saber usar el lenguaje de SQL

'''
import sqlite3

# Abrir-Cerrar conexion
miConexion = sqlite3.connect("BaseDatosPrueba")

# Crear puntero
miCursor = miConexion.cursor()

# Ejecutar query SQL
# Creamos una tabla PRODUCTOS 
# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',20,'DEPORTES')")
miCursor.execute("SELECT * FROM PRODUCTOS")
leerProductos = miCursor.fetchall()
print(leerProductos)

miConexion.commit()

'''
Tambien se pueden registrar de un solo golpe varios registros

variosProductos = [
    ("Camiseta",10,"Deportes"),
    ("Jarron",90,"Cerámica"),
    ("Camión",20,"Juguetería")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
'''

# Manejar los resultados de la query

# Cerrar puntero

# Cerrar conexion
miConexion.close()

#VAMOS POR EL VIDEO: https://www.youtube.com/watch?v=eM0MkDc34qo&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=56