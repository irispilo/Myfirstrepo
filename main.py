from zodiac import list_signs, get_zodiac_sign
from messages import get_random_message

def main():
    current_sign = None

    while True:
        print("\nBienvenido al Programa del Zodiaco")
        print("1. Listar Signos del Zodiaco")
        print("2. Obtener Signo según Cumpleaños")
        print("3. Obtener Mensaje del Signo")
        print("4. Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            list_signs()

        elif choice == "2":
            try:
                month = int(input("Ingresa tu mes de nacimiento (1-12): "))
                day = int(input("Ingresa tu día de nacimiento (1-31): "))
                sign = get_zodiac_sign(month, day)
                if sign:
                    print(f"Tu signo del zodiaco es: {sign}")
                    current_sign = sign
                else:
                    print("Fecha inválida para un signo del zodiaco.")
            except ValueError:
                print("Por favor ingresa números válidos para mes y día.")

        elif choice == "3":
            if current_sign:
                message = get_random_message(current_sign)
                print(f"Mensaje aleatorio para {current_sign}: \"{message}\"")
            else:
                print("Primero debes obtener tu signo (opción 2).")

        elif choice == "4":
            print("¡Gracias por usar el programa! Hasta luego.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
