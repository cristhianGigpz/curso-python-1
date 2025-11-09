frutas = ["manzana", "banana", "cereza", "durazno"]
print("Lista original de frutas:", frutas)
print(type(frutas))

# indices
print("Primera fruta:", frutas[0])
print("Segunda fruta:", frutas[1])
print("Tercera fruta:", frutas[2])

frutas[1] = "naranja"
print("Lista de frutas después de la modificación:", frutas)

# agregar elementos
frutas.append("uva")
print("Lista de frutas después de agregar un elemento:", frutas)

frutas.insert(2, "kiwi")
print(frutas)

len_frutas = len(frutas)
print("Número de frutas en la lista:", len_frutas)

print(frutas[0:3])  # desde el índice 0 hasta el 2
print(frutas[1:])   # desde el índice 1 hasta el final
print(frutas[:3])   # desde el inicio hasta el índice 2

# eliminar elementos
frutas.remove("cereza")
print("Lista de frutas después de eliminar 'cereza':", frutas)
del frutas[0]
print("Lista de frutas después de eliminar el primer elemento:", frutas)

fruta_eliminada = frutas.pop()
print("Fruta eliminada usando pop():", fruta_eliminada)
print("Lista de frutas después de usar pop():", frutas)

# ordernar
mi_lista_numeros = [5, 2, 9, 1, 5, 6]
mi_lista_numeros.sort()
print("Lista de números ordenada:", mi_lista_numeros)

mi_lista_numeros.reverse()
print("Lista de números en orden inverso:", mi_lista_numeros)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_combinada = lista1 + lista2
print("Lista combinada:", lista_combinada)

lista1.extend(lista2)
print("Lista1 después de usar extend():", lista1)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Elemento en la fila 1, columna 2 de la matriz:", matriz[0][1])   