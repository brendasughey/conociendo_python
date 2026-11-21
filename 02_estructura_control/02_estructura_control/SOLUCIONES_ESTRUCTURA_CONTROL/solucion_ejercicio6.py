cantidad = int(input("Cantidad de balones: "))

if cantidad > 15:
    precio = 85
elif cantidad > 10:
    precio = 92
else:
    precio = 99

total = cantidad * precio

print(f"Total a pagar: {total} pesos")