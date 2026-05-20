# Diccionarios (Caracteristicas a un elemento)

#creacion de un diccionario

#Estrcutura de un diccionario

diccionario = {
    "clave 1": "valor 1",
    "clave 2": "valor 2",
    "clave 3": "valor 3"
}


# diccionario vacio
diccionario_vacio = {}

# Diccionario aprendiz

diccionario_aprendiz = {
    "nombre": "David",
    "aprellido": "Lopez",
    "programa": "ADSO",
    "ficha": "3321349",
    "edad": "18"
}

print(type(diccionario_aprendiz)) # class <dict>

# Obtener valor del diccionario
print(diccionario_aprendiz["programa"])
print(diccionario_aprendiz.get("programa"))

#Obtener solo las claves del diccionario

print(diccionario_aprendiz.keys())

# Obtener solo los valores del diccionario

print(diccionario_aprendiz.values())

# Obtener la clave y el valor

print(diccionario_aprendiz.items())

# Agregar un nuevo elemento al diccionario

diccionario_aprendiz["correo"]= "ownercreater@gmail.com"

# Modificar un valor de un diccionario

diccionario_aprendiz["programa"]= "SST"
print(diccionario_aprendiz)

# Metodo UPDATE()

diccionario_aprendiz.update({"nombre": "Andres"})

# Recorrer sololas claves del diccionario
for claves  in diccionario_aprendiz.keys():
    print(claves)

#recorres solo los valores del diccionario

for valor in diccionario_aprendiz.values():
    print(valor)

# Recorrer las claves y los valores del diccioanrio 

for clave, valor in diccionario_aprendiz.items():
    print(f"{clave}, {valor}")

# Eliminar Elementos de un diccionario POP()

diccionario_aprendiz.popitem() # borra el ultimo elemento del diccionario
print(diccionario_aprendiz)

diccionario_aprendiz.popitem("edad") # borra el elemento edad del diccionario
print(diccionario_aprendiz)

diccionario_aprendiz.clear()
print(diccionario_aprendiz)

#diccionarioa anidados 
aprendiz = {
    "aprendiz_1":{
    "nombre": "David",
    "aprellido": "Lopez",
    "programa": "ADSO",
    "ficha": "3321349",
    "edad": "18"
    }
}

aprendiz_2 = {
    "nombre": "miguel",
    "aprellido": "castaneda",
    "programa": "ADSO",
    "ficha": "3321349",
    "edad": "19"
}

print(aprendiz["aprendiz_1":]["programa"])

for aprendiz,datos in aprendiz.items():
    print(f"{aprendiz}")
    for clave, valor in datos.items():
        print(f"{clave}:{valor}")
