# Clasificador de IMC

from curses.ascii import alt


peso = float(input("ingrese su peso en KG!!"))
altura = float(input("ingrese su altura en MT!!"))

IMC = peso/(altura**2)

print(f"su IMC")
