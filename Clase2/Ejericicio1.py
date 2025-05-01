import datetime  # Importamos un módulo para trabajar con fechas y horas

# Creamos una lista vacía donde se van a guardar los productos del inventario
inventario = []


# Esta función permite agregar un producto al inventario
def agregar_producto():
    # Pedimos al usuario el nombre del producto
    nombre = input("Introduce el nombre del producto: ").strip()

    try:
        # Pedimos la cantidad y el precio del producto, y los convertimos a número decimal (float)
        cantidad = float(input("Introduce la cantidad del producto: "))
        precio = float(input("Introduce el precio del producto: "))

        # Validamos que ambos sean mayores a cero
        if cantidad <= 0 or precio <= 0:
            print("Cantidad y precio deben ser positivos.")
            return  # Salimos de la función si no es válido

    except ValueError:
        # Si el usuario no escribe un número válido, se muestra este mensaje
        print("La cantidad y el precio deben ser números válidos.")
        return  # Salimos de la función

    # Creamos un diccionario con los datos del producto
    producto = {
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio,
        'fecha_registro': datetime.datetime.now()  # Guardamos la fecha y hora actual
    }

    # Agregamos el producto a la lista del inventario
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado correctamente.\n")


# Esta función muestra todos los productos del inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.\n")
        return  # Salimos si la lista está vacía

    # Recorremos cada producto en el inventario y lo mostramos
    for idx, producto in enumerate(inventario, start=1):
        print(f"{idx}. {producto['nombre']} - Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f}€")
        print()


# Esta función calcula el valor total del inventario
def calcular_valor_total():
    if not inventario:
        print("El inventario está vacío.\n")
        return

    # Sumamos (cantidad * precio) de cada producto
    total = sum(p['cantidad'] * p['precio'] for p in inventario)
    print(f"El valor total del inventario es: {total:.2f}€\n")


# Esta función solo muestra el menú de opciones
def mostrar_menu():
    print("1. Añadir producto")
    print("2. Mostrar Inventario")
    print("3. Calcular valor total")
    print("4. Salir")


# Esta es la función principal que ejecuta todo el programa
def main():
    terminado = True  # Esta variable controla si seguimos ejecutando el programa

    while terminado:
        mostrar_menu()  # Mostramos el menú
        opcion = input("Elige una opción: ")

        # Dependiendo de lo que elija el usuario, llamamos a una función
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            calcular_valor_total()
        elif opcion == '4':
            print("Saliendo del programa...")
            terminado = False  # Cambiamos la variable para salir del bucle
        else:
            print("Opción no válida. Intenta de nuevo.")


# Esta línea se asegura de que el programa comience desde aquí
if __name__ == "__main__":
    main()
