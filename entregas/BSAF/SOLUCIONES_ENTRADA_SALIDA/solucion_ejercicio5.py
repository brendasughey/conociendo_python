from pathlib import Path

ruta = Path("../../../01_entrada_salida/datos/salida.txt")
texto = input("Escribe el texto: ")

ruta.parent.mkdir(parents=True, exist_ok=True)
ruta.write_text(texto, encoding="utf-8")
print("Guardado.")