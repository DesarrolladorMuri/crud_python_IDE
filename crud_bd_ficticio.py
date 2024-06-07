# Importar la biblioteca de base de datos
import sqlite3

# Crear la conexión a la base de datos y la tabla de productos
conn = sqlite3.connect("productos.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS productos (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              nombre TEXT,
              precio REAL,
              stock INTEGER
           )""")

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("¡Bienvenido al sistema de gestión de productos!")
    print("Selecciona una opción:")
    print("1. Ver todos los productos")
    print("2. Buscar un producto")
    print("3. Agregar un producto")
    print("4. Actualizar un producto")
    print("5. Eliminar un producto")
    print("6. Salir")

# Función para mostrar todos los productos
def ver_productos():
    c.execute("SELECT * FROM productos")
    productos = c.fetchall()
    if not productos:
        print("No hay productos registrados.")
    else:
        print("Lista de productos:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]}, Stock: {producto[3]}")

# Función para buscar un producto
def buscar_producto():
    nombre = input("Ingresa el nombre del producto a buscar: ")
    c.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
    producto = c.fetchone()
    if producto:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]}, Stock: {producto[3]}")
    else:
        print("No se encontró el producto.")

# Función para agregar un producto
def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    stock = int(input("Ingresa la cantidad de stock: "))
    c.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", (nombre, precio, stock))
    conn.commit()
    print("Producto agregado exitosamente.")

# Función para actualizar un producto
def actualizar_producto():
    id_producto = int(input("Ingresa el ID del producto a actualizar: "))
    c.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = c.fetchone()
    if producto:
        nuevo_nombre = input(f"Ingresa el nuevo nombre (actual: {producto[1]}): ") or producto[1]
        nuevo_precio = float(input(f"Ingresa el nuevo precio (actual: ${producto[2]}): ")) or producto[2]
        nuevo_stock = int(input(f"Ingresa la nueva cantidad de stock (actual: {producto[3]}): ")) or producto[3]
        c.execute("UPDATE productos SET nombre = ?, precio = ?, stock = ? WHERE id = ?", (nuevo_nombre, nuevo_precio, nuevo_stock, id_producto))
        conn.commit()
        print("Producto actualizado exitosamente.")
    else:
        print("No se encontró el producto.")

# Función para eliminar un producto
def eliminar_producto():
    id_producto = int(input("Ingresa el ID del producto a eliminar: "))
    c.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = c.fetchone()
    if producto:
        c.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conn.commit()
        print("Producto eliminado exitosamente.")
    else:
        print("No se encontró el producto.")

# Ciclo principal del programa
while True:
    mostrar_menu()
    opcion = int(input("Ingresa el número de la opción: "))

    if opcion == 1:
        ver_productos()
    elif opcion == 2:
        buscar_producto()
    elif opcion == 3:
        agregar_producto()
    elif opcion == 4:
        actualizar_producto()
    elif opcion == 5:
        eliminar_producto()
    elif opcion == 6:
        print("¡Gracias por usar el sistema de gestión de productos!")
        break
    else:
        print("Opción inválida. Por favor, intenta de nuevo.")

    otra_operacion = input("¿Deseas realizar otra operación? (s/n): ")
    if otra_operacion.lower() != "s":
        print("¡Gracias por usar el sistema de gestión de productos!")
        break

# Cerrar la conexión a la base de datos
conn.close()