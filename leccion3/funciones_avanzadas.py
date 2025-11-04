"""
Lección 3: Funciones Avanzadas
Este script demuestra conceptos avanzados de funciones en Python
"""

# Args - número variable de argumentos posicionales
def sumar_todos(*args):
    """Suma todos los argumentos recibidos"""
    return sum(args)

print("=== *args - Argumentos Variables ===")
print(f"Suma de 1, 2, 3: {sumar_todos(1, 2, 3)}")
print(f"Suma de 1, 2, 3, 4, 5: {sumar_todos(1, 2, 3, 4, 5)}")
print(f"Suma de 10, 20: {sumar_todos(10, 20)}")

# Kwargs - número variable de argumentos con nombre
def mostrar_info(**kwargs):
    """Muestra información recibida como argumentos nombrados"""
    print("Información recibida:")
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

print("\n=== **kwargs - Argumentos con Nombre Variables ===")
mostrar_info(nombre="Ana", edad=25, ciudad="Madrid")
mostrar_info(producto="Laptop", precio=800, marca="Dell")

# Combinación de args y kwargs
def funcion_completa(arg1, arg2, *args, **kwargs):
    """Función que combina diferentes tipos de argumentos"""
    print(f"Arg1: {arg1}")
    print(f"Arg2: {arg2}")
    print(f"Args adicionales: {args}")
    print(f"Kwargs adicionales: {kwargs}")

print("\n=== Combinación de Argumentos ===")
funcion_completa(1, 2, 3, 4, 5, nombre="Python", version=3.9)

# Scope de variables
variable_global = "Soy global"

def ejemplo_scope():
    """Demuestra el scope de variables"""
    variable_local = "Soy local"
    print(f"Dentro de la función:")
    print(f"  Variable local: {variable_local}")
    print(f"  Variable global: {variable_global}")

print("\n=== Scope de Variables ===")
ejemplo_scope()
print(f"Fuera de la función:")
print(f"  Variable global: {variable_global}")
# print(f"  Variable local: {variable_local}")  # Esto daría error

# Modificar variable global
contador = 0

def incrementar():
    """Incrementa el contador global"""
    global contador
    contador += 1
    return contador

print("\n=== Modificar Variable Global ===")
print(f"Contador inicial: {contador}")
print(f"Después de incrementar: {incrementar()}")
print(f"Después de incrementar: {incrementar()}")
print(f"Después de incrementar: {incrementar()}")

# Función dentro de función
def funcion_externa(x):
    """Función que contiene otra función"""
    def funcion_interna(y):
        """Función interna"""
        return y * 2
    
    return funcion_interna(x) + 5

print("\n=== Función dentro de Función ===")
print(f"Resultado: {funcion_externa(10)}")  # (10 * 2) + 5 = 25

# Closures
def crear_multiplicador(factor):
    """Crea una función que multiplica por un factor"""
    def multiplicar(numero):
        return numero * factor
    return multiplicar

print("\n=== Closures ===")
multiplicar_por_2 = crear_multiplicador(2)
multiplicar_por_5 = crear_multiplicador(5)

print(f"5 multiplicado por 2: {multiplicar_por_2(5)}")
print(f"5 multiplicado por 5: {multiplicar_por_5(5)}")

# Decoradores simples
def mi_decorador(func):
    """Decorador simple"""
    def wrapper():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return wrapper

@mi_decorador
def saludar():
    """Función decorada"""
    print("¡Hola desde la función!")

print("\n=== Decoradores ===")
saludar()

# Función como parámetro
def aplicar_operacion(func, valores):
    """Aplica una función a una lista de valores"""
    return [func(valor) for valor in valores]

print("\n=== Función como Parámetro ===")
numeros = [1, 2, 3, 4, 5]
cuadrados = aplicar_operacion(lambda x: x**2, numeros)
print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")

# Map, filter, reduce
from functools import reduce

print("\n=== Map, Filter, Reduce ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map - aplica función a cada elemento
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Cuadrados con map: {cuadrados}")

# Filter - filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares con filter: {pares}")

# Reduce - reduce a un solo valor
suma = reduce(lambda x, y: x + y, numeros)
print(f"Suma con reduce: {suma}")
