'''En el presente archivo de la clase empleados se tienen los datos más
   importantes para cada empleado que labore o quiera laborar en le empresa'''
import csv
class Industria:
    def __init__(self, Empresa):
        self.__Empresa = Empresa

    def getterEmpresa(self):
        return self.__Empresa

    def setterEmpresa(self, newNameEm):
        self.__Empresa = newNameEm

    def Empresa(self):
        print('\033[1m' + "Buen día, bienvenido a la planta: ", self.__Empresa)
print(" ")
Empresa1 = Industria("General Motors..." + '\033[0m')
Empresa1.Empresa()

#print('\033[4;36m' + "Digite su rol en la empresa...", "\n" + '\033[0m',
#      " 1 --> Gerente", "\n", " 2 --> Salir", "\n")

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
        print("A continuación le haré una entrevista para saber un poco más de usted... ")
        print("Me presento, me llamo", self.__nombre, ", mi estatura es", self.__estatura,
              "tengo nacionalidad", self.__nacionalidad, "mi edad es", self.__edad)

        print("Soy el gerente de la empresa, me identifico del genero", self.__genero, '\n')

#Name = input("Ingrese el nombre del entrevistador: ")
#Genre = Datos(Name, "gerente", "1.85 cm", "Colombiana", "24 años", "másculino")
#Genre.mostrarInfo()

class Entrevistar:
    def __init__(self, A, B, C, D, E, F, G, H, I, J):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.G = G
        self.H = H
        self.I = I
        self.J = J
    def entrevistarPersonal(self):
        print("1. Dígame sus motivos por los cuales desea trabajar con nosotros", self.A)
        print("2. Cuénteme la perspectiva que tiene de la empresa", self.B)
        print("3. ¿Cuenta con flexibilidad de horario?", self.C)
        print("4. ¿Tiene la facilidad de viajar?", self.D)
        print("5. Del 0 al 100 %, digame con que porcentaje de inglés cuenta", self.E)
        print("6. ¿Qué metas tiene a corto, mediano y largo plazo?", self.F)
        print("7. ¿Cuenta con alguna certificación que lo especialice en alguna rama específica en la empresa?", self.G)
        print("8. Si en algún momento llega a ocurrir algún problema en la planta y no sabe como resolverlo, "
              "¿Qué alternativas propones de solución?", self.H)
        print("9. ¿Qué te hace diferente de otros candidatos al puesto que solicitas?", self.I)
        print("10. ¿Qué te motiva en la vida?", self.J)

class vestirGerente:
    def __init__(self, saco, botones):
        self.__saco = saco
        self.__botones = botones

    def getterSaco(self):
        return self.__saco
    def getterBotones(self):
        return self.__botones

    def outfit(self):
        print("No me gusta la formalidad, así que hoy traigo puesto un ", self.__saco, "gris oxford con", self.__botones )
sacoGerente = vestirGerente("Saco", "3 botones")
#sacoGerente.outfit()

#while True:
#        try:
marcar= float(input("Para obtener una entrevista, marque 1: "))

if(marcar == 1):
    print("Sea bienvenido, en un momento lo atenderemos...")
    print(" ")
    Name = input("Ingrese el nombre del entrevistador: ")
    Genre = Datos(Name, "gerente", "1.85 cm", "Colombiana", "24 años", "másculino")
    Genre.mostrarInfo()
    sacoGerente.outfit()

    #Name = input("¿Usted tiene cita con? [Ingresar nombre por favor...]: ")
    #P1 = Datos(Name, 'Gerente', "Masculino", "24 años", "1.90")
    #P1.mostrarInfo()

    print("Por favor, responda con sinceridad: ")
    A = input("1. Dígame sus motivos por los cuales desea trabajar con nosotros: ")
    B = input("2. Cuénteme la perspectiva que tiene de la empresa: ")
    C = input("3. ¿Cuenta con flexibilidad de horario?")
    D = input("4. ¿Tiene la facilidad de viajar? ")
    E = input("5. Del 0 al 100 %, digame con que porcentaje de inglés cuenta: ")
    F = input("6. ¿Qué metas tiene a corto, mediano y largo plazo? ")
    G = input("7. ¿Cuenta con alguna certificación que lo especialice en alguna rama específica en la empresa? ")
    H = input("8. Si en algún momento llega a ocurrir algún problema en la planta y no sabe como resolverlo, "
              "¿Qué alternativas de solución accionarías? ")
    I = input("9. ¿Qué te hace diferente de otros candidatos al puesto que solicitas? ")
    J = input("10. ¿Qué te motiva en la vida? ")

    #print("Mostrando sus respuestas en la consola...")
    enterview = Entrevistar(A, B, C, D, E, F, G, H, I, J)
    enterview.entrevistarPersonal()

    with open('Respuestas.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow([f"1. Dígame sus motivos por los cuales desea trabajar con nosotros: {A} "])
        spamwriter.writerow([f"2. Cuénteme la perspectiva que tiene de la empresa {B}"])
        spamwriter.writerow([f"3. ¿Cuenta con flexibilidad de horario? {C} "])
        spamwriter.writerow([f"4. ¿Tiene la facilidad de viajar? {D} "])
        spamwriter.writerow([f"5. Del 0 al 100 %, digame con que porcentaje de inglés cuenta {E} "])
        spamwriter.writerow([f"6. ¿Qué metas tiene a corto, mediano y largo plazo? {F} "])
        spamwriter.writerow([f"7. ¿Cuenta con alguna certificación que lo especialice en alguna rama específica en la empresa? {G} "])
        spamwriter.writerow([f"8. Si en algún momento llega a ocurrir algún problema en la planta y no sabe como resolverlo, "
                             f"¿Qué alternativas propones de solución? {H} "])
        spamwriter.writerow([f"9. ¿Qué te hace diferente de otros candidatos al puesto que solicitas? {I} "])
        spamwriter.writerow([f"10. ¿Qué te motiva en la vida? {J} "])

else:
    print("Gracias por responder, sus respuestas se han guardado en el archivo .csv para su revisión...")

    #Gerente1 = Datos(Gerente, "Luis", "25", "Mexa", "Masculino", "1.80")
    #Gerente1.mostrarInfo()
    #sacoGerente.outfit()
#        except ValueError:
#            print("Ingrese solo números")
#        break

