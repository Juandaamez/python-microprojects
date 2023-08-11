#Juan David Amezquita Nuñez
# 4.Conversión de Temperaturas: Crear un programa que permita al usuario convertir entre grados Celsius y grados Fahrenheit.

opcion = input("¿Qué quieres convertir? (c)elsius o (f)ahrenheit: ")

temperatura = float(input("Ingresa la temperatura: "))

def celsius_a_fahrenheit(c):
  return c * 9/5 + 32

def fahrenheit_a_celsius(f):
  return (f - 32) * 5/9

if opcion == "c":
  resultado = celsius_a_fahrenheit(temperatura)
  print(f"{temperatura} grados Celsius son {resultado} grados Fahrenheit")
elif opcion == "f":
  resultado = fahrenheit_a_celsius(temperatura)
  print(f"{temperatura} grados Fahrenheit son {resultado} grados Celsius")
else:
  print("Opción inválida")