#Juan David Amezquita Nuñez
# 9. Anagramas: Validar si dos palabras son anagramas

def son_anagramas(palabra1, palabra2):
  return sorted(palabra1) == sorted(palabra2)

palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")
if son_anagramas(palabra1, palabra2):
  print(f"{palabra1} y {palabra2} son anagramas")
else:
  print(f"{palabra1} y {palabra2} no son anagramas")