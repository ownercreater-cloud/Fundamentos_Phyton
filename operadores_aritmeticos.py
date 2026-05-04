# Operdaores aritmeticos

a = 5
b = 10

# suma

suma = a + b
print(f"la suma de {a} y {b} es: {suma}")

# resta 
resta = a - b
print(f"la resta de {a} y {b} es: {resta}")

#multiplicacion
multiplicacion = a * b
print(f"la multiplicacion de {a} y {b} es: {multiplicacion}")

#division
division = a / b    
print(f"la division de {a} y {b} es: {division}")

#modulo
modulo = a % b
print(f"el modulo de {a} y {b} es: {modulo}")

#potencia
potencia = a ** b
print(f"la potencia de {a} y {b} es: {potencia}")

#precedencia de operadores
resultado = a + b * 2
print(f"el resultado de la precededncia de ({a} + {b} * 2) es: {resultado}")

resultado_2 = (a + b) * 2
print(f"el resultado de la precededncia de ({a} + {b} * 2) es: {resultado_2}")
resultado_3 = a * b // 3
print(f"el resultado de la precededncia de ({a} + {b} * 2) es: {resultado_3}")
resultado_4 = (a * b) // 3
print(f"el resultado de la precededncia de ({a} + {b} * 2) es: {resultado_4}")
resultado_5 = a *(b // 3)
print(f"el resultado de la precededncia de ({a} + {b} * 2) es: {resultado_5}")

ejercicio = ((a+b) *(a-b) / (a*b))-((a ** b)% 3)
print(f"el resultado de la operacion ({a}+{b})*({a}-{b})/({a}*{b})es{ejercicio}")

# librerias matematicas
# las librerias y los imports deben llamarse en las primeras lineas del codigo

import math

# help(math)

print(math.pi)
print(math.e)
print(math.sqrt(16))

import random

random.random() #numero aleatorio entre 0 y 1
numero_aleatorio = random.randint(1, 10)#numro aleatorio entre 0 y 10
print(numero_aleatorio)
