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

def agregarInventario():

    nombreProducto = input("Nombre producto: ")
    cantidadProducto = input("Cantidad: ")
    costo = input("Precio: $")
    try:
        cursor.execute("INSERT INTO inventario (`nombreProducto`, `cantidadProducto`, `costo`) VALUES (%s, %s, %s)", (nombreProducto, cantidadProducto, costo))
        conexion.commit()
    # INSERT INTO `test`.`inventario` (`nombreProducto`, `cantidadProducto`, `costo`) VALUES ('pan', '111', '222');
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()
    conexion.close()

agregarInventario()

