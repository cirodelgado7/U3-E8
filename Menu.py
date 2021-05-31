class Menu:

    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.salir
            }

    def mostrarMenu(self, ce):
        salir = False
        while not salir:
            print("\n***** Empresa Constructora *****")
            print("*************** Menu ***************\n"
                  "1. Registrar horas"
                  "\n2. Total de tarea"
                  "\n3. Ayuda"
                  "\n4. Calcular sueldo"
                  "\n5. Salir")
            op = int(input('Ingrese una opcion: '))
            if op in range(1, 6) and type(op) is not str:
                self.opcion(op, ce)
                salir = op == 5
            else:
                print('La opción ingresada no es valida. Ingrese una opción válida')

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, ce):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(ce)

    def opcion1(self, ce):
        ce.registrarHoras()

    def opcion2(self, ce):
        ce.totalTarea()

    def opcion3(self, ce):
        ce.ayuda()

    def opcion4(self, ce):
        ce.calcularSueldo()

    def salir(self, ce):
        print('Salir')