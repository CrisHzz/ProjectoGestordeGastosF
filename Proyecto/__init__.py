from dataclasses import dataclass

class Perfil:
    def __init__(self, jubilado=False, estudiante=False, trabajador=True):
        self.jubilado = jubilado
        self.estudiante = estudiante
        self.trabajador = trabajador

class Usuario:
    def __init__(self, nombre, edad, correo, perfil, divisa):
        self.nombre :str = nombre
        self.edad :int = edad
        self.correo :str = correo
        self.perfil :Perfil = perfil
        self.divisa :str = divisa

    @classmethod
    def registro_usuario(cls):
      nombre=str(input("Porfavor,Ingrese su nombre "))
      edad=int(input("Porfavor,ingrese su edad "))
      correo=str(input("Porfavor,ingrese su correo "))
      perfil_jubilado = input("¿Es usted jubilado? (S/N): ").upper() == "S"
      perfil_estudiante = input("¿Es usted estudiante? [S/N]: ").upper() == "S"
      perfil_trabajador = input("¿Es usted trabajador? [S/N]: ").upper() == "S"
      perfil = Perfil(jubilado=perfil_jubilado, estudiante=perfil_estudiante,trabajador=perfil_trabajador)
      divisa = input("Ingrese su divisa (Hasta el momento solo disponible COP): ")
      return cls(nombre, edad, correo, perfil, divisa)



@dataclass
class Ingreso:
    monto: int
    dia: str
    mes: str
    anio: str

def ingresar_ingreso(usuario):
    monto = int(input("Ingrese el monto del ingreso: "))
    dia = input("Ingrese el día del ingreso (formato DD): ")
    mes = input("Ingrese el mes del ingreso (formato MM): ")
    anio = input("Ingrese el año del ingreso (formato AAAA): ")
    ingreso = Ingreso(monto, dia, mes, anio)
    with open('balance.csv', 'a') as file:
        file.write(f'{ingreso.monto},{ingreso.dia},{ingreso.mes},{ingreso.anio}\n')
    balance()

@dataclass
class Egreso:
    monto: int
    dia: str
    mes: str
    anio: str

def ingresar_egreso(usuario):
    monto = int(input("Ingrese el monto del egreso: "))
    dia = input("Ingrese el día del egreso (formato DD): ")
    mes = input("Ingrese el mes del egreso (formato MM): ")
    anio = input("Ingrese el año del egreso (formato AAAA): ")
    egreso = Egreso(monto, dia, mes, anio)
    monto = egreso.monto * -1
    with open('balance.csv', 'a') as file:
        file.write(f'{monto},{egreso.dia},{egreso.mes},{egreso.anio}\n')
    balance()

def balance():
    with open('balance.csv', 'r') as file:
        suma = 0
        for line in file:
            linea = line.split(',')
            monto = int(linea[0])
            suma = monto + suma
        print(f"El balance actual es: {suma}")


def menu(usuario):
    while True:
        print("---- GESTOR DE GASTOS ----")
        print("1. Ingresar ingreso")
        print("2. Ingresar egreso")
        print("3. Ver balance")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")
        if opcion == "1":
            ingresar_ingreso(usuario)
        elif opcion == "2":
            ingresar_egreso(usuario)
        elif opcion == "3":
            balance()
        elif opcion == "4":
            break
        else:
            print("Opción inválida, intente de nuevo")

