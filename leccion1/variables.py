"""
Lección 1: Variables y Tipos de Datos
Este script demuestra cómo usar variables y diferentes tipos de datos en Python
"""

# Variables numéricas
edad = 25
altura = 1.75
temperatura = -5

print("=== Variables Numéricas ===")
print(f"Edad: {edad} (tipo: {type(edad)})")
print(f"Altura: {altura} (tipo: {type(altura)})")
print(f"Temperatura: {temperatura} (tipo: {type(temperatura)})")

# Variables de texto (strings)
nombre = "Juan"
apellido = 'Pérez'
mensaje = """Este es un
mensaje de
varias líneas"""

print("\n=== Variables de Texto ===")
print(f"Nombre completo: {nombre} {apellido}")
print(f"Tipo: {type(nombre)}")
print(f"Mensaje:\n{mensaje}")

# Variables booleanas
es_estudiante = True
tiene_trabajo = False

print("\n=== Variables Booleanas ===")
print(f"¿Es estudiante? {es_estudiante}")
print(f"¿Tiene trabajo? {tiene_trabajo}")
print(f"Tipo: {type(es_estudiante)}")

# Conversión de tipos
numero_texto = "42"
numero_entero = int(numero_texto)
numero_decimal = float(numero_texto)

print("\n=== Conversión de Tipos ===")
print(f"Texto: '{numero_texto}' -> Entero: {numero_entero} -> Decimal: {numero_decimal}")

# Múltiples asignaciones
x, y, z = 10, 20, 30
print(f"\n=== Múltiples Asignaciones ===")
print(f"x = {x}, y = {y}, z = {z}")

# Constantes (por convención se escriben en mayúsculas)
PI = 3.14159
GRAVEDAD = 9.8

print(f"\n=== Constantes ===")
print(f"PI = {PI}")
print(f"GRAVEDAD = {GRAVEDAD}")
