'''En el presente archivo de la clase empleados se tienen los datos más
   importantes para cada empleado que labore o quiera laborar en le empresa'''

class datosEmpleados:
    def __init__(self, Puesto, Nombre, Edad, Genero, Estatura, Peso):
        self.__Puesto = Puesto
        self.__Nombre = Nombre
        self.__Edad = Edad
        self.__Genero = Genero
        self.__Estatura = Estatura
        self.__Peso = Peso

    # Getters
    def getPuesto(self):
        return self.__Puesto
    def getNombre(self):
        return self.__Nombre
    def getEdad(self):
        return self.__Edad
    def getGenero(self):
        return self.__Genero
    def getEstatura(self):
        return self.__Estatura
    def getPeso(self):
        return self.__Peso

    # Setters
    def setPuesto(self, newPuesto):
        self.__Puesto = newPuesto
    def setNombre(self, newNombre):
        self.__Nombre = newNombre
    def setEdad(self, newEdad):
        self.__Edad = newEdad
    def setGenero(self, newGenero):
        self.__Genero = newGenero
    def setEstatura(self, newEstatura):
        self.__Estatura = newEstatura
    def setPeso(self, newPeso):
        self.__Peso = newPeso


class Uniformes(datosEmpleados):
    def __init__(self, Oberol, Botas, Casco, Guantes):
        self.__Oberol = Oberol
        self.__Botas = Botas
        self.__Casco = Casco
        self.__Guantes = Guantes

    def getterOberol(self):
        return self.__Oberol
    def getterBotas(self):
        return self.__Botas
    def getterCasco(self):
        return self.__Casco
    def getterGuantas(self):
        return self.__Guantes

class Formal(datosEmpleados):
    def __init__(self, saco, camisa, corbata, topknot, pantalonFormal):
        self.__saco = saco
        self.__camisa = camisa
        self.__corbata = corbata
        self.__topknot = topknot
        self.__pantalonFormal = pantalonFormal

    def getterSaco(self):
        return self.__saco
    def getterCamisa(self):
        return self.__camisa
    def getterCorbata(self):
        return self.__corbata
    def getterTopknot(self):
        return self.__topknot
    def getterPFormal(self):
        return self.__pantalonFormal

    def setterSaco(self, nSaco):
        self.__saco = nSaco
    def setterCamisa(self, nCamisa):
        self.__camisa = nCamisa
    def setterCorbata(self, nCorbata):
        self.__corbata = nCorbata
    def setterTopknot(self, nMono):
        self.__topknot = nMono
    def setterPFormal(self, nPFormal):
        self.__pantalonFormal = nPFormal


class Gerente:
    def __init__(self, Puesto, Nombre, Edad, Genero, Estatura, Peso, ):