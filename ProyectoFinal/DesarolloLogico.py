import csv
import tkinter as tk

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
        balance_actualizado = balance()

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
    return suma


class IngresoCatalogado(Ingreso):
    def __init__(self, monto, dia, mes, año, divisa, categoria, ):
        super().__init__(monto, dia, mes, año, divisa)
        self.categoria = categoria

    def guardar_ingreso(self, divisa):
        monto_convertido = self.convertir_divisa(divisa)
        with open('balance.csv', 'a') as file:
            file.write(f'{monto_convertido},{self.dia},{self.mes},{self.año},{self.categoria}\n')

    
class EgresoCatalogado(Egreso):
    def __init__(self, monto, dia, mes, año, divisa, categoria):
        super().__init__(monto, dia, mes, año, divisa)
        self.categoria = categoria

    def guardar(self, divisa):
        monto_convertido = int(self.convertir_divisa(divisa))
        print(monto_convertido)
        with open('balance.csv', 'a') as file:
            file.write(f'{monto_convertido*-1},{self.dia},{self.mes},{self.año},{self.categoria}\n')

    @staticmethod
    def obtener_egresos_por_categoria(categoria):
        with open('balance.csv', 'r') as file:
            egresos = []
            for line in file:
                linea = line.split(',')
                monto = int(linea[0])
                dia = int(linea[1])
                mes = int(linea[2])
                año = int(linea[3])
                cat = linea[4].strip()
                if cat == categoria:
                    egreso = EgresoCatalogado(monto, dia, mes, año, '', cat)
                    egresos.append(egreso)
            return egresos

def monto():
    with open('balance.csv', 'r') as file:
        list = []
        for line in file:
            linea = line.split(',')
            list.append(linea[0])
        return list


def dia():
    with open('balance.csv', 'r') as file:
        list = []
        for line in file:
            linea = line.split(',')
            list.append(linea[1])
        return list


def mes():
    with open('balance.csv', 'r') as file:
        list = []
        for line in file:
            linea = line.split(',')
            list.append(linea[2])
        return list


def año():
    with open('balance.csv', 'r') as file:
        list = []
        for line in file:
            linea = line.split(',')
            list.append(linea[3].replace("\n", ""))
        return list


def filtrar(filtro, tipo_filtro):
    listMonto = monto()
    listDia = dia()
    listMes = mes()
    listAño = año()
    if tipo_filtro == 1:
        for i in range(len(listDia)):
            if str(filtro) == listDia[i]:
                print(listMonto[i], listDia[i], listMes[i],listAño[i])
    elif tipo_filtro == 2:
        for i in range(len(listMes)):
            if str(filtro) == listMes[i]:
                print(listMonto[i], listDia[i], listMes[i],listAño[i])
    elif tipo_filtro == 3:
        for i in range(len(listAño)):
            if str(filtro) == listAño[i]:
                print(listMonto[i], listDia[i], listMes[i],listAño[i])

filtrar(4, 2)