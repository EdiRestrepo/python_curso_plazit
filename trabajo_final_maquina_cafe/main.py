from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            pedir_cafe()   
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("\n Gracias por usar la maquina de cafe")
            break
        else:
            print("Opción no valida, intenta de nuevo")

if __name__ == "__main__":
    main()