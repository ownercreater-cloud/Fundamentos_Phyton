#operdaores aritmeticos


a = float(input("Ingrese su primer valor: "))
b = float(input("Ingrese su segundo valor: "))

print("Elija que operación quiere realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Módulo")
print("6. Potencia")

tipo_de_operacion = int(input("Ingrese el número de la operación: "))

if tipo_de_operacion == 1:
    print("La suma es:", a + b)
elif tipo_de_operacion == 2:
    print("La resta es:", a - b)
elif tipo_de_operacion == 3:
    print("La multiplicación es:", a * b)
elif tipo_de_operacion == 4:
    if b != 0:
        print("La división es:", a / b)
    else:
        print("Error: división por cero")
elif tipo_de_operacion == 5:
    print("El módulo es:", a % b)
elif tipo_de_operacion == 6:
    print("La potencia es:", a ** b)
else:
    print("Opción inválida")
