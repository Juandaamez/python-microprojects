#Juan David Amezquita Nuñez
# 1. Contador Simple: 
# Diseñar un programa que solicite al usuario ingresar un número y luego muestre en pantalla los números del 1 al número ingresado.
numero = int(input("Por favor ingrese un numero: "))
cont = 1

for i in range(numero):
    print(cont)
    cont = cont + 1