"""Enunciado:
Crea un sistema que pida al usuario una contraseña. 
Si no la acierta, podrá intentarlo hasta 3 veces. Si falla, muestra un mensaje de acceso bloqueado."""

contrasena_correcta = "secreto123"
intentos_maximos = 3
intentos_realizados = 0

while intentos_realizados < intentos_maximos:
    contrasena_ingresada = input("Introduce la contraseña: ")
    intentos_realizados += 1

    if contrasena_ingresada == contrasena_correcta:
        print("¡Acceso concedido!")
        break
    elif intentos_realizados < intentos_maximos:
        print(f"Contraseña incorrecta. Te quedan {intentos_maximos - intentos_realizados} intentos.")
    else:
        print("Acceso bloqueado. Has superado el número máximo de intentos.")