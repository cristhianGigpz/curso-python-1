# conjuntos (set): colección no ordenada de elementos únicos
conjunto_frutas = {"manzana", "banana", "cereza", "durazno"}
print("Conjunto original de frutas:", conjunto_frutas)
print(type(conjunto_frutas))
print("Número de frutas en el conjunto:", len(conjunto_frutas))

for fruta in conjunto_frutas:
    print("Fruta:", fruta)


print("¿'banana' está en el conjunto?", "banana" in conjunto_frutas)

conjunto_frutas.add("uva")
print("Conjunto de frutas después de agregar 'uva':", conjunto_frutas)

conjunto_frutas.update(["kiwi", "mango", "uva"])
print("Conjunto de frutas después de actualizar con 'kiwi' y 'mango':", conjunto_frutas)

# conjunto_frutas.remove("papa")
# print("Conjunto de frutas después de eliminar 'cereza':", conjunto_frutas)

conjunto_frutas.discard("naranja")  # No genera error si el elemento no existe
print("Conjunto de frutas después de intentar eliminar 'naranja':", conjunto_frutas)

conjunto_frutas.pop()  # Elimina un elemento arbitrario
print("Conjunto de frutas después de usar pop():", conjunto_frutas)

conjunto_frutas.clear()
print("Conjunto de frutas después de usar clear():", conjunto_frutas)

print("--- Operaciones con conjuntos ---")
conjunto_a = {"a", "b", "c", "d"}
conjunto_b = {"c", "d", "e", "f"}

union = conjunto_a.union(conjunto_b)
print("Unión de conjunto_a y conjunto_b:", union)

interseccion = conjunto_a.intersection(conjunto_b)
print("Intersección de conjunto_a y conjunto_b:", interseccion)

diferencia = conjunto_a.difference(conjunto_b)
print("Diferencia de conjunto_a y conjunto_b (elementos en A no en B):", diferencia)

