#en este ejercicio estamos practicando POO
class Empleado: #esta es la clase
    #esto es el constructor
    def __init__(self, id_empleado, nombre, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.salario = salario

    #declarando el metodo que me pide el enunciado
    def calcular_bonificacion(self):
        return self.salario * 0.1

    #declarando el metodo mostrar informacion
    def mostrar_informacion(self):
        info = f"Empleado {self.id_empleado}: nombre: {self.nombre}, salario: {self.salario}"
        return info

#Creando la clase Gerente que extiende de Empleado
class Gerente(Empleado):
    #defino el constructor
    def __init__(self, id_empleado, nombre, salario, departamento):
        super().__init__(id_empleado,nombre,salario) #asi se define la herencia de los atributps
        self.departamento = departamento

    #declarando el metodo que me pide el enunciado
    def aprobar_proyectos(self):
        print(f"Gerente{self.nombre} del departamento{self.departamento} aprueba el proyecto")

    #usando el metodo heredado de Empleado
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f"Departamento: {self.departamento}"
        return info

#Creando la clase Departamento
class Departamento:
    #defino el constructor
    def __init__(self, id_departamento, nombre):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.empleados = [] #se crea esta lista vacia para ir añadiendo futuros empleados

    #creando los metodos
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado al departamento {self.nombre}")

    def remover_empleado(self, empleado):
        if empleado in self.empleados:
           self.empleados.remove(empleado)
           print(f"Empleado {empleado.nombre} se eliminado del departamento {self.nombre}")

    def listar_empleados(self):
        print(f"Empleados del departamento {self.nombre}")
        for empl in self.empleados:
            print(empl.mostrar_informacion())

def main():
    empleado1 = Empleado(1,"Juan perez",3000)
    gerente1 = Gerente(2,"Maria Gomez",5000,"Ventas")
    depto1 = Departamento(1,"Ventas")
    depto1.agregar_empleado(empleado1)
    depto1.agregar_empleado(gerente1)

    print(empleado1.mostrar_informacion())
    print(gerente1.mostrar_informacion())

if __name__ == "__main__":
    main()

    #me quede por el minuto 41:48



