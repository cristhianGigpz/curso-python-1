"""
Lección 4: Listas
Este script demuestra el uso de listas en Python
"""

# Crear listas
print("=== Crear Listas ===")
lista_vacia = []
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "naranja"]
mixta = [1, "dos", 3.0, True, [5, 6]]

print(f"Lista vacía: {lista_vacia}")
print(f"Números: {numeros}")
print(f"Frutas: {frutas}")
print(f"Mixta: {mixta}")

# Acceder a elementos
print("\n=== Acceder a Elementos ===")
print(f"Primera fruta: {frutas[0]}")
print(f"Segunda fruta: {frutas[1]}")
print(f"Última fruta: {frutas[-1]}")
print(f"Penúltima fruta: {frutas[-2]}")

# Slicing (rebanado)
print("\n=== Slicing ===")
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista completa: {numeros}")
print(f"Primeros 3: {numeros[:3]}")
print(f"Últimos 3: {numeros[-3:]}")
print(f"Del 2 al 5: {numeros[2:6]}")
print(f"Cada 2 elementos: {numeros[::2]}")
print(f"Lista invertida: {numeros[::-1]}")

# Modificar listas
print("\n=== Modificar Listas ===")
frutas = ["manzana", "banana", "naranja"]
print(f"Lista original: {frutas}")

frutas[1] = "uva"
print(f"Después de cambiar índice 1: {frutas}")

# Métodos de listas
print("\n=== Métodos de Listas ===")
numeros = [1, 2, 3]
print(f"Lista original: {numeros}")

# append - agregar al final
numeros.append(4)
print(f"Después de append(4): {numeros}")

# insert - insertar en posición
numeros.insert(0, 0)
print(f"Después de insert(0, 0): {numeros}")

# extend - agregar múltiples elementos
numeros.extend([5, 6, 7])
print(f"Después de extend([5, 6, 7]): {numeros}")

# remove - eliminar elemento
numeros.remove(3)
print(f"Después de remove(3): {numeros}")

# pop - eliminar y retornar
elemento = numeros.pop()
print(f"Elemento eliminado con pop(): {elemento}")
print(f"Lista después de pop(): {numeros}")

elemento = numeros.pop(0)
print(f"Elemento eliminado con pop(0): {elemento}")
print(f"Lista después de pop(0): {numeros}")

# Ordenar y buscar
print("\n=== Ordenar y Buscar ===")
numeros = [5, 2, 8, 1, 9, 3]
print(f"Lista original: {numeros}")

numeros.sort()
print(f"Después de sort(): {numeros}")

numeros.sort(reverse=True)
print(f"Después de sort(reverse=True): {numeros}")

# sorted - crear nueva lista ordenada
original = [5, 2, 8, 1, 9, 3]
ordenada = sorted(original)
print(f"\nOriginal: {original}")
print(f"Ordenada (nueva lista): {ordenada}")

# Buscar elementos
print("\n=== Buscar Elementos ===")
frutas = ["manzana", "banana", "naranja", "uva"]
print(f"Lista: {frutas}")
print(f"Índice de 'naranja': {frutas.index('naranja')}")
print(f"¿Está 'banana'? {'banana' in frutas}")
print(f"¿Está 'pera'? {'pera' in frutas}")
print(f"Cuenta de 'manzana': {frutas.count('manzana')}")

# Operaciones con listas
print("\n=== Operaciones con Listas ===")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Concatenación: {lista1 + lista2}")
print(f"Repetición: {lista1 * 3}")
print(f"Longitud de lista1: {len(lista1)}")
print(f"Máximo de lista2: {max(lista2)}")
print(f"Mínimo de lista1: {min(lista1)}")
print(f"Suma de lista1: {sum(lista1)}")

# List comprehension
print("\n=== List Comprehension ===")
numeros = [1, 2, 3, 4, 5]
print(f"Números originales: {numeros}")

cuadrados = [x**2 for x in numeros]
print(f"Cuadrados: {cuadrados}")

pares = [x for x in numeros if x % 2 == 0]
print(f"Números pares: {pares}")

# Listas anidadas
print("\n=== Listas Anidadas ===")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz:")
for fila in matriz:
    print(f"  {fila}")

print(f"\nElemento en [1][2]: {matriz[1][2]}")

# Copiar listas
print("\n=== Copiar Listas ===")
original = [1, 2, 3]
copia_shallow = original  # referencia
copia_real = original.copy()  # copia real
copia_slice = original[:]  # copia con slicing

print(f"Original: {original}")
print(f"Copia shallow: {copia_shallow}")
print(f"Copia real: {copia_real}")

original[0] = 999
print(f"\nDespués de modificar original[0] = 999:")
print(f"Original: {original}")
print(f"Copia shallow: {copia_shallow}")
print(f"Copia real: {copia_real}")
