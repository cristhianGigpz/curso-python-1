"""
Lección 3: Funciones
Este script demuestra cómo definir y usar funciones en Python
"""

# Función simple sin parámetros
def saludar():
    """Función que muestra un saludo"""
    print("¡Hola, bienvenido a Python!")

print("=== Función Simple ===")
saludar()

# Función con parámetros
def saludar_persona(nombre):
    """Función que saluda a una persona específica"""
    print(f"¡Hola, {nombre}!")

print("\n=== Función con Parámetros ===")
saludar_persona("Ana")
saludar_persona("Carlos")

# Función con múltiples parámetros
def sumar(a, b):
    """Función que suma dos números"""
    resultado = a + b
    return resultado

print("\n=== Función con Múltiples Parámetros ===")
suma = sumar(5, 3)
print(f"5 + 3 = {suma}")
print(f"10 + 20 = {sumar(10, 20)}")

# Función con parámetros por defecto
def presentarse(nombre, edad=18):
    """Función con parámetro por defecto"""
    print(f"Me llamo {nombre} y tengo {edad} años")

print("\n=== Función con Parámetros por Defecto ===")
presentarse("María")
presentarse("Juan", 25)

# Función con múltiples valores de retorno
def operaciones(a, b):
    """Función que retorna múltiples valores"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return suma, resta, multiplicacion, division

print("\n=== Función con Múltiples Retornos ===")
s, r, m, d = operaciones(10, 5)
print(f"10 y 5 -> Suma: {s}, Resta: {r}, Multiplicación: {m}, División: {d}")

# Función con parámetros nombrados
def crear_perfil(nombre, edad, ciudad="Desconocida", profesion="Estudiante"):
    """Función con parámetros nombrados"""
    return f"{nombre}, {edad} años, {ciudad}, {profesion}"

print("\n=== Función con Parámetros Nombrados ===")
print(crear_perfil("Ana", 25))
print(crear_perfil("Carlos", 30, ciudad="Madrid"))
print(crear_perfil("Luis", 28, profesion="Ingeniero", ciudad="Barcelona"))

# Función que verifica números
def es_par(numero):
    """Verifica si un número es par"""
    return numero % 2 == 0

print("\n=== Función de Verificación ===")
for i in range(1, 6):
    resultado = "par" if es_par(i) else "impar"
    print(f"{i} es {resultado}")

# Función recursiva
def factorial(n):
    """Calcula el factorial de un número"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("\n=== Función Recursiva ===")
for i in range(1, 6):
    print(f"Factorial de {i}: {factorial(i)}")

# Función lambda (función anónima)
print("\n=== Funciones Lambda ===")
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")

suma_lambda = lambda x, y: x + y
print(f"Suma con lambda (3 + 7): {suma_lambda(3, 7)}")

# Docstring - documentación de funciones
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Parámetros:
    base (float): La base del rectángulo
    altura (float): La altura del rectángulo
    
    Retorna:
    float: El área del rectángulo
    """
    return base * altura

print("\n=== Docstring ===")
print(f"Área de rectángulo (5 x 3): {area_rectangulo(5, 3)}")
print(f"\nDocumentación de la función:")
print(area_rectangulo.__doc__)
