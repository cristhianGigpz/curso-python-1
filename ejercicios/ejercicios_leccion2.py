"""
Ejercicios - Lección 2: Estructuras de Control

Intenta resolver estos ejercicios por tu cuenta antes de ver las soluciones.
"""

# =============================================================================
# EJERCICIO 1: Clasificador de Números
# =============================================================================
# Crea un programa que:
# 1. Verifique si un número es positivo, negativo o cero
# 2. Determine si es par o impar (solo si no es cero)
# 3. Determine si es múltiplo de 5
# =============================================================================

print("=== EJERCICIO 1: Clasificador de Números ===")
print("\nEjemplo de solución:")

def clasificar_numero(numero):
    """Clasifica un número"""
    print(f"\nAnalizando el número: {numero}")
    
    # Positivo, negativo o cero
    if numero > 0:
        print("  - Es positivo")
    elif numero < 0:
        print("  - Es negativo")
    else:
        print("  - Es cero")
    
    # Par o impar
    if numero != 0:
        if numero % 2 == 0:
            print("  - Es par")
        else:
            print("  - Es impar")
    
    # Múltiplo de 5
    if numero % 5 == 0:
        print("  - Es múltiplo de 5")

clasificar_numero(15)
clasificar_numero(-8)
clasificar_numero(0)

# =============================================================================
# EJERCICIO 2: Tabla de Multiplicar
# =============================================================================
# Crea un programa que:
# 1. Genere la tabla de multiplicar de un número del 1 al 10
# 2. Muestre el resultado de forma ordenada
# =============================================================================

print("\n\n=== EJERCICIO 2: Tabla de Multiplicar ===")
print("\nEjemplo de solución:")

def tabla_multiplicar(numero):
    """Genera la tabla de multiplicar"""
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"  {numero} x {i:2d} = {resultado:3d}")

tabla_multiplicar(7)

# =============================================================================
# EJERCICIO 3: Suma de Números Pares
# =============================================================================
# Crea un programa que:
# 1. Sume todos los números pares del 1 al 100
# 2. Muestre cuántos números pares hay
# 3. Muestre el promedio de los números pares
# =============================================================================

print("\n\n=== EJERCICIO 3: Suma de Números Pares ===")
print("\nEjemplo de solución:")

suma = 0
contador = 0

for i in range(1, 101):
    if i % 2 == 0:
        suma += i
        contador += 1

promedio = suma / contador if contador > 0 else 0

print(f"\nNúmeros pares del 1 al 100:")
print(f"  Cantidad: {contador}")
print(f"  Suma total: {suma}")
print(f"  Promedio: {promedio:.2f}")

# =============================================================================
# EJERCICIO 4: Factorial
# =============================================================================
# Crea un programa que calcule el factorial de un número
# Factorial de n = n! = n * (n-1) * (n-2) * ... * 1
# Ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
# =============================================================================

print("\n\n=== EJERCICIO 4: Factorial ===")
print("\nEjemplo de solución:")

def calcular_factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        return "No existe factorial de números negativos"
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

for numero in [0, 1, 5, 10]:
    resultado = calcular_factorial(numero)
    print(f"Factorial de {numero}: {resultado}")

# =============================================================================
# EJERCICIO 5: Números Primos
# =============================================================================
# Crea un programa que:
# 1. Determine si un número es primo
# 2. Muestre todos los números primos del 1 al 50
# =============================================================================

print("\n\n=== EJERCICIO 5: Números Primos ===")
print("\nEjemplo de solución:")

def es_primo(numero):
    """Verifica si un número es primo"""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Mostrar números primos del 1 al 50
print("\nNúmeros primos del 1 al 50:")
primos = []
for i in range(1, 51):
    if es_primo(i):
        primos.append(i)

print(primos)
print(f"\nTotal de números primos: {len(primos)}")

# =============================================================================
# EJERCICIO 6: Patrón de Asteriscos
# =============================================================================
# Crea un programa que dibuje un patrón triangular con asteriscos
# =============================================================================

print("\n\n=== EJERCICIO 6: Patrón de Asteriscos ===")
print("\nEjemplo de solución:")

altura = 5

print("\nTriángulo ascendente:")
for i in range(1, altura + 1):
    print("*" * i)

print("\nTriángulo descendente:")
for i in range(altura, 0, -1):
    print("*" * i)

print("\nPirámide:")
for i in range(1, altura + 1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)

# =============================================================================
# EJERCICIO 7: Contador de Vocales
# =============================================================================
# Crea un programa que cuente cuántas vocales hay en un texto
# =============================================================================

print("\n\n=== EJERCICIO 7: Contador de Vocales ===")
print("\nEjemplo de solución:")

def contar_vocales(texto):
    """Cuenta las vocales en un texto"""
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador = 0
    vocales_encontradas = {}
    
    for caracter in texto:
        if caracter in vocales:
            contador += 1
            vocal = caracter.lower()
            vocales_encontradas[vocal] = vocales_encontradas.get(vocal, 0) + 1
    
    return contador, vocales_encontradas

texto = "Hola, este es un curso de Python"
total, detalle = contar_vocales(texto)

print(f"\nTexto: '{texto}'")
print(f"Total de vocales: {total}")
print(f"Detalle: {detalle}")

print("\n" + "="*50)
print("¡Intenta resolver estos ejercicios por tu cuenta!")
print("Experimenta con diferentes valores y casos")
print("="*50)
