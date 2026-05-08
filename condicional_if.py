# Condicional IF/ELIF/ELSE

if True:
    print("La condicion es verdadera")
elif False:
    print("La segunda condicion es verdadera")
elif True:
    print("La tercera condicion es verdadera")
else:
    print("la condicion es falsa")

# Ejercicio: Clasificacion de edad

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    if edad  >= 65:
        print("Usted es un adulto mayor")
elif edad > 12 and edad < 18: 
    print("Usted es un Adolescente")       
else:
    print("Usted es un infante")
# Ejercicio Profe


# Operador Ternario

numero = 10

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

print("el numero es par" if numero % 2 == 0 else "el numero es impar")