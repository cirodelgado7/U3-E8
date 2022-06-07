from Menu import Menu
from ObjectEncoder import ObjectEncoder
from ITesorero import ITesorero
from IDirector import IDirector


def tesorero(lista): #muestra el sueldo para tesorero segun un dni
    dni = input('DNI del agente: ')
    sueldo = lista.gastosSueldoPorEmpleado(dni)
    if sueldo != 0:
        print('Sueldo: ${:.2f}'.format(sueldo))
    else:
        print('No es posible calcular el sueldo')


def director(lista): #muestra un menu para director
    op = int(input('\n1.Modificar Básico'
                   '\n2.Modificar Porcentaje por Cargo'
                   '\n3.Modificar porcentaje por categoría'
                   '\n4.Modificar porcentaje extra '
                   '\n Opcion: '))
    dni = input('DNI del empleado: ')
    if op == 1:
        lista.modificarBasico(dni, float(input('Nuevo sueldo básico: ')))
    elif op == 2:
        lista.modificarPorcentajeporcargo(dni, float(input('Nuevo porcentaje por cargo: ')))
    elif op == 3:
        lista.modificarPorcentajeporcategoria(dni, float(input('Nuevo porcentaje por categoría: ')))
    elif op == 4:
        lista.modificarImporteExtra(dni, float(input('Nuevo porcentaje extra: ')))


def testInterfaces(lista): #verifica el tesorero o el director
    usuario = input('Usuario (Tesorero/Director): ')
    clave = input('Clave: ')
    if usuario.lower() == 'uTesorero'.lower() and clave == 'ag@74ck':
        '''testeando tesorero '''
        tesorero(ITesorero(lista))
    else:
        if usuario.lower() == 'uDirector'.lower() and clave == 'ufC77#!1':
            '''testeado director'''
            director(IDirector(lista))
    menu = Menu()
    menu.mostrarMenu(lista)


if __name__ == "__main__":
    encoder = ObjectEncoder()
    try:
        lista = encoder.decodificarDiccionario(encoder.reader("personal.json"))
        print('-------------------------------------------------------------------')
        for nodo in lista:
            print(nodo)
        testInterfaces(lista)
        encoder.writer(lista.toJSON(), "personal.json")
        del encoder
    except FileNotFoundError:
        print('No es posible abrir el archivo')
