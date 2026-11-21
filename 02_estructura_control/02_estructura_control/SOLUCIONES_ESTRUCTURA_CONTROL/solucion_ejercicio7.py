cantidad = int(input("Cantidad de lápices: "))

if cantidad >= 100:
    precio = 0.80
elif cantidad > 50:
    precio = 1.20
elif cantidad >= 30:
    precio = 1.50
else:
    precio = 2.10

total = cantidad * precio

print(f"Total a pagar: {total} pesos")