"""✅ 1. Suma de los primeros 10 números
Enunciado:
Escribe un programa que use un bucle for para sumar los números del 1 al 10 y mostrar el resultado final."""


for i in range (0,11):
    print(i)  

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
for numero in numbers:
    suma += numero 
print(f"La suma total es ",suma) 
