class Empleado:

    __nombre = ''
    __dni = ''
    __direccion = ''
    __telefono = ''

    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def __str__(self):
        return '\n DNI: {} \n Nombre: {} \n Dirección: {} \n Telefono: {}'\
            .format(self.__dni, self.__nombre, self.__direccion, self.__telefono)

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono



