#Juan David Amezquita Nuñez
# 7. Calculadora de fracciones: Suma, resta, multiplicacion y division.
from fractions import Fraction

f1 = Fraction(int(input("Ingrese el primer numero de la primera fraccion: ")), int(input("Ingrese el segundo numero de la primera fraccion: ")))
f2 = Fraction(int(input("Ingrese el primer numero de la segunda fraccion: ")), int(input("Ingrese el segundo numero de la segunda fraccion: ")))
op = str(input("Ingrese el la operacion que desea realizar +, -, *, o /:  "))

def calcular(f1, f2, op):
  # f1 y f2 son objetos de tipo Fraction
  # op es una cadena que indica la operación
  if op == "+":
    return f1 + f2 # suma las fracciones y retorna el resultado
  elif op == "-":
    return f1 - f2 # resta las fracciones y retorna el resultado
  elif op == "*":
    return f1 * f2 # multiplica las fracciones y retorna el resultado
  elif op == "/":
    return f1 / f2 # divide las fracciones y retorna el resultado
  else:
    return "Operación inválida" # retorna un mensaje de error si la operación no es válida
  
resultado = calcular(f1, f2, "+") # llama a la función con la operación de suma
print(resultado)
