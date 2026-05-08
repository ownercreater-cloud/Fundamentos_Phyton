#  ejercicio 1

from math import e
from unittest import result


nombre= "David"
producto= 20000
promedio_asignatura= 4.5
print(f"mi nombre es {nombre}, y mi producto es: {producto}, mi promedio en la asignatura es de {promedio_asignatura}.")

# Ejercicio 2

variable_1_entera = 5
variable_2_entera = 10
variable_float = 4.31
variable_1_string = "hola"
variable_2_string = "mundo"

suma_de_numeros = variable_1_entera + variable_2_entera + variable_float
print(f"la suma de mis variables numericas es de {suma_de_numeros}")
print(max(variable_1_entera, variable_2_entera))

division_del_float = variable_float / (variable_1_entera / variable_2_entera)
print(division_del_float)

concatenacion = variable_1_string+ " " +variable_2_string
print(concatenacion)

# Ejercicio 3

base = 6
potencia = 7

potenciacion = base ** potencia
print(potenciacion)

# ejercicio 4


numero = float(input("Ingrese el número al que desea sacarle la raíz: "))
x = numero / 2 
if numero >= 0:
    for _ in range(5):
        x = round(x + (numero - x**2) / (2 * x))
        print(f"La raíz aproximada de {numero} es {x}")
else:
    print("el numero que desea potenciar es 0 o menor de 0")

# Ejercicio 5

estudiante = "David"
nota_1 =  5.0
nota_2 = 5.0
nota_3 = 3.0
nota_4 = 1.0
nota_5 = 3.0

promedio = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

print(f"El estudiante {estudiante} por sus notas tiene un promedio de {promedio}")

# Ejercicio 6

numeroUno = 8
numeroDos = 2
numeroAuxiliar = numeroUno

print(f"{numeroUno},{numeroDos}")

numeroUno = numeroDos
numeroDos = numeroAuxiliar

print(f"{numeroUno},{numeroDos}")

# Ejercicio 7

estado = (5 == 2) or (2 > 1)
print(estado)

#Ejercicio 8

resultado = ((10 + 5 - 3) * 2) / 4 + (7 % 3) + (2 ** 3) - (15 / 5) + (4 * 3) - (9 % 4) + (3 ** 2)

print(resultado)

#Ejercicio 9

ladoCuadrado = 8
areaCuadrado = ladoCuadrado * ladoCuadrado
perimetroCuadrado = ladoCuadrado * 4

baseTriangulo = 9
alturaTriangulo = 8
ladoUnoTriangulo = 8
ladoDosTriangulo = 8
areaTriangulo = (baseTriangulo * alturaTriangulo) / 2
perimetroTriangulo = baseTriangulo + ladoUnoTriangulo + ladoDosTriangulo

baseRectangulo = 8
alturaRectangulo = 6
areaRectangulo = baseRectangulo * alturaRectangulo
perimetroRectangulo = 2 * (baseRectangulo + alturaRectangulo)

print(f"el area del cuadrado es de {areaCuadrado}, y su perimetro es de {perimetroCuadrado}")
print(f"el area del triangulo es de {areaTriangulo}, y su perimetro es de {perimetroTriangulo}")
print(f"el area del rectangulo es de {areaRectangulo}, y su perimetro es de {perimetroRectangulo}")

# Ejercicio 10

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <= 5:
    print("Infante")
elif edad <= 10:
    print("Niño")
elif edad <= 15:
    print("Pre adolescente")
elif edad <= 18:
    print("Adolescente")
elif edad <= 25:
    print("Pre adulto")
elif edad <= 40:
    print("Adulto")
elif edad <= 55:
    print("Pre anciano")
elif edad >= 56:
    print("Anciano")
else:
    print("Edad no válida")







