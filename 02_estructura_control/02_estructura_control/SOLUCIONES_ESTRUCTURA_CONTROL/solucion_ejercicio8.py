cantidad = int(input("Bates comprados: "))

if cantidad <= 10:
    total = cantidad * 250
else:
    total = (10 * 250) + ((cantidad - 10) * 230)

print(f"Bates comprados: {cantidad}")
print(f"Costo total: {total} pesos")