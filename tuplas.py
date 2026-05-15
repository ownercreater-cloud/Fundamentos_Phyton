#Tuplas

# Estructura de una tupla

tupla = ("Elemento 1", "Elemento 2", "Elemento 3")
print(type(tupla))

tupla_2 = "a", "b", "c"
print(type(tupla))

tupla_3 = (type("Hola"))

tupla_mixta = ("hola", 123, 3.14, True, [1, 2, 3])
print(tupla_mixta)

aprendices = ("Simon", "Camilo", "Santiago", "Valentina", "Laura")

print(aprendices)

# Acceder a un elemneto de la tupla
# aprendices[2] = "Daniel" # Esto generara un error porque las tuplas son inmutables

# Consultar rangos de elemento de la tupla
print(aprendices[0:2]) #("Simon", "Camilo")
print(aprendices[1:4])
print(aprendices[1:])

# Sumar 2 tuplas 
tupla_suma = tupla + tupla_2
print(tupla_suma)

multiplicacion_tupla = tupla * 3
print(multiplicacion_tupla)

# Metodos de tuplas

# Medir el largo del len()
print(len(aprendices))

# Contar elemntos repetidos en una tupla con count


print(aprendices.count("Camilo"))
print(aprendices.index("Valentina"))

# Modificar una tupla en una lista

print(type(aprendices))

aprendices_lista = list(aprendices)
aprendices_lista.append("Felipe")
print(type(aprendices_lista))

aprendices = tuple(aprendices_lista)
print(type(aprendices))

# Comprobar pertenencia

print("Simon" in aprendices)
print("Andres" in aprendices)

# Empaquetar tuplas

programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "Topografia" 


tupla_programas = (programa_1, programa_2, programa_3)
print(tupla_programas)


# Desempaquetar programas

tupla_desepaquetada = ("ADSO", "SST", "Topografia")
programa_1, programa_2, programa_3 = tupla_desepaquetada
print(programa_1)  #ADSO

