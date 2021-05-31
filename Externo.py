from Empleado import Empleado

class Externo(Empleado):

    __tarea = ''
    __fechaInicio = ''
    __fechaFinalizacion = ''
    __montoViatico = 0.00
    __costoObra = 0.00
    __montoSeguroDeVida = 0.00

    def __init__(self, dni, nombre, direccion, telefono, tarea, fechaInicio, fechaFinalizacion,
                 montoViatico, costoObra, montoSeguroDeVida):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fechaInicio = fechaInicio
        self.__fechaFinalizacion = fechaFinalizacion
        self.__montoViatico = montoViatico
        self.__costoObra = costoObra
        self.__montoSeguroDeVida = montoSeguroDeVida

    def __str__(self):
        return super(Externo, self).__str__() + \
               '\n Tarea: {} \n Fecha de Inicio de la Tarea: {} \n Fechas de Finalización de la Tarea: {}' \
               '\n Monto por Viático: {} \n Costo de la Obra: {} \n Monto del Seguro de Vida: {}' \
            .format(self.__tarea, self.__fechaInicio, self.__fechaFinalizacion, self.__montoViatico,
                    self.__costoObra, self.__montoSeguroDeVida)

    def getTarea(self):
        return self.__tarea

    def getFinal(self):
        return self.__fechaFinalizacion

    def getCostoObra(self):
        return self.__costoObra

    def setMontoViatico(self, montoViatico):
        self.__montoViatico = montoViatico

    def Sueldo(self):
        return self.__costoObra - self.__montoViatico - self.__montoSeguroDeVida