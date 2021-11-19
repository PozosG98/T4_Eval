'''Se denominará una clase padre general donde se colocarán los atributos
propios que tendrán los empleados de la empresa en la que se encuentran
trabajando o buscando una oportunidad de empleo.
Además de ello, se crearán más clases para determinar su vestimenta, conforme a
los requisitos que se piden para realizar el programa.'''

import Datos
print("Vestimenta del personal que labore en la empresa")

class Uniformes(Empleados):
    def __init__(self, Oberol, Botas, Casco, Guantes):
        Empleados.__init__()