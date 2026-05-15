#CONJUNTOS (SETS) EN PYTHON

conjunto = set()
print(type(conjunto))

#creacion
lenguajes = {"python", "java", "C++"}
print(lenguajes)

#metodos de mof=dificacion 
frutas = {"mango", "guayaba", "mora"}
frutas.add("maracuya")    #agrega un elemento
frutas.add("mango")       #no hace nada, ya existe
frutas.remove("mora")     #elimina; lanza keyerror si no existe
frutas.discard("papaya")  #elimina; no lanza error si no existe
elem = frutas.pop()       #elimina y retorna un elemento aleatorio
print(frutas)

#verificar pertenenciaa :0(1)
print("python" in lenguajes) 
print("COBOL" in lenguajes)

python_devs ={"camilo", "leonardo", "miguel", "sharit"}
java_devs ={"manolo", "simon", "miguel", "leonardo"}

todos = python_devs | java_devs
union= python_devs.union(java_devs)
print("union", todos )

#interseccion 

ambos = python_devs & java_devs
interseccion = python_devs.intersection(java_devs)
print("interseccion", ambos)

#diferencia
solo_python = python_devs - java_devs
print("solo_python", solo_python)

solo_java = java_devs - python_devs
print("solo_java",solo_java  )

#diferencia simetrica

diferencia_simetrica = python_devs ^ java_devs
print("diferencia_simetrica", diferencia_simetrica)



