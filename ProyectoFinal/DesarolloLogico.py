import csv

class Perfil:
    def __init__(self, jubilado=False, estudiante=False, trabajador=True):
        self.jubilado = jubilado
        self.estudiante = estudiante
        self.trabajador = trabajador

class Movimiento :

    def __init__(self, monto, dia, mes, año, divisa,):
        self.monto = monto
        self.dia = dia
        self.mes = mes
        self.año = año
        self.divisa = divisa


    def convertir_divisa(self, divisa):
        if self.divisa == 'USD' and divisa == 'COP':
            return self.monto * 4500
        elif self.divisa == 'COP' and divisa == 'USD':
            return self.monto / 4500
        else:
            return self.monto

    def guardar(self, divisa):
        monto_convertido = self.convertir_divisa(divisa)
        with open('balance.csv', 'a') as file:
            file.write(f'{monto_convertido},{self.dia},{self.mes},{self.año}\n')
        balance()

class Ingreso(Movimiento):
    def ingresos(self, divisa):
        self.guardar(divisa)

class Egreso(Movimiento):
    def egresos(self, divisa):
        self.monto *= -1
        self.guardar(divisa)

def balance():
    with open('balance.csv', 'r') as file:
        suma = 0
        for line in file:
            linea = line.split(',')
            monto = int(linea[0])
            suma += monto
        print(suma)
