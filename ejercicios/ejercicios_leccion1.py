"""
Ejercicios - Lección 1: Variables y Operadores

Intenta resolver estos ejercicios por tu cuenta antes de ver las soluciones.
"""

# =============================================================================
# EJERCICIO 1: Calculadora Básica
# =============================================================================
# Crea un programa que:
# 1. Pida al usuario dos números
# 2. Muestre la suma, resta, multiplicación y división de esos números
# 3. Muestre también el resultado de la división entera y el módulo
# =============================================================================

print("=== EJERCICIO 1: Calculadora Básica ===")
print("\nEjemplo de solución:")

num1 = 20
num2 = 6

print(f"\nNúmero 1: {num1}")
print(f"Número 2: {num2}")
print(f"\nSuma: {num1} + {num2} = {num1 + num2}")
print(f"Resta: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")
print(f"División: {num1} / {num2} = {num1 / num2:.2f}")
print(f"División entera: {num1} // {num2} = {num1 // num2}")
print(f"Módulo: {num1} % {num2} = {num1 % num2}")

# =============================================================================
# EJERCICIO 2: Conversión de Temperaturas
# =============================================================================
# Crea un programa que:
# 1. Convierta una temperatura de Celsius a Fahrenheit
# 2. Convierta una temperatura de Fahrenheit a Celsius
# Fórmulas:
#   F = (C * 9/5) + 32
#   C = (F - 32) * 5/9
# =============================================================================

print("\n\n=== EJERCICIO 2: Conversión de Temperaturas ===")
print("\nEjemplo de solución:")

celsius = 25
fahrenheit = 77

fahrenheit_convertido = (celsius * 9/5) + 32
celsius_convertido = (fahrenheit - 32) * 5/9

print(f"\n{celsius}°C = {fahrenheit_convertido}°F")
print(f"{fahrenheit}°F = {celsius_convertido:.2f}°C")

# =============================================================================
# EJERCICIO 3: Información Personal
# =============================================================================
# Crea un programa que:
# 1. Almacene información personal (nombre, edad, ciudad, altura)
# 2. Calcule el año de nacimiento aproximado
# 3. Muestre toda la información de forma ordenada
# =============================================================================

print("\n\n=== EJERCICIO 3: Información Personal ===")
print("\nEjemplo de solución:")

nombre = "Ana García"
edad = 25
ciudad = "Madrid"
altura = 1.65  # en metros
año_actual = 2025

año_nacimiento = año_actual - edad

print(f"\n--- Información Personal ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Año de nacimiento aproximado: {año_nacimiento}")
print(f"Ciudad: {ciudad}")
print(f"Altura: {altura} m ({int(altura * 100)} cm)")

# =============================================================================
# EJERCICIO 4: Área y Perímetro
# =============================================================================
# Crea un programa que calcule el área y perímetro de:
# 1. Un rectángulo (base = 5, altura = 3)
# 2. Un círculo (radio = 4)
# Fórmulas:
#   Rectángulo: área = base * altura, perímetro = 2 * (base + altura)
#   Círculo: área = π * r², perímetro = 2 * π * r
# =============================================================================

print("\n\n=== EJERCICIO 4: Área y Perímetro ===")
print("\nEjemplo de solución:")

PI = 3.14159

# Rectángulo
base = 5
altura = 3
area_rectangulo = base * altura
perimetro_rectangulo = 2 * (base + altura)

print(f"\nRectángulo (base={base}, altura={altura}):")
print(f"  Área: {area_rectangulo}")
print(f"  Perímetro: {perimetro_rectangulo}")

# Círculo
radio = 4
area_circulo = PI * radio ** 2
perimetro_circulo = 2 * PI * radio

print(f"\nCírculo (radio={radio}):")
print(f"  Área: {area_circulo:.2f}")
print(f"  Perímetro: {perimetro_circulo:.2f}")

# =============================================================================
# EJERCICIO 5: Operaciones con Strings
# =============================================================================
# Crea un programa que:
# 1. Combine nombre y apellido
# 2. Muestre el nombre completo en mayúsculas y minúsculas
# 3. Cuente cuántos caracteres tiene el nombre completo
# 4. Muestre las iniciales
# =============================================================================

print("\n\n=== EJERCICIO 5: Operaciones con Strings ===")
print("\nEjemplo de solución:")

nombre = "Juan"
apellido = "Pérez"

nombre_completo = nombre + " " + apellido
iniciales = nombre[0] + apellido[0]

print(f"\nNombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Nombre completo: {nombre_completo}")
print(f"En mayúsculas: {nombre_completo.upper()}")
print(f"En minúsculas: {nombre_completo.lower()}")
print(f"Número de caracteres: {len(nombre_completo)}")
print(f"Iniciales: {iniciales}")

print("\n" + "="*50)
print("¡Intenta resolver estos ejercicios por tu cuenta!")
print("Modifica los valores y experimenta con el código")
print("="*50)
