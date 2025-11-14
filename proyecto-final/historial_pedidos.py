ARCHIVO_PEDIDOS = "pedidos.txt"
def mostrar_historial_pedidos():
    try:
        with open(ARCHIVO_PEDIDOS, "r") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                print("Historial de Pedidos:")
                for pedido in pedidos:
                    print("- " + pedido.strip())
            else:
                print("No hay pedidos en el historial.")
    except FileNotFoundError:
        print("No se encontró el archivo de historial de pedidos.")
    except Exception as e:
        print("Ocurrió un error al leer el historial de pedidos:", e)