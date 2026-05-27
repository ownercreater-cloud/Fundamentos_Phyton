i = 0

while i < 6:
    print("hola, soy un bucle WHILE")
    if i == 3:
        break # rompe el ciclo cuando i es igual a 3
i += 1

puntos_de_vida = 100
pokemon = input("elije tu pokemon: pikachu, charmander, bulbasaur: ")


while puntos_de_vida >0:
    print(f"tu pokemon {pokemon} tiene {puntos_de_vida} puntos de vida")
    ataque =input(input("ingrese el dano del ataque: "))
    puntos_de_vida -=ataque
    print(f"tu pokemon {pokemon} ha sido derrotado")

#definir una funcion 
def nombre_funcion()
    
# funcion con parametros 

  def saludar(nombre,apellido):
    return f"hola, {nombre} {apellido}, bienvenido ala programavion con funciones"
print(saludar("felipe"))