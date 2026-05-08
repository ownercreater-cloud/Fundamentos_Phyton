calificacion_1 = float(input("Ingrese la nota de su primer parcial: "))
calificacion_2 = float(input("Ingrese la nota de su segundo parcial: "))
calificacion_3 = float(input("Ingrese la nota de su tercer parcial: "))

if ((calificacion_1 or calificacion_2 or calificacion_3) <= 5):
    promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3
    promedio = round(promedio, 2)
    print("su promedio es de:", promedio)


    nota_faltante = round(5.0 - promedio, 2)

    if nota_faltante == 0.0:
        print(f"Su promedio es de {promedio} por lo tanto tiene la nota maxima Felicitaciones!")
    elif promedio >= 3.0:
        print(f"su promedio es de {promedio} por tanto ha aprobado le faltaron {nota_faltante} para la nota maxima")
    else:
        print(f"A usted le hicieron falta{nota_faltante} para la nota maxima")
else:
    print("error: las calificaciones deben ser menores a 5")


