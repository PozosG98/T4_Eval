class Empleados:
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