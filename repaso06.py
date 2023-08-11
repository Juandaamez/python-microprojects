#Juan David Amezquita Nuñez
# 6.Adivinar el Número: 
# Crear un juego en el que el pc elija un numero aleatorio y el jugador tenga que adivinarlo. El pc debe proporcionar pistas si el número es mayor o menor.
import random

numero_objetivo = random.randint(1,50)
numero = int(input("Adivina el numero, ingresa un numero: "))

while (numero_objetivo != numero):

    if numero > numero_objetivo:
        print(f"{numero} es muy grande")
    if numero < numero_objetivo:
        print(f"{numero} es muy pequeño")

    numero = int(input("Adivina el numero, ingresa un numero: "))

print(f"Felicidades, el numero es {numero_objetivo}")