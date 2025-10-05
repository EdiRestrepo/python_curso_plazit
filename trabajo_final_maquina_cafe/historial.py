ARCHIVO_PEDIDOS = "pedidos.txt"

def ver_historial():
    try:
        print("\n Cargando historial de pedidos...")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                print("\n ---Historial de Pedidos---")
                for i, pedido in enumerate(pedidos, start=1):
                    print(str(i) + ". " + pedido.strip())
            else:
                print("\n No hay pedidos en el historial.")
    except FileNotFoundError:
        print("\n No hay pedidos en el historial.")