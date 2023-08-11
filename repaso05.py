#Juan David Amezquita Nuñez
# 5.Contador de Vocales: Diseñar una función que cuente y devuelva la cantidad de vocales de una cadena de texto.
palabra = str(input("Ingrese la palabra: "))

vocales = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

cont = 0

for letra in palabra:
    if letra in vocales:
        cont = cont + 1

print(f"En esta palabra hay {cont} vocales")
