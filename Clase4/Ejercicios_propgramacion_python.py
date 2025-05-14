from xmlrpc.client import boolean


def ejercicio1():
    ciudad = input("Introduce tu ciudad de residencia: ")
    habitantes =input(f"Introduce el numero aprox. de habitantes en tu {ciudad}: ")

    try:
        num_habitantes = int(habitantes)
        print(f"La ciudad de {ciudad} tiene aproximadamente {num_habitantes} habitantes.")
        habitantes_miles = num_habitantes / 1000
        print(f"Esto equivale a {habitantes_miles} mil habitantes.")
    except ValueError:
        print("Error: No introdujo un numero correcto de habitantes.")
    finally:
        print("Fin del bloque try/excep...")

def ejercicio2():
    try:
        capital = float(input("Capital inicial (€):"))
        tasa = float(input("Tasa de interes anual (%):"))
        anos = int(input("Numero de años:"))

        if capital <0 or tasa<0 or anos<0:
            print("Error: Ninguno de los valores puede ser negativo")
            exit() #Terminar el programa

        else:
            interes = capital * (tasa / 100) * anos
            monto_total = capital + interes
            print(f"Interes generado: {interes}")
            print(f"Monto total: {monto_total}")

    except ValueError:
        print("Tienes que introducir valores apropiados")

def ejercicio3():
    try:
        edad = int(input("¿Cual es tu edad?:"))
        if edad <0:
            print("Edad invalida. No puede ser negativo")
        elif edad < 12:
            print("Niñez")

        elif edad < 18:
            print("Adultez")

        elif edad < 65:
            print("Adultez")

        else:
            print("Tercera edad")

    except ValueError:
        print("Tienes que introducir un numero entero")

def ejercicio5():
    contrasena_defecto = "python123"
    contador = 1  # Primera vez que se pide la contraseña
    contrasenia = input("Ingrese la contraseña: ")

    while contrasenia != contrasena_defecto:
        contrasenia = input("Contraseña incorrecta. Inténtelo de nuevo: ")
        contador += 1

    print("Acceso concedido!!!")
    print(f"Número de intentos: {contador}")

conteo_conversiones = 0 # VARIABLE GLOBAL

def celsius_a_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def conventir_temperatura(celsius):
    global conteo_conversiones
    kelvin = celsius_a_kelvin(celsius)
    conteo_conversiones +=1
    return kelvin

def ejercicio6():
    temp_c = float(input("Temperatura en C:"))
    temp_k = conventir_temperatura(temp_c)
    print(f"{temp_c} en C son {temp_k} en K")
    print(f"Total de conversiones realizadas {conteo_conversiones}")






if __name__ == '__main__':
    ejercicio6()