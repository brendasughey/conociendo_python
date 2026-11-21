horas = float(input("Horas trabajadas: "))

if horas <= 40:
    salario = horas * 14.0
else:
    horas_extra = horas - 40
    salario = (40 * 14.0) + (horas_extra * 26.0)

print(f"Salario: {salario}")