"""Enunciado:
Haz un programa que muestre las tablas de multiplicar del 1 al 5. Cada tabla debe ir del 1 al 10."""
for tabla in range(1, 6):
    print(f"Tabla de multiplicar del {tabla}:")
    for i in range(1, 11):
        resultado = tabla * i
        print(f"{tabla} x {i} = {resultado}")
