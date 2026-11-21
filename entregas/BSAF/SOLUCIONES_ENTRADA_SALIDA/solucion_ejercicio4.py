from pathlib import Path

ruta = Path("../../../01_entrada_salida/datos/ejemplo.txt")

try:
    print(ruta.read_text(encoding="utf-8"))
except FileNotFoundError:
    print(f"No se encontró '{ruta}'.")