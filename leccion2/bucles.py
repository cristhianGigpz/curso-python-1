"""
Lección 2: Bucles
Este script demuestra el uso de bucles for y while en Python
"""

# Bucle for con range
print("=== Bucle for con range ===")
print("Números del 0 al 4:")
for i in range(5):
    print(i, end=" ")
print()

print("\nNúmeros del 1 al 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

print("\nNúmeros pares del 0 al 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# Bucle for con listas
print("\n\n=== Bucle for con Listas ===")
frutas = ["manzana", "banana", "naranja", "uva"]
print("Frutas:")
for fruta in frutas:
    print(f"  - {fruta}")

# Bucle for con strings
print("\n=== Bucle for con Strings ===")
palabra = "Python"
print(f"Letras en '{palabra}':")
for letra in palabra:
    print(letra, end=" ")
print()

# Bucle for con enumerate
print("\n\n=== Bucle for con enumerate ===")
colores = ["rojo", "verde", "azul"]
print("Lista de colores con índice:")
for indice, color in enumerate(colores):
    print(f"  {indice}: {color}")

# Bucle while
print("\n=== Bucle while ===")
contador = 1
print("Contando del 1 al 5:")
while contador <= 5:
    print(contador, end=" ")
    contador += 1
print()

# Bucle while con condición
print("\n=== Bucle while con condición ===")
suma = 0
numero = 1
while suma < 50:
    suma += numero
    numero += 1
print(f"La suma llegó a {suma} con {numero-1} números")

# Break - salir del bucle
print("\n=== Uso de break ===")
print("Buscando el número 7:")
for i in range(1, 11):
    print(f"Número: {i}")
    if i == 7:
        print("¡Encontrado!")
        break

# Continue - saltar a la siguiente iteración
print("\n=== Uso de continue ===")
print("Números impares del 1 al 10:")
for i in range(1, 11):
    if i % 2 == 0:  # si es par
        continue  # saltar a la siguiente iteración
    print(i, end=" ")
print()

# Bucles anidados
print("\n\n=== Bucles Anidados ===")
print("Tabla de multiplicar (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j:2d}", end="  ")
    print()

# List comprehension (forma compacta)
print("\n=== List Comprehension ===")
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados del 1 al 5: {cuadrados}")

pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares del 1 al 10: {pares}")

# Bucle con else
print("\n=== Bucle con else ===")
print("Buscando número mayor a 10:")
for i in range(1, 6):
    print(f"  Revisando: {i}")
    if i > 10:
        print("  ¡Encontrado!")
        break
else:
    print("  No se encontró ningún número mayor a 10")
