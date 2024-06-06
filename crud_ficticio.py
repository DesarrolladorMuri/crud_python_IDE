# lista de productos
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 15, "stock": 20},
    {"id": 2, "nombre": "Pantalon", "precio": 20, "stock": 30},
    {"id": 3, "nombre": "Zapato", "precio": 50, "stock": 50},
]

# Fución para mostrar opciones
def mostrar_menu():
    print("¡Bievenidos a el sistema de gestion de inventario")
    print("Selecciona una opción:")
    print("1. Agregar un producto")
    print("2. Buscar un producto")
    print("3. Actualizar un Stock")
    print("4. Eliminar un producto")
    print("5. Ver todos los productos")
    print("6. Salir")

# Función para mostrar productos
def ver_productos():
    if not productos:
        print("No hay productos registrados")
    else:
        print("Lista de productos:")
        for producto in productos:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Stock: {producto['stock']}")

# Función para buscar productos
def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar:")
    producto_encontrado = next((p for p in productos if p["nombre"].lower() == nombre.lower()), None)
    if producto_encontrado:
        print(f"Nombre: {producto_encontrado['nombre']}, Precio: ${producto_encontrado['precio']}, Stock: {producto_encontrado['stock']}")
    else:
        print("No se encontró el producto")

# Función Agregar producto
def agregar_producto():
    id_nuevo = max([p["id"] for p in productos], default=0) + 1
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad de productos en stock: "))
    nuevo_producto = {"id": id_nuevo, "nombre": nombre, "precio": precio, "stock": stock}
    productos.append(nuevo_producto)
    print("Nuevo producto agregado exitosamente")

# Función Actualizar producto
def actualizar_Stock():
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    producto_encontrado = next((p for p in productos if p["id"] == id_producto), None)
    if producto_encontrado:
        nuevo_nombre = input(f"Ingrese el nuevo nombre (actual: {producto_encontrado['nombre']}): ") or producto_encontrado["nombre"]
        nuevo_precio = float(input(f"Ingrese el nuevo precio (actual: ${producto_encontrado['precio']}): ")) or producto_encontrado["precio"]
        nuevo_stock = int(input(f"Ingresa la nueva cantidad de stock (actual: {producto_encontrado['stock']}): ")) or producto_encontrado["stock"]
        producto_encontrado["nombre"] = nuevo_nombre
        producto_encontrado["precio"] = nuevo_precio
        producto_encontrado["stock"] = nuevo_stock
        print("Producto actualizado exitosamente.")
    else:
        print("No se encontro el producto.")

# función Eliminar un producto
def eliminar_producto():
    
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    producto_encontrado = next((p for p in productos if p["id"] == id_producto), None)
    if producto_encontrado:
        productos.remove(producto_encontrado)
        print("Producto eliminado exitosamente.")
    else:
        print("No se encontró el producto.")

#Ciclo del programa
while True:
    mostrar_menu()
    opcion = int(input("Ingresa el número de la opción: "))
    
    if opcion == 1:
        agregar_producto()
        ver_productos()
    elif opcion == 2:
        buscar_producto()
    elif opcion == 3:
        actualizar_Stock()
        ver_productos()
    elif opcion == 4:
        eliminar_producto()
        ver_productos()
    elif opcion == 5:
        ver_productos()
    elif opcion == 6:
        print("¡Gracias por usar el sistema de gestion de productos!")
        break
    else:
        print("Opción inválida. Por favor, intentelo nuevamente.")
    
    otra_operacion = input("¿Desea realizar otra operación? (s/q): ")
    if otra_operacion.lower() != "s":
        mostrar_menu()