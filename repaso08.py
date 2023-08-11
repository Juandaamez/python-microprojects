#Juan David Amezquita Nuñez
# 8. Convertir decimal a binario.

decimal = int(input("Ingresa un número decimal: "))
binario = '{:b}'.format(decimal)
print(f"El número {decimal} es {binario} en binario")

