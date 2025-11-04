"""
Lección 5: Manejo de Excepciones
Este script demuestra cómo manejar errores y excepciones en Python
"""

# Excepción básica
print("=== Excepción Básica ===")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")

# Múltiples excepciones
print("\n=== Múltiples Excepciones ===")
try:
    numero = int("abc")
except ValueError:
    print("Error: No se puede convertir 'abc' a número")
except TypeError:
    print("Error de tipo")

# Capturar cualquier excepción
print("\n=== Capturar Cualquier Excepción ===")
try:
    resultado = 10 / 0
except Exception as e:
    print(f"Ocurrió un error: {e}")
    print(f"Tipo de error: {type(e).__name__}")

# Try-except-else
print("\n=== Try-Except-Else ===")
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: División por cero")
else:
    print(f"Operación exitosa, resultado: {resultado}")

# Try-except-finally
print("\n=== Try-Except-Finally ===")
try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    print("Este bloque siempre se ejecuta")

# Manejo de archivos con excepciones
print("\n=== Manejo de Archivos con Excepciones ===")
nombre_archivo = "archivo_prueba.txt"

try:
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe")
    print("Creando el archivo...")
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write("Archivo creado por manejo de excepciones\n")
    print("Archivo creado exitosamente")

# Excepciones comunes
print("\n=== Excepciones Comunes ===")

# 1. ValueError
print("\n1. ValueError - Valor incorrecto")
try:
    edad = int("veinticinco")
except ValueError as e:
    print(f"   Error: {e}")

# 2. TypeError
print("\n2. TypeError - Tipo incorrecto")
try:
    resultado = "texto" + 5
except TypeError as e:
    print(f"   Error: {e}")

# 3. IndexError
print("\n3. IndexError - Índice fuera de rango")
try:
    lista = [1, 2, 3]
    elemento = lista[10]
except IndexError as e:
    print(f"   Error: {e}")

# 4. KeyError
print("\n4. KeyError - Clave no existe")
try:
    diccionario = {"nombre": "Ana"}
    edad = diccionario["edad"]
except KeyError as e:
    print(f"   Error: Clave {e} no existe")

# 5. AttributeError
print("\n5. AttributeError - Atributo no existe")
try:
    lista = [1, 2, 3]
    lista.append_all([4, 5])  # método inexistente
except AttributeError as e:
    print(f"   Error: {e}")

# 6. ZeroDivisionError
print("\n6. ZeroDivisionError - División por cero")
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"   Error: {e}")

# Lanzar excepciones (raise)
print("\n=== Lanzar Excepciones ===")

def validar_edad(edad):
    """Valida que la edad sea positiva"""
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 150:
        raise ValueError("La edad no parece válida")
    return True

try:
    validar_edad(-5)
except ValueError as e:
    print(f"Error de validación: {e}")

try:
    validar_edad(200)
except ValueError as e:
    print(f"Error de validación: {e}")

# Validación exitosa
try:
    if validar_edad(25):
        print("Edad válida: 25 años")
except ValueError as e:
    print(f"Error: {e}")

# Excepciones personalizadas
print("\n=== Excepciones Personalizadas ===")

class EdadInvalidaError(Exception):
    """Excepción personalizada para edades inválidas"""
    def __init__(self, edad, mensaje="Edad inválida"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)
    
    def __str__(self):
        return f"{self.mensaje}: {self.edad}"

def verificar_edad(edad):
    """Verifica edad con excepción personalizada"""
    if edad < 18:
        raise EdadInvalidaError(edad, "Debe ser mayor de 18 años")
    return True

try:
    verificar_edad(15)
except EdadInvalidaError as e:
    print(f"Error personalizado: {e}")

# Assert - verificación de condiciones
print("\n=== Assert - Verificaciones ===")

def dividir(a, b):
    """División con assert"""
    assert b != 0, "El divisor no puede ser cero"
    return a / b

try:
    resultado = dividir(10, 2)
    print(f"10 / 2 = {resultado}")
    
    resultado = dividir(10, 0)  # esto fallará
except AssertionError as e:
    print(f"Assertion error: {e}")

# Contexto completo de manejo de errores
print("\n=== Ejemplo Completo ===")

def leer_numero_desde_archivo(nombre_archivo):
    """Lee un número desde un archivo con manejo completo de errores"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().strip()
            numero = int(contenido)
            return numero
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe")
        return None
    except ValueError:
        print(f"Error: El contenido del archivo no es un número válido")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
    finally:
        print("Operación de lectura finalizada")

# Crear archivo de prueba
with open("numero.txt", 'w', encoding='utf-8') as f:
    f.write("42")

resultado = leer_numero_desde_archivo("numero.txt")
if resultado is not None:
    print(f"Número leído: {resultado}")

# Intentar con archivo inexistente
resultado = leer_numero_desde_archivo("no_existe.txt")

# Crear archivo con contenido inválido
with open("texto.txt", 'w', encoding='utf-8') as f:
    f.write("esto no es un número")

resultado = leer_numero_desde_archivo("texto.txt")

print("\n=== Buenas Prácticas ===")
print("1. Captura excepciones específicas, no genéricas")
print("2. Usa 'finally' para limpieza de recursos")
print("3. Usa 'with' para manejo automático de archivos")
print("4. Lanza excepciones descriptivas")
print("5. Documenta las excepciones que puede lanzar tu código")
