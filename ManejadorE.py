from datetime import datetime
import numpy as np
from Empleado import Empleado
from Contratado import Contratado
from Externo import Externo
from ITesorero import ITesorero
from IGerente import IGerente
from zope.interface import implementer


@implementer(ITesorero)
@implementer(IGerente)

class ManejadorE:

    __cantidad = 0
    __dimension = 0
    __incremento = 10

    def __init__(self, dimension=0, incremento=10):
        self.__Empleados = np.empty(dimension, dtype=Empleado)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def __str__(self):
        s = "\n***** Empleados *****\n"
        for lista in self.__Empleados:
            s += str(lista) + '\n'
        return s

    def agregarEmpleado(self, unEmpleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Empleados.resize(self.__dimension)
        self.__Empleados[self.__cantidad] = unEmpleado
        self.__cantidad += 1

    def registrarHoras(self):
        dni = input('DNI: ')
        horas = int(input('Horas: '))
        i = 0
        r = True
        while i < len(self.__Empleados) and r:
            if type(self.__Empleados[i]) == Contratado and self.__Empleados[i].getDni() == dni:
                self.__Empleados[i].getHorasTrabajadas(horas)
                r = False
            i += 1

    def totalTarea(self):
        tarea = input('Tarea: ')
        acum = 0
        for empleado in self.__Empleados:
            if isinstance(empleado, Externo):
                if empleado.getTarea() == tarea and empleado.getFinal() > datetime.now():
                    acum += empleado.getCostoObra()
        print('Monto a Pagar: {:.2f}'.format(acum))

    def ayuda(self):
        for empleado in self.__Empleados:
            if empleado.Sueldo() < 25000:
                print("\nNombre: {} \nDirección: {} \nDNI: {}"
                      .format(empleado.getNombre(), empleado.getDireccion(), empleado.getDni()))

    def calcularSueldo(self):
        for empleado in self.__Empleados:
            print("\nNombre: {} \nTelefono: {} \nSueldo: {:.2f} \n"
                  .format(empleado.getNombre(), empleado.getTelefono(), empleado.Sueldo()))

    def gastosSueldoPorEmpleado(self, dni):
        i = 0
        while i < len(self.__Empleados) and self.__Empleados[i].getDni() != dni:
            i += 1
        if i < len(self.__Empleados):
            return self.__Empleados[i].Sueldo()
        else:
            return None

    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        i = 0
        while i < len(self.__Empleados) and self.__Empleados[i].getDni() != dni:
            i += 1
        if i < len(self.__Empleados):
            self.__Empleados[i].setSueldoBasico(nuevoBasico)
        else:
            print('No es posible modificar el sueldo básico del empleado de planta')

    def modificarValorEPorHora(self, dni, nuevoValorHora):
        i = 0
        while i < len(self.__Empleados) and self.__Empleados[i].getDni() != dni:
            i += 1
        if i < len(self.__Empleados):
            Contratado.setValorPorHora(nuevoValorHora)
            print(Contratado.getValorPorHora())
        else:
            print('No es posible modificar el valor por hora del empleado contratado')

    def modificarViaticoEExterno(self, dni, nuevoViatico):
        i = 0
        while i < len(self.__Empleados) and self.__Empleados[i].getDni() != dni:
            i += 1
        if i < len(self.__Empleados):
            self.__Empleados[i].setMontoViatico(nuevoViatico)
            print(self)
        else:
            print('No es posible modificar el monto por viáticos del empleado externo')