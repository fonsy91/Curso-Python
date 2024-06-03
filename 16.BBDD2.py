import sqlite3

miConexion = sqlite3.connect("BBDDGestionProductos")
miCursor = miConexion.cursor()

# Creamos el campo clave y la tabla productos solo se ejecuta la primera vez

#miCursor.execute('''
#    CREATE TABLE PRODUCTOS (
#        ID INTEGER PRIMARY KEY AUTOINCREMENT,
#        NOMBRE_ARTICULO VARCHAR(40) UNIQUE,
#        PRECIO INTEGER,
#        SECCION VARCHAR(40)
#    )
#''')

'''
productos = [
    ("pelota",20,"juguetería"),
    ("pantalón",15,"confección"),
    ("destornillador",25,"ferretería"),
    ("jarrón",45,"cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
'''

# OPERACIONES CRUD
# Consulta (get)
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confección'")
consulta = miCursor.fetchall() 
print(consulta)

# Update (actualizar)
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO = 'pelota'")
miCursor.execute("SELECT * FROM PRODUCTOS")
consulta2 = miCursor.fetchall() 
print(consulta2)

# Eliminar (Delete)
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")
miCursor.execute("SELECT * FROM PRODUCTOS")
consulta3 = miCursor.fetchall() 
print(consulta3)

miConexion.commit()
miConexion.close()