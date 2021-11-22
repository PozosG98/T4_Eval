'''
FR7A. PROGRAMACIÓN AVANZADA
EVALUACIÓN TEMA 4. MODELAR UN GERENTE.

Escriba una aplicación que modele en el paradigma orientado a objetos el siguiente escenario:
“El gerente de la empresa es un empleado que mide 1.80 m, se llama <nombre> y tiene puesto un saco con tres botones.
En este momento el gerente está entrevistando a una persona para su contratación.”

Deberás generar múltiples archivos que representen la situación de la vida real en términos de programación.
Así tendrás varias clases como son: gerente, persona, empleado, empresa, vestimenta, saco, etc.
Debes establecer en ellas comportamientos como vestirse, trabajar y entrevistar que hagan que el escenario cobre vida.
'''

import Programa_Principal as principal
import csv
print(" ")
Empresa1 = principal.Industria("General Motors..." + '\033[0m')
Empresa1.Empresa()

print("Digite el número 1 o 2 de acuerdo con lo que desee realizar... \n",
      " 1 --> Gerente", "\n", " 2 --> Salir", "\n")
while True:
    try:
        Select = float(input("Marque 1 o 2 según sea el caso: "))
        if ((Select >=1) & (Select <= 2)):
            if Select ==1:
                print("Bienvenido Sr. Gerente")
                Name = input("Ingrese sus datos para verificar si tiene cita con nuestro gerente por favor: ")
                Genre = principal.Datos(Name, "Luis", "1.85 cm", "Colombiana", "24 años", "masculino")
                Genre.mostrarInfo()

                sacoGerente = principal.vestirGerente("saco", "3 botones")
                sacoGerente.outfit()
                break
        if Select == 2:
            print("Que tenga un buen día, gracias")
            break
        else:
            print("Ingrese un valor que se encuentre en el valor correcto...")
            break
    except ValueError:
        print("Ingrese solo números...")

print(" ")
print("Elija el número de acuerdo con lo que desee realizar:", "\n",
        "1. Realizar entrevista...", "\n",
        "2. Salir... ")
while True:
    try:
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
                print("7. ¿Cuenta con alguna certificación que lo especialice en alguna rama específica en la empresa?",
                      self.G)
                print("8. Si en algún momento llega a ocurrir algún problema en la planta y no sabe como resolverlo, "
                      "¿Qué alternativas propones de solución?", self.H)
                print("9. ¿Qué te hace diferente de otros candidatos al puesto que solicitas?", self.I)
                print("10. ¿Qué te motiva en la vida?", self.J)

        entrevistar = float(input("Marque 1, si desea tener una entrevista: "))
        if (entrevistar == 1):
            if entrevistar == 1:
                print("Sea bienvenido, en un momento lo atenderemos...")
                #break
                #print(" ")
                # print("Mostrando sus respuestas en la consola...")

            print("Por favor, responda con sinceridad: ")
            A = input("1. Dígame sus motivos por los cuales desea trabajar con nosotros: ")
            B = input("2. Cuénteme la perspectiva que tiene de la empresa: ")
            C = input("3. ¿Cuenta con flexibilidad de horario?")
            D = input("4. ¿Tiene la facilidad de viajar? ")
            E = input("5. Del 0 al 100 %, digame con que porcentaje de inglés cuenta: ")
            F = input("6. ¿Qué metas tiene a corto, mediano y largo plazo? ")
            G = input(
                "7. ¿Cuenta con alguna certificación que lo especialice en alguna rama específica en la empresa? ")
            H = input(
                "8. Si en algún momento llega a ocurrir algún problema en la planta y no sabe como resolverlo, "
                "¿Qué alternativas de solución accionarías? ")
            I = input("9. ¿Qué te hace diferente de otros candidatos al puesto que solicitas? ")
            J = input("10. ¿Qué te motiva en la vida? ")
            enterview = Entrevistar(A, B, C, D, E, F, G, H, I, J)
            enterview.entrevistarPersonal()
            break
        else:
            print("Ingrese un valor que se encuentre en el valor correcto...")
    except ValueError:
        print("Ingrese solo números...")

with open('Respuestas.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow([f"1. Dígame sus motivos por los cuales desea trabajar con nosotros: {A} "])
    spamwriter.writerow([f"2. Cuénteme la perspectiva que tiene de la empresa {B}"])
    spamwriter.writerow([f"3. ¿Cuenta con flexibilidad de horario? {C} "])
    spamwriter.writerow([f"4. ¿Tiene la facilidad de viajar? {D} "])
    spamwriter.writerow([f"5. Del 0 al 100 %, digame con que porcentaje de inglés cuenta {E} "])
    spamwriter.writerow([f"6. ¿Qué metas tiene a corto, mediano y largo plazo? {F} "])
    spamwriter.writerow([
                            f"7. ¿Cuenta con alguna certificación que lo especialice en alguna rama específica en la empresa? {G} "])
    spamwriter.writerow(
        [f"8. Si en algún momento llega a ocurrir algún problema en la planta y no sabe como resolverlo, "
         f"¿Qué alternativas propones de solución? {H} "])
    spamwriter.writerow([f"9. ¿Qué te hace diferente de otros candidatos al puesto que solicitas? {I} "])
    spamwriter.writerow([f"10. ¿Qué te motiva en la vida? {J} "])
    # else:
    print("Gracias por responder, sus respuestas se han guardado en el archivo .csv para su revisión...")



