"""Enunciado:
Escribe un programa que pida al usuario adivinar un número secreto entre 1 y 10. El juego se repite hasta que adivine correctamente."""
import random

def juego_adivina_el_numero():
    print("¡Bienvenido al juego de adivinar el número!")
    numero_secreto = random.randint(1, 10)  

    while True:
        try:
            adivinanza = int(input("Adivina el número secreto (entre 1 y 10): "))
            
            if adivinanza < 1 or adivinanza > 10:
                print("Por favor, introduce un número entre 1 y 10.")
                continue

            match adivinanza:
                case _ if adivinanza == numero_secreto:
                    print("¡Felicidades! Adivinaste el número secreto.")
                    break
                case _ if adivinanza < numero_secreto:
                    print("El número secreto es mayor. ¡Intenta de nuevo!")
                case _ if adivinanza > numero_secreto:
                    print("El número secreto es menor. ¡Intenta de nuevo!")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")

