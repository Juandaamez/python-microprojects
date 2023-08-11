#Juan David Amezquita Nuñez
# 3. Palindromos: Revisar si una cadena de texto es un palindromo
palabra = input("Ingrese una palabra: ")

def palidromo(palabra):
    return palabra[::-1]

if palabra == palidromo(palabra):
    print("Si es palindormo")
else:
    print("No es palindromo")