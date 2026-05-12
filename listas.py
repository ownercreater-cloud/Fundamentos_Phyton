# actividad 1: inventario de la tienda escolar

productos = ["Cuaderno", "Esferos", "Lapiz", "Reglas", "Colores"]
precios = [8000.0, 5000.0, 1000.0, 5000.0, 12000.0]
cantidades = [67, 76, 56, 70, 40]

cantidad_productos = len(productos)

print(
    f"Inventario tienda escolar:\n"
    f"Productos: {productos}\n"
    f"Precios: {precios}\n"
    f"Cantidades: {cantidades}\n"
    f"Cantidad de productos: {cantidad_productos}"
)

print(f"La papelería tiene {cantidad_productos} productos")

print(f"El producto {productos[0]} tiene un precio de {precios[0]} y hay una cantidad disponible de {cantidades[0]}")
print(f"El producto {productos[1]} tiene un precio de {precios[1]} y hay una cantidad disponible de {cantidades[1]}")
print(f"El producto {productos[2]} tiene un precio de {precios[2]} y hay una cantidad disponible de {cantidades[2]}")
print(f"El producto {productos[3]} tiene un precio de {precios[3]} y hay una cantidad disponible de {cantidades[3]}")
print(f"El producto {productos[4]} tiene un precio de {precios[4]} y hay una cantidad disponible de {cantidades[4]}")

# Actividad 2

# Actividad 2: Listas y slicing

temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# 2 
print("Temperatura del primer dia:", temperaturas[0])
print("Temperatura del ultimo dia:", temperaturas[-1])
print("Temperatura del dia:", temperaturas[6])
print("Temperatura del penultimo dia:", temperaturas[-2])

# 3
primera_semana = temperaturas[0:7]
segunda_semana = temperaturas[7:14]
dias_pares = temperaturas[1::2]  
invertida = temperaturas[::-1]

print("\nPrimera semana:", primera_semana)
print("Segunda semana:", segunda_semana)
print("Días pares:", dias_pares)
print("Temperaturas invertidas:", invertida)

# 4
promedio_semana1 = sum(primera_semana) / len(primera_semana)
promedio_semana2 = sum(segunda_semana) / len(segunda_semana)

print("\nPromedio semana 1:", promedio_semana1)
print("Promedio semana 2:", promedio_semana2)

# 5
if promedio_semana1 > promedio_semana2:
    print("\nLa primera semana tuvo mayor temperatura promedio")
elif promedio_semana2 > promedio_semana1:
    print("\nLa segunda semana tuvo mayor temperatura promedio")
else:
    print("\nAmbas semanas tuvieron el mismo promedio de temperatura")

# Lista de gestion de lista de reproduccion semanal

# 1 
canciones = ["Eclipse", "Horizonte", "Luz Interna", "Viaje Sonoro", "Reflejos"]

print("lista inicial")
print(canciones, "\n")

# 2 

canciones.append("Nueva Melodia")
print("despues de append")
print(canciones, "\n")

canciones.insert(1, "Intro Especial")
print("despues de insert en la segunda posicion")
print(canciones, "\n")

canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("despues de extend")
print(canciones, "\n")

# 3

canciones.remove("Viaje Sonoro")
print("despues de remove Viaje Sonoro")
print(canciones, "\n")

ultima = canciones.pop()
print("despues de pop")
print(canciones)
print("cancion eliminada con pop", ultima, "\n")

# 4 

canciones.sort()
print("lista ordenada")
print(canciones, "\n")

# 5 
total = len(canciones)
pos_primera_agregada = canciones.index("Nueva Melodia")
bonus1 = canciones.count("Bonus Track 1")

print("total de canciones", total)
print("posicion de Nueva Melodia", pos_primera_agregada)
print("veces que aparece Bonus Track 1", bonus1)
