#import csv
class Industria:
    def __init__(self, Empresa):
        self.__Empresa = Empresa

    def getterEmpresa(self):
        return self.__Empresa

    def setterEmpresa(self, newNameEm):
        self.__Empresa = newNameEm

    def Empresa(self):
        print('\033[1m' + "Buen día, bienvenido a la planta: ", self.__Empresa)

class Empleados(Industria):
    def __init__(self, cargo):
        self.__cargo = cargo

    def getterCargo(self):
        self.__cargo()
    def setterCargo(self, nCargo):
        self.__cargo = nCargo

class Datos(Empleados):
    def __init__(self, cargo, nombre, estatura, nacionalidad, edad, genero):
        self.__nombre = nombre
        self.__estatura = estatura
        self.__nacionalidad = nacionalidad
        self.__edad = edad
        self.__genero = genero
        self.__cargo = cargo
        super().__init__(cargo)

    def getterNombre(self):
        self.__nombre()
    def getterEstatura(self):
        self.__estatura()
    def getterNacionalidad(self):
        self.__nacionalidad()
    def getterEdad(self):
        self.__edad()
    def getterGenero(self):
        self.__genero()

    def mostrarInfo(self):
        print(" ")
        print("Me presento, me llamo", self.__nombre, ", mi estatura es", self.__estatura,
              "tengo nacionalidad", self.__nacionalidad, " y tengo", self.__edad)
        print("Soy el gerente de la empresa, me identifico con el genero", self.__genero, '\n')

class vestirGerente:
    def __init__(self, saco, botones):
        self.__saco = saco
        self.__botones = botones

    def getterSaco(self):
        return self.__saco
    def getterBotones(self):
        return self.__botones

    def outfit(self):
        print("No me gusta vestir formal, así que hoy me puse un ", self.__saco, " color gris oxford con", self.__botones )
