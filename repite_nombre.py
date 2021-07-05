'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas
 el nombre del usuario tantas veces como el número introducido.'''

# IMporta la clase del sistema operativo para limpiar pantalla
from os import system

# Comando que Limpia pantalla
system("cls")

# Toma de datos
print("Programa que repite el nombre cuantas veces se quiera\n")
usuario  = input("Nombre del usuario: ")
nombre = input("\nEscriba nombre a repetir: ")
numero = int(input("\nCuantas veces deseas repetir ese nombre? "))
print()

# Bucle que recorre tantas veces como indique el usuario e imprime la variable nombre en cada iteracción
i = 1
for i in range(numero):
    print("N° {} ==> {}".format(i+1, nombre))

print()
print("Estimad@ {} el nombre se imprimió {} veces\n".format(usuario, numero))