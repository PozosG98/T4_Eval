'''Se denominará una clase padre general donde se colocarán los atributos
propios que tendrán los empleados de la empresa en la que se encuentran
trabajando o buscando una oportunidad de empleo.
Además de ello, se crearán más clases para determinar su vestimenta, conforme a
los requisitos que se piden para realizar el programa.'''

#import Datos
class vestirGerente:
    def __init__(self, saco, botones):
        self.__saco = saco
        self.__botones = botones

    def getterSaco(self):
        return self.__saco
    def getterBotones(self):
        return self.__botones

    def outfit(self):
        print("Odio la informalidad, así que traigo un ", self.__saco, "gris oxford con", self.__botones )
sacoGerente = vestirGerente("Saco", "3 botones")
