from pathlib import Path

ruta = Path("../../../01_entrada_salida/datos/numero.txt")

try:
    numero = int(ruta.read_text(encoding="utf-8").strip())
    print(numero)
except FileNotFoundError:
    print(f"No se encontró '{ruta}'.")
except ValueError:
    print("El contenido del archivo no es un número entero válido.")