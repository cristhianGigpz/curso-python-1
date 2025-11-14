from pedidos import hacer_pedido
from historial_pedidos import mostrar_historial_pedidos 
def main():
    while True:
        print("\n--------------------------")
        print("Bienvenido a nuestro Restaurante")
        print("1. Ver menú")
        print("2. Ver pedidos")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            hacer_pedido()
        elif opcion == '2':
            mostrar_historial_pedidos()
        elif opcion == '3':
            print("Saliendo del programa. ¡Gracias por visitarnos!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

if __name__ == "__main__":
    main()