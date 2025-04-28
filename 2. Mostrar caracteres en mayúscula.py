"""Enunciado:
Crea un programa que recorra una palabra carácter por carácter y muestre cada letra en mayúscula en una nueva línea."""


while True:
    palabra = input("Ingresa la palabra:")
    if  palabra.isalpha():
       break
    if not palabra.isalpha():
        print("Ingrese dato valido") 


for i in palabra:   
    print (i.upper())
