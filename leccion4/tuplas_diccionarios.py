"""
Lección 4: Tuplas y Diccionarios
Este script demuestra el uso de tuplas y diccionarios en Python
"""

# TUPLAS
print("=" * 50)
print("TUPLAS")
print("=" * 50)

# Crear tuplas
print("\n=== Crear Tuplas ===")
tupla_vacia = ()
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mixta = (1, "dos", 3.0, True)
tupla_un_elemento = (42,)  # nota la coma

print(f"Tupla vacía: {tupla_vacia}")
print(f"Tupla de números: {tupla_numeros}")
print(f"Tupla mixta: {tupla_mixta}")
print(f"Tupla de un elemento: {tupla_un_elemento}")

# Acceder a elementos
print("\n=== Acceder a Elementos de Tuplas ===")
coordenadas = (10, 20, 30)
print(f"Coordenadas: {coordenadas}")
print(f"x: {coordenadas[0]}")
print(f"y: {coordenadas[1]}")
print(f"z: {coordenadas[2]}")

# Desempaquetado
print("\n=== Desempaquetado de Tuplas ===")
x, y, z = coordenadas
print(f"x = {x}, y = {y}, z = {z}")

# Tuplas son inmutables
print("\n=== Las Tuplas son Inmutables ===")
print("Las tuplas no se pueden modificar después de crearlas")
# tupla_numeros[0] = 999  # Esto daría error

# Operaciones con tuplas
print("\n=== Operaciones con Tuplas ===")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(f"Tupla 1: {tupla1}")
print(f"Tupla 2: {tupla2}")
print(f"Concatenación: {tupla1 + tupla2}")
print(f"Repetición: {tupla1 * 2}")
print(f"Longitud: {len(tupla1)}")

# Tuplas anidadas
print("\n=== Tuplas Anidadas ===")
persona = ("Ana", 25, ("Madrid", "España"))
nombre, edad, ubicacion = persona
ciudad, pais = ubicacion
print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}, País: {pais}")

# DICCIONARIOS
print("\n" + "=" * 50)
print("DICCIONARIOS")
print("=" * 50)

# Crear diccionarios
print("\n=== Crear Diccionarios ===")
diccionario_vacio = {}
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid",
    "profesion": "Ingeniera"
}
print(f"Persona: {persona}")

# Acceder a elementos
print("\n=== Acceder a Elementos ===")
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Profesion: {persona.get('profesion')}")
print(f"País (no existe): {persona.get('pais', 'No especificado')}")

# Modificar y agregar elementos
print("\n=== Modificar y Agregar ===")
print(f"Diccionario original: {persona}")

persona["edad"] = 26  # modificar
print(f"Después de modificar edad: {persona}")

persona["email"] = "ana@email.com"  # agregar
print(f"Después de agregar email: {persona}")

# Eliminar elementos
print("\n=== Eliminar Elementos ===")
del persona["email"]
print(f"Después de del email: {persona}")

profesion = persona.pop("profesion")
print(f"Profesión eliminada: {profesion}")
print(f"Diccionario actual: {persona}")

# Métodos de diccionarios
print("\n=== Métodos de Diccionarios ===")
producto = {
    "nombre": "Laptop",
    "precio": 800,
    "marca": "Dell",
    "stock": 15
}

print(f"Diccionario: {producto}")
print(f"Claves: {list(producto.keys())}")
print(f"Valores: {list(producto.values())}")
print(f"Items: {list(producto.items())}")

# Iterar sobre diccionarios
print("\n=== Iterar sobre Diccionarios ===")
print("Iterando sobre items:")
for clave, valor in producto.items():
    print(f"  {clave}: {valor}")

print("\nIterando sobre claves:")
for clave in producto.keys():
    print(f"  {clave}")

print("\nIterando sobre valores:")
for valor in producto.values():
    print(f"  {valor}")

# Verificar existencia
print("\n=== Verificar Existencia ===")
print(f"¿Existe 'precio'? {'precio' in producto}")
print(f"¿Existe 'color'? {'color' in producto}")

# Actualizar diccionarios
print("\n=== Actualizar Diccionarios ===")
nuevos_datos = {"color": "negro", "peso": "2kg"}
print(f"Antes: {producto}")
producto.update(nuevos_datos)
print(f"Después de update: {producto}")

# Diccionarios anidados
print("\n=== Diccionarios Anidados ===")
empresa = {
    "nombre": "TechCorp",
    "empleados": {
        "gerente": {"nombre": "Ana", "edad": 35},
        "desarrollador": {"nombre": "Carlos", "edad": 28},
        "diseñador": {"nombre": "María", "edad": 26}
    }
}

print(f"Nombre del gerente: {empresa['empleados']['gerente']['nombre']}")
print(f"Edad del desarrollador: {empresa['empleados']['desarrollador']['edad']}")

# Dictionary comprehension
print("\n=== Dictionary Comprehension ===")
numeros = [1, 2, 3, 4, 5]
cuadrados_dict = {x: x**2 for x in numeros}
print(f"Números y sus cuadrados: {cuadrados_dict}")

# Copiar diccionarios
print("\n=== Copiar Diccionarios ===")
original = {"a": 1, "b": 2}
copia = original.copy()
print(f"Original: {original}")
print(f"Copia: {copia}")

original["c"] = 3
print(f"\nDespués de modificar original:")
print(f"Original: {original}")
print(f"Copia: {copia}")
