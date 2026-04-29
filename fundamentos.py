print("Hola, mundo")

# Tipo de escritura
 
nombre = "Juan David"
apellido = "Lopez Chaparro"
edad = "18"
altura = "1.80"
activo = True
correo = "ownercreater@gmail.com"
telefono = "3208829858"
cedula = "1052839903"


print(type(nombre), nombre)
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono), telefono)
print


telefono = int(telefono)
print(type(telefono))

# Identacion en python

if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 en menor que 2")
#inputs
nombre_completo = input("ingrese su nombre completo: ")
print(nombre_completo)

edad = int(input("ingrese su edad: "))
print(type(edad), edad, "años")

print("Hola, " + nombre_completo + " tienes " + str(edad) + " años")

#PRINT CON FORMATO f

print(f"hola {nombre_completo}", "tienes {edad}, anos")


#operadores aritemticos
a = float(input("ingrese su primer valor "))
b = float(input("ingrese su segundo valor "))

print("eliga que operacion quiere realizar")

tipo_de_operacion=input(int("ingrese el tipo de operacion que requiere"))
if tipo_de_operacion == 1:
    print("suma")
elif tipo_de_operacion == 2:
    print("resta")
elif tipo_de_operacion == 3:
    print("multiplicacion")
elif tipo_de_operacion == 4:
    print("division")
elif tipo_de_operacion == 5:
    print("modulo")
elif tipo_de_operacion == 6:
    print("potencia")



suma = (a+b)
resta = (a-b)
multiplicacion=(a*b)
division=(a/b)
modulo=(a%b)
potencia=(a**b)

print("la suma es: ", suma)