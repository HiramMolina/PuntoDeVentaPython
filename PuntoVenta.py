import mysql.connector

# def conexion():
#     try:
#         db = mysql.connector.connect(host="localhost",
#                             user="root",
#                             passwd="admin",
#                             db="test"
#                             )
#         print("Conexión hecha")
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")

# tabla = input("Ingrese la tabla: ")
# cursor.execute("SELECT * FROM " + tabla) #Ejecutar Query

# cursor.execute("SELECT * FROM empleado")
# for fila in cursor:
#     print(fila)
# cursor.close()
# conexion.close()

conexion = mysql.connector.connect(host="localhost",
                            user="root",
                            passwd="admin",
                            db="test"
                            )

cursor = conexion.cursor()

def mostrarInventario():

    print("\n")
    print("Inventario de la tiendita:\n")
    cursor.execute("SELECT * FROM inventario")
    for fila in cursor:
        print(fila)
    cursor.close()
    conexion.close()

def mostrarInventarioo():
    
    print("\n")
    print("Inventario de la tiendita:\n")
    cursor.fetchall("SELECT * FROM inventario")
    for fila in cursor:
        print(fila)
    cursor.close()
    conexion.close()

mostrarInventarioo()

