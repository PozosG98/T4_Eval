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
Este será el programa principal. Se crearán algunos programas de clases más, conforme a los datos que 
se solicitan por el docente de la materia.
"""

# Empleados ---> Gerente y persona ---> Contratación ---> Empresa
# Vestimenta ---> Tipos de vestimentas en horarios laborales ---> Saco, Suéter, Jeans, Botas, Casco, etc
# Vestimenta se puede cambiar por "Acciones", tomar en cuenta.
# Entrevistas <--- Gerente
# Empleados (que no sean el gerente) ---> Actividades por hacer <--- Gerente ---> Realizar entrevistas y supervisión del personal


print("Sea bienvenido al programa de la empresa... ¡Qué tenga un buen dia!")

# Definiendo bien el funcionamiento del proyecto, se definió una estructura base a partir
# de un diagrama de clases, pero conforme se va programando, se van implementando nuevas formas y maneras
# de llegar a una mejor solución. Por el momento hasta aquí llegaré.