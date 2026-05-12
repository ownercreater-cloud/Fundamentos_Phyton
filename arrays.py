# Listas

# Estructura de una lista

aprendices=["Simon","Camilo","David","Valentina"]
print(type(aprendices))

#Lista de aprendices Sena ADSO
#indices           1        2       3       4      5
#indices negativos -5       -4      -3     -2     -1
aprendicesAdso=["David","Camilo","Leidy","Milo","Juan"]
print(aprendicesAdso)

# Acceder a un elemento de la lista
print(aprendicesAdso[1]) # Camilo

# Modificar elemento de la lista
aprendicesAdso[2] = "Daniel"
print(aprendicesAdso)

# Listas mixtas
listaMixta=["hola", 123, 3.14, True, [1,2,3]]
print(listaMixta)

print(aprendices[0:2])

# Consultar rangos de elementos de la lista

print(aprendicesAdso[2:4])

# Concatenar lista 

aprendices_adso = aprendicesAdso + aprendices
print(aprendices_adso)

# Unir listas con extend 

aprendices.extend(aprendicesAdso)
print(aprendices)

# Medir el largo de una lista con len()

print(len(aprendices)) #8

#contar elementos repetidos

count_David = aprendices_adso.count("David")
print(f"el nombre David se repite {count_David} veces en la lista")

# Obtener el indice de un elemento con index()

indice_valentina = aprendices_adso.index("Valentina")
print(indice_valentina)

# Copiar una lista con copy()

nueva_lista = aprendices_adso.copy()
print(nueva_lista)

# Agregar elemntos nuevos

nueva_lista.insert(1, "James")
nueva_lista. append("falcao")
print(nueva_lista)

# Eliminar elementos (remove y pop)


# Remove es para el nombre
nueva_lista.remove("James")
print(nueva_lista)

# pop es para borrar un elemento de una lista segun su indice

nueva_lista.pop(1)
print(nueva_lista)

# Comprobar pertenencia

if "Messi" in nueva_lista:
    print("Messi esta en esta lista")
else:
    print("Messi no esta en esta lista")

# Ordenar (sort() y )

# sort


 # de la a-z
nueva_lista.sort()
print(nueva_lista)
# de la z-a
nueva_lista.reverse()
print(nueva_lista)




