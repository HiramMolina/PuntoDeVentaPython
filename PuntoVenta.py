import mysql.connector
from tabulate import tabulate 

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

    print("\n" + "=" * 40)
    print("             INVENTARIO")
    print("=" * 40 + "\n")

    cursor.execute("SELECT * FROM inventario")
    filas = cursor.fetchall()

    tabla = [[fila[0],fila[1],fila[2],fila[3]] for fila in filas]
    print(tabulate(tabla, headers=["ID Producto", "Nombre del Producto", "Cantidad Producto", "Costo"], tablefmt="heavy_outline"))

    cursor.close()
    conexion.close()

mostrarInventario()

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

def eliminarInventario():
    print("\n" + "=" * 40)
    print("    ELIMINAR PRODUCTO DEL INVENTARIO")
    print("=" * 40 + "\n")

    # Consulta los datos de inventario
    cursor.execute("SELECT `idProducto`, `nombreProducto` FROM inventario")
    filas = cursor.fetchall()  # Obtener todos los registros
    # Mostrar los datos en formato tabular
    tabla = [ [fila[0], fila[1] ] for fila in filas]
    print(tabulate(tabla, headers=["ID Producto", "Nombre del Producto"], tablefmt="heavy_outline"))
    cursor.close()
    conexion.close()

# eliminarInventario()
