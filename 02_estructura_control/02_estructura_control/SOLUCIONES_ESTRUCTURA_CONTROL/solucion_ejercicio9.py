horas = float(input("Horas trabajadas: "))

if horas <= 40:
    salario = horas * 50
else:
    horas_extra = horas - 40
    salario = (40 * 50) + (horas_extra * 70)

print(f"Salario: {salario}")234