# Importamos datetime para verificar que las fechas estén en un formato correcto (AAAA-MM-DD)
from datetime import datetime

# Creamos una lista vacía que se llama "tareas". Aquí se guardarán todas las tareas.
# Una lista es como una caja donde puedes meter muchos objetos (en este caso, diccionarios con tareas).
tareas = []


# Esta función sirve para agregar una nueva tarea a la lista
def agregar_tarea():
    print("\n-- Agregar nueva tarea --")

    # Solicitamos datos al usuario y los guardamos en variables
    titulo = input("Introduce el título de la tarea: ")
    descripcion = input("Introduce la descripción de la tarea: ")
    fecha_limite = input("Introduce la fecha límite (YYYY-MM-DD): ")
    prioridad = input("Selecciona la prioridad: 1-Alta, 2-Media, 3-Baja: ")

    try:
        # Convertimos el texto ingresado a un formato de fecha. Si no se puede, da error.
        datetime.strptime(fecha_limite, "%Y-%m-%d")

        # Convertimos prioridad a número entero (para poder usarlo como número después)
        prioridad = int(prioridad)

        # Validamos que esté entre 1 y 3
        if prioridad < 1 or prioridad > 3:
            print("La prioridad seleccionada no existe.")
            return  # Salimos de la función sin agregar nada
    except ValueError:
        # Si ocurre un error al convertir la fecha o prioridad, mostramos un mensaje y salimos
        print("Error: formato de fecha o prioridad inválido. Intente de nuevo.")
        return

    # Creamos un diccionario con los datos de la tarea. Un diccionario es como una ficha con etiquetas (clave: valor).
    tarea = {
        'titulo': titulo,
        'descripcion': descripcion,
        'fecha_limite': fecha_limite,
        'prioridad': prioridad,
        'estado': 'pendiente'  # Todas las tareas empiezan como "pendientes"
    }

    # Agregamos la tarea a la lista usando append()
    # append() sirve para "meter" un elemento al final de una lista
    tareas.append(tarea)
    print("✅ Tarea agregada con éxito.\n")


# Función para mostrar todas las tareas guardadas
def mostrar_tareas():
    print("\n-- Lista de tareas --")
    if not tareas:
        # Si la lista está vacía, mostramos un mensaje
        print("No hay tareas registradas.\n")
        return  # Aquí usamos return para salir de la función. No es obligatorio, pero útil si ya no hay nada que hacer.

    # Recorremos la lista con enumerate() que da el índice y el valor de cada tarea
    for idx, tarea in enumerate(tareas, start=1):
        # Traducimos el número de prioridad a texto
        prioridad_txt = {1: 'Alta', 2: 'Media', 3: 'Baja'}[tarea['prioridad']]
        print(
            f"{idx}. {tarea['titulo']} | {tarea['descripcion']} | Prioridad: {prioridad_txt} | Estado: {tarea['estado']} | Fecha límite: {tarea['fecha_limite']}")
    print()


# Función para buscar tareas por palabra clave (en el título o descripción)
def buscar_tarea():
    print("\n-- Buscar tarea --")
    busqueda = input("Introduce una palabra clave: ").strip().lower()

    # Creamos una nueva lista con las tareas que contienen la palabra clave
    encontrados = [t for t in tareas if busqueda in t['titulo'].lower() or busqueda in t['descripcion'].lower()]

    if encontrados:
        print("\nTareas encontradas:")
        for t in encontrados:
            prioridad_txt = {1: 'Alta', 2: 'Media', 3: 'Baja'}[t['prioridad']]
            print(
                f"- {t['titulo']}: {t['descripcion']} | Prioridad: {prioridad_txt} | Estado: {t['estado']} | Fecha límite: {t['fecha_limite']}")
    else:
        print("No se encontró ninguna tarea.")
    print()


# Esta función permite cambiar el estado de una tarea (de "pendiente" a "completada", o al revés)
def actualizar_estado():
    print("\n-- Actualizar estado de tarea --")
    mostrar_tareas()  # Mostramos la lista para que el usuario elija cuál modificar

    if not tareas:
        return

    try:
        num = int(input("¿Qué número de tarea quieres cambiar?: "))
        if num < 1 or num > len(tareas):
            print("Número inválido.")
            return

        # Alternamos el estado de la tarea
        estado_actual = tareas[num - 1]['estado']
        nuevo_estado = 'completada' if estado_actual == 'pendiente' else 'pendiente'
        tareas[num - 1]['estado'] = nuevo_estado

        print(f"Estado actualizado a '{nuevo_estado}'.\n")
    except ValueError:
        print("Error: debes escribir un número.\n")


# Función para borrar una tarea de la lista
def borrar_tarea():
    print("\n-- Eliminar tarea --")
    mostrar_tareas()

    if not tareas:
        return

    try:
        num = int(input("¿Qué número de tarea quieres eliminar?: "))
        if num < 1 or num > len(tareas):
            print("Número inválido.")
            return
        tarea_eliminada = tareas.pop(num - 1)  # pop() elimina el elemento en la posición dada
        print(f"Tarea '{tarea_eliminada['titulo']}' eliminada con éxito.\n")
    except ValueError:
        print("Error: debes escribir un número.\n")


# Esta es la función principal que muestra el menú al usuario
def main():
    while True:
        print("===== MENÚ DE TAREAS =====")
        print("1. Agregar una tarea")
        print("2. Listar todas las tareas")
        print("3. Buscar una tarea")
        print("4. Actualizar el estado de una tarea")
        print("5. Eliminar una tarea")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        # Según lo que elija el usuario, llamamos a una función distinta
        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            mostrar_tareas()
        elif opcion == '3':
            buscar_tarea()
        elif opcion == '4':
            actualizar_estado()
        elif opcion == '5':
            borrar_tarea()
        elif opcion == '6':
            print("Gracias por usar el gestor de tareas. ¡Hasta luego!")
            break  # Salimos del ciclo y termina el programa
        else:
            print("❌ Opción no válida. Intente de nuevo.\n")


# Aquí empieza el programa. Llamamos al menú.
if __name__ == "__main__":
    main()
