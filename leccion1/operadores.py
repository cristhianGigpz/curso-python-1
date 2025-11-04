"""
Lección 1: Operadores
Este script demuestra el uso de diferentes operadores en Python
"""

# Operadores aritméticos
print("=== Operadores Aritméticos ===")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Suma: a + b = {a + b}")
print(f"Resta: a - b = {a - b}")
print(f"Multiplicación: a * b = {a * b}")
print(f"División: a / b = {a / b}")
print(f"División entera: a // b = {a // b}")
print(f"Módulo: a % b = {a % b}")
print(f"Potencia: a ** b = {a ** b}")

# Operadores de comparación
print("\n=== Operadores de Comparación ===")
x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Operadores lógicos
print("\n=== Operadores Lógicos ===")
es_mayor_edad = True
tiene_licencia = False

print(f"es_mayor_edad = {es_mayor_edad}, tiene_licencia = {tiene_licencia}")
print(f"es_mayor_edad AND tiene_licencia: {es_mayor_edad and tiene_licencia}")
print(f"es_mayor_edad OR tiene_licencia: {es_mayor_edad or tiene_licencia}")
print(f"NOT es_mayor_edad: {not es_mayor_edad}")

# Operadores de asignación
print("\n=== Operadores de Asignación ===")
numero = 10
print(f"numero inicial: {numero}")

numero += 5  # numero = numero + 5
print(f"numero += 5: {numero}")

numero -= 3  # numero = numero - 3
print(f"numero -= 3: {numero}")

numero *= 2  # numero = numero * 2
print(f"numero *= 2: {numero}")

numero //= 4  # numero = numero // 4
print(f"numero //= 4: {numero}")

# Operadores de cadenas
print("\n=== Operadores con Cadenas ===")
saludo = "Hola"
nombre = "Mundo"

print(f"Concatenación: '{saludo}' + ' ' + '{nombre}' = '{saludo + ' ' + nombre}'")
print(f"Repetición: '{saludo}' * 3 = '{saludo * 3}'")

# Entrada y salida
print("\n=== Entrada y Salida ===")
print("Ejemplo de input() (comentado para ejecución automática):")
print("# nombre_usuario = input('¿Cómo te llamas? ')")
print("# print(f'¡Hola, {nombre_usuario}!')")
