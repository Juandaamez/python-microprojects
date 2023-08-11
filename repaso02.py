#Juan David Amezquita Nuñez
# 2.Factorial de un Número: Diseñar una función que calcule el factorial de un número ingresado por el usuario.
numero = int(input("Por favor ingrese un numero: "))
fact_cont = 1
cont = 0

for i in range(1, numero + 1):
    fact_cont *= i
    cont = cont + fact_cont

print(fact_cont)
