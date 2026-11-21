cantidad = int(input("Cantidad de bates: "))

if cantidad >= 10:
    precio = 100
else:
    precio = 108

total = cantidad * precio

print(f"Total a pagar: {total} pesos")