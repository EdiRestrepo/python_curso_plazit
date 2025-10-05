ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n Elige el cafe que deseas preparar:")
    print("1. Espresso")
    print("2. Americano")
    print("3. Capuccino")
    print("4. Latte")
    print("5. Mocha")
    print("----------------")

    opcion = input("Opción: ")

    cafes = {
        "1": "Espresso",
        "2": "Americano",
        "3": "Capuccino",
        "4": "Latte",
        "5": "Mocha"
    }

    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print(f"Has seleccionado: {cafe_elegido} estamos preparando tu café...")

        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(f"{cafe_elegido}\n")
    else:
        print("Opción no válida")