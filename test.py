primer_valor=input("ingrese el primer valor")
segundo_valor=input("ingrese el segundo valor")

print("ingrese el numero de la operacion que desea realizar")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. potencia")

operacion=input("ingrese el numero de la operacion que desea realizar")

if operacion=="1":
    resultado=int(primer_valor)+int(segundo_valor)
    print("el resultado de la suma es: ", resultado)
elif operacion=="2":
    resultado=int(primer_valor)-int(segundo_valor)
    print("el resultado de la resta es: ", resultado)
elif operacion=="3":
    resultado=int(primer_valor)*int(segundo_valor)
    print("el resultado de la multiplicacion es: ", resultado)
elif operacion=="4":
    resultado=int(primer_valor)/int(segundo_valor)
    print("el resultado de la division es: ", resultado)
elif operacion=="5":
    resultado=int(primer_valor)**int(segundo_valor)
    print("el resultado de la potencia es: ", resultado)
else:
    print("operacion no valida") 
