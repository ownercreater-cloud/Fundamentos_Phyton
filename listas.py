# Listas

# Estructura de una lista

aprendices=["Simon","Camilo","David"]
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