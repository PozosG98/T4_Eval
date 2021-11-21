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

"""
Este será el programa principal. Se crearán algunos programas de clases más, 
conforme a los datos que se solicitan por el docente de la materia.
"""
'''
import Datos
#Empleado1 = Datos.Empleados("Gerente", "Pozos Guzmán Luis Ángel", "23 años", "Másculino", "1.80 cm", "85 kg")
#Empleado1.infoEmpleados()

print(" ")
print("Sea bienvenido a Coca Cola... ¡Qué tenga un buen dia!")

print("Digite su rol en la empresa... \n",
      " 1 --> Gerente", "\n", " 2 --> Empleado", "\n", " 3 --> Vengo a una entrevista de trabajo")

print(" ")

"""Metemos en un ciclo infinito a nuestras funciones implementadas a continuación..."""
while True:
            try:
                print(" ")
                rol = int(input("Por favor digite el número de su interés: "))
                #Implementamos un if para dar a elegir entre los números 1 al 3
                if ((rol >= 1) & (rol <= 3)):
                    if rol == 1:
                        print("Gerente...")
                        print("Para seguir su proceso es necesario ingresar sus datos en el siguiente formato", "\n",
                              "Nombre, Sexo, Edad_años, Estatura_m, Cargo, Antiguedad")

                        print("Digite su nombre: ")

                        Datos = input(Datos.Gerente)
                        print(Datos)
                        break

            except ValueError:
                print("Ingrese solo valores en el rango del 1 al 3...")
'''

import Datos
