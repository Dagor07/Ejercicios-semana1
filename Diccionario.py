"""Parte 1: Básicos
Crea un diccionario llamado auto que contenga:

Marca
Modelo
Año
Cambia el modelo del auto a otro diferente.
Agrega una nueva clave color al diccionario.
Elimina la clave año.
Imprime todas las claves del diccionario usando un bucle for.
Imprime todos los valores del diccionario usando un bucle for."""

cars = {
    "Mark" : "Mazda",
    "Model": "Mazda 3",
    "Year" : "2024"
}
cars ["color"] =  "Rojo"

del cars["Year"]
for key, value in cars.items():
    print({key})
    print({value})

"""Parte 2: Intermedio
Crea un diccionario paises donde las claves sean nombres de países y los valores sus capitales.
Escribe un programa que pregunte al usuario un país y devuelva su capital (si existe).

Invierte el diccionario paises, es decir, que las capitales sean las claves y los países los valores.

Crea un diccionario de estudiantes donde las claves sean los nombres y los valores sus notas finales.
Después imprime los nombres de los estudiantes que aprobaron (nota mayor o igual a 6)"""

paises = {
    "México": "Ciudad de México",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín",
    "Colombia" : "Bogotá"
}


pais = input("Ingresa el nombre de un país: ")
capital = paises.get(pais, "El país no está en el diccionario.")
print(f"La capital de {pais} es: {capital}")


invertidas = {capital: pais for pais, capital in paises.items()}
print("\nDiccionario invertido")
print(invertidas)


estudiantes = {
    "Juan": 8,
    "María": 5,
    "Pedro": 6,
    "Ana": 9,
    "Luis": 4
}

print("\nEstudiantes que aprobaron:")
for nombre, nota in estudiantes.items():
    if nota >= 6:
        print(nombre)