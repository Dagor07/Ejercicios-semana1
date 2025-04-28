
while True:
    print("\n--- Menú ---")
    print("1. Opción Uno")
    print("2. Opción Dos")
    print("3. Opción Tres")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")
    opcion1 = opcion.lower()
    match opcion1:
        case "1" | "uno" | "primera":
            print("Phones")
            while True:
                print("Opción 1")
                print("Opción 2")
                opcion2 = input("Elige una opción (1-2): ")
                match opcion2:
                    case "1" | "uno" | "primer":
                        print ("Comprar")
                        break
                    case "2" | "dos":
                        print ("Vender")
                        break
                    case _:
                        print("Opción inválida. Por favor, elige una opción válida.")
        case "2" | "dos" | "segunda":
            print("Computer")
        case "3" | "tres" | "tercera":
            print("appliances")
        case "4" | "cuatro" | "cuarta":
            print("¡Fin del programa!")
            break
        case _:
            print("Opción inválida. Por favor, elige una opción válida.")