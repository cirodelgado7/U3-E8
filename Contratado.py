from Empleado import Empleado


class Contratado(Empleado):
    __fechaInicio = ''
    __fechaFinalizacion = ''
    __cantidadHorasTrabajadas = 0

    valorPorHora = 0

    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFinalizacion, cantidadHorasTrabajadas):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFinalizacion = fechaFinalizacion
        self.__cantidadHorasTrabajadas = cantidadHorasTrabajadas

    def __str__(self):
        return super(Contratado, self).__str__() + \
               '\n Fecha de Inicio del Contrato: {} \n Fecha de Finalización del Contrato: {} ' \
               '\n Cantidad de Horas Trabajadas: {}'\
                   .format(self.__fechaInicio, self.__fechaFinalizacion, self.__cantidadHorasTrabajadas)

    def getHorasTrabajadas(self):
        return self.__cantidadHorasTrabajadas

    @classmethod
    def getValorPorHora(cls):
        return cls.valorPorHora

    @classmethod
    def setValorPorHora(cls, valor):
        cls.valorPorHora = valor

    def Sueldo(self):
        sueldo = self.__cantidadHorasTrabajadas * self.getValorPorHora()
        return sueldo
