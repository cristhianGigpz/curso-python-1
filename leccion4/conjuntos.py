"""
Lección 4: Conjuntos (Sets)
Este script demuestra el uso de conjuntos en Python
"""

# Crear conjuntos
print("=== Crear Conjuntos ===")
conjunto_vacio = set()
numeros = {1, 2, 3, 4, 5}
frutas = {"manzana", "banana", "naranja"}
desde_lista = set([1, 2, 2, 3, 3, 3, 4])  # elimina duplicados

print(f"Conjunto vacío: {conjunto_vacio}")
print(f"Números: {numeros}")
print(f"Frutas: {frutas}")
print(f"Desde lista (sin duplicados): {desde_lista}")

# Características de los sets
print("\n=== Características ===")
print("1. No permiten elementos duplicados")
print("2. No están ordenados")
print("3. Los elementos deben ser inmutables")

# Agregar elementos
print("\n=== Agregar Elementos ===")
colores = {"rojo", "verde", "azul"}
print(f"Conjunto original: {colores}")

colores.add("amarillo")
print(f"Después de add('amarillo'): {colores}")

colores.update(["naranja", "violeta"])
print(f"Después de update(['naranja', 'violeta']): {colores}")

# Eliminar elementos
print("\n=== Eliminar Elementos ===")
print(f"Conjunto: {colores}")

colores.remove("rojo")
print(f"Después de remove('rojo'): {colores}")

colores.discard("verde")  # no da error si no existe
print(f"Después de discard('verde'): {colores}")

elemento = colores.pop()  # elimina elemento aleatorio
print(f"Elemento eliminado con pop(): {elemento}")
print(f"Conjunto actual: {colores}")

# Operaciones de conjuntos
print("\n=== Operaciones de Conjuntos ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Unión
union = set1.union(set2)
print(f"\nUnión (|): {union}")
print(f"O también: {set1 | set2}")

# Intersección
interseccion = set1.intersection(set2)
print(f"\nIntersección (&): {interseccion}")
print(f"O también: {set1 & set2}")

# Diferencia
diferencia = set1.difference(set2)
print(f"\nDiferencia set1 - set2 (-): {diferencia}")
print(f"O también: {set1 - set2}")

diferencia2 = set2.difference(set1)
print(f"Diferencia set2 - set1 (-): {diferencia2}")

# Diferencia simétrica
diferencia_simetrica = set1.symmetric_difference(set2)
print(f"\nDiferencia simétrica (^): {diferencia_simetrica}")
print(f"O también: {set1 ^ set2}")

# Relaciones entre conjuntos
print("\n=== Relaciones entre Conjuntos ===")
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {6, 7, 8}

print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")

# Subconjunto
print(f"\n¿A es subconjunto de B? {a.issubset(b)}")
print(f"¿B es subconjunto de A? {b.issubset(a)}")

# Superconjunto
print(f"\n¿B es superconjunto de A? {b.issuperset(a)}")
print(f"¿A es superconjunto de B? {a.issuperset(b)}")

# Disjuntos (sin elementos comunes)
print(f"\n¿A y C son disjuntos? {a.isdisjoint(c)}")
print(f"¿A y B son disjuntos? {a.isdisjoint(b)}")

# Verificar pertenencia
print("\n=== Verificar Pertenencia ===")
frutas = {"manzana", "banana", "naranja"}
print(f"Frutas: {frutas}")
print(f"¿Está 'banana'? {'banana' in frutas}")
print(f"¿Está 'pera'? {'pera' in frutas}")

# Iterar sobre conjuntos
print("\n=== Iterar sobre Conjuntos ===")
print("Elementos del conjunto:")
for fruta in frutas:
    print(f"  - {fruta}")

# Longitud
print(f"\nNúmero de elementos: {len(frutas)}")

# Limpiar conjunto
print("\n=== Limpiar Conjunto ===")
numeros = {1, 2, 3, 4, 5}
print(f"Antes: {numeros}")
numeros.clear()
print(f"Después de clear(): {numeros}")

# Conjuntos inmutables (frozenset)
print("\n=== Frozenset (Conjunto Inmutable) ===")
conjunto_inmutable = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {conjunto_inmutable}")
print("No se puede modificar (no tiene add, remove, etc.)")

# Set comprehension
print("\n=== Set Comprehension ===")
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
print(f"Lista con duplicados: {numeros}")

unicos = {x for x in numeros}
print(f"Set de únicos: {unicos}")

cuadrados = {x**2 for x in range(1, 6)}
print(f"Cuadrados del 1 al 5: {cuadrados}")

# Aplicación práctica: eliminar duplicados
print("\n=== Aplicación: Eliminar Duplicados ===")
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(f"Lista original: {lista_con_duplicados}")

lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista sin duplicados: {lista_sin_duplicados}")

# Aplicación práctica: comparar listas
print("\n=== Aplicación: Comparar Listas ===")
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comunes = list(set(lista1) & set(lista2))
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Elementos comunes: {comunes}")

solo_en_lista1 = list(set(lista1) - set(lista2))
print(f"Solo en lista 1: {solo_en_lista1}")

todos = list(set(lista1) | set(lista2))
print(f"Todos los elementos: {todos}")
