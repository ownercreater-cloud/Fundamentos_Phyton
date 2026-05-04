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


