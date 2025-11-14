ARCHIVO_PEDIDOS = "pedidos.txt"

def hacer_pedido():
    print("Elige uno de los platos del menú:")
    print("1. Ceviche")
    print("2. Lomo Saltado")
    print("3. Aji de Gallina")
    eleccion = input("Selecciona una opción (1-3): ")

    platos = {
        '1': 'Ceviche',
        '2': 'Lomo Saltado',
        '3': 'Aji de Gallina'
    }   

    if eleccion in platos:
        plato_seleccionado = platos[eleccion]
        try:
            with open(ARCHIVO_PEDIDOS, "a") as archivo:
                archivo.write(plato_seleccionado + "\n")
            print(f"Has pedido: {plato_seleccionado}")
        except Exception as e:
            print("Ocurrió un error al guardar el pedido:", e)