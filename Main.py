import csv
from datetime import datetime
from Planta import Planta
from Contratado import Contratado
from Externo import Externo
from ManejadorE import ManejadorE
from ITesorero import ITesorero
from IGerente import IGerente
from Menu import Menu


def cargarArreglo(ce):

    with open("Planta.csv") as archivo:
        reader = csv.reader(archivo, delimiter=";")
        for row in reader:
            ce.agregarEmpleado(Planta(row[0], row[1], row[2], row[3], float(row[4]), int(row[5])))
    archivo.close()

    with open("Contratados.csv") as archivo:
        reader = csv.reader(archivo, delimiter=";")
        for row in reader:
            ce.agregarEmpleado(Contratado(row[0], row[1], row[2], row[3],
            datetime.strptime(row[4], "%d/%m/%Y"), datetime.strptime(row[5], "%d/%m/%Y"), int(row[6])))
    archivo.close()

    with open("Externos.csv") as archivo:
        reader = csv.reader(archivo, delimiter=";")
        for row in reader:
            ce.agregarEmpleado(Externo(row[0], row[1], row[2], row[3], row[4],
            datetime.strptime(row[5], "%d/%m/%Y"), datetime.strptime(row[6], "%d/%m/%Y"),
            float(row[7]), float(row[8]), float(row[9])))
    archivo.close()

    Contratado.setValorPorHora(float(300))  # Valor de la hora para empleados contratados

def tesorero(ce):
    dni = input('DNI del empledo: ')
    sueldo = ce.gastosSueldoPorEmpleado(dni)
    if sueldo is not None:
        print('Sueldo: ${:.2f}'.format(sueldo))
    else:
        print('No es posible calcular el sueldo')

def gerente(ce):
    op = int(input('1. Planta - 2. Contratado - 3. Externo: '))
    dni = input('DNI del empleado: ')
    if op == 1:
        ce.modificarBasicoEPlanta(dni, float(input('Nuevo sueldo básico: ')))
    elif op == 2:
        ce.modificarValorEPorHora(dni, float(input('Nuevo valor por hora: ')))
    else:
        ce.modificarViaticoEExterno(dni, float(input('Nuevo monto viatico: ')))

def testInterfaces(ce):
    cargarArreglo(ce)
    print(ce)
    usuario = input('Usuario (Tesorero/Gerente): ')
    clave = input('Clave: ')
    if usuario.lower() == 'uTesorero'.lower() and clave == 'ag@74ck':
        '''testeando tesorero '''
        tesorero(ITesorero(ce))
    else:
        if usuario.lower() == 'uGerente'.lower() and clave == 'ufC77#!1':
            '''testeado gerente'''
            gerente(IGerente(ce))
    menu = Menu()
    menu.mostrarMenu(ce)

if __name__ == '__main__':
    ce = ManejadorE(int(9))  # Cantidad de Empleados
    testInterfaces(ce)