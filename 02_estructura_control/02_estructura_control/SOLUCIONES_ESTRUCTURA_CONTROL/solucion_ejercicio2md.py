horas = 8
dias = 15
pago_hora = 50

bruto = horas * dias * pago_hora

compensacion = bruto * 0.02
imss = bruto * 0.015
ispt = bruto * 0.012

neto = bruto + compensacion - imss - ispt

print(f"Salario bruto: {bruto:.2f}")
print(f"Compensación: {compensacion:.2f}")
print(f"Descuento IMSS: {imss:.2f}")
print(f"Descuento ISPT: {ispt:.2f}")
print(f"Salario neto: {neto:.2f}")