def ejercicio1():
    nombre = input("¿Cuál es tu nombre?")
    altura_cm = input("Introduce tu altura en centímetros:")

    print(f"Hola {nombre}, mides {altura_cm} cm")

    try:
        altura_cm_float = float(altura_cm)
        altura_m = altura_cm_float / 100
        print(f"Hola {nombre}, mides {altura_m} m")
    except ValueError:
        print("El valor ingresado para la altura no es un número válido")

def ejercicio2():
    num1 = input("Introduzca el primer numero: ")
    num2 = input("Introduzca el segundo numero: ")

    try:
        multiplicacion = int(num1) * int(num2) #aqui estoy haciendo el casteo para que sea numeros
        print(f"La multpilcacion entre {num1} * {num2} = {multiplicacion}")
        division = int(num1) / int(num2)
        print(f"La division entre {num1} / {num2} = {division}")
    except ValueError:
        print("ERROR: no ha introducido numeros enteros correctamente.")
    except ZeroDivisionError:
        print("ERROR: No se puede dividir por cero.")

#Condicionales (if, elif, else)
def ejercicio3():
    nota = float(input("Introduce una nota, escala 0-10 ==> "))

    try:
        if nota < 0 or nota > 10:
            print("La nota esta fuera de rango")
        elif nota < 5:
            print("Supendido")
        elif 5 <= nota <= 6:
            print("Aprobado")
        elif 7 >= nota or nota <= 8:
            print("Notable")
        else:
            print("Sobresaliente")
    except ValueError:
        print("No estas pasando un numero a la nota")

#Bucles For
def ejercicio4():
    numeros = [5,2,7,1,9]
    suma_total = 0

    for num in numeros:
        suma_total  += num

    print(f"La total de todos los numeros es: {suma_total}")

#Bucles While
def ejercicio5():
    numeros_ingresados = []
    try:
        numero = float(input("Introduzca un numero entero - numero negativo para salir: "))
        while numero >= 0 :
            numeros_ingresados.append(numero)
            numero = float(input("Introduzca un numero entero - numero negativo para salir: "))
    except ValueError:
        print("No se puede introducir algo que no sea numero")
    print(f"Numeros enteros ingresados: {numeros_ingresados}")

#cuando es una funcion se le pasa un valor por parametro, eso es lo que creo yo
def cuadrado(num):
    resultado_local = num * num #variable local
    return resultado_local

#varaible global

mensaje_global = "valor Inicial"

def modificar_mensaje():
    global mensaje_global
    mensaje_global = "El mensaje a sido modificado desde la funcion"

def ejercicio6():
    numero = 4
    print(f"El cuadrado de {numero} es: {cuadrado(numero)}")
    print(f"Antes de modificar: {mensaje_global}")
    modificar_mensaje()
    print(f"Despues de modificar: {mensaje_global}")

def ejercicio7():
    multiplicar_por_diez = lambda x : x*10
    numeros = [1,2,3,4,5]

    nuevos_numeros = list(map(multiplicar_por_diez, numeros))

def ejercicio9():
    numero = input("Introduce un numero entero: ")
    try:
        resultado = 10 / int(numero)
        print(f"La division entre 10/{numero}:{resultado}")
    except ValueError:
        print("ERROR: Lo que introdujo no es un numero")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.....")
    finally:
        print("Fin del bloque try/except")

if __name__ == '__main__':
    ejercicio9()
