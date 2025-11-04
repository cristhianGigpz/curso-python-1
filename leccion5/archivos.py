"""
Lección 5: Manejo de Archivos
Este script demuestra cómo trabajar con archivos en Python
"""

import os

# Crear directorio para ejemplos si no existe
if not os.path.exists("archivos_ejemplo"):
    os.makedirs("archivos_ejemplo")

# Escribir en un archivo
print("=== Escribir en un Archivo ===")
ruta_archivo = "archivos_ejemplo/ejemplo1.txt"

with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
    archivo.write("Hola, este es un archivo de ejemplo.\n")
    archivo.write("Esta es la segunda línea.\n")
    archivo.write("Y esta es la tercera línea.\n")

print(f"Archivo '{ruta_archivo}' creado exitosamente")

# Leer todo el archivo
print("\n=== Leer Todo el Archivo ===")
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print("Contenido completo:")
    print(contenido)

# Leer línea por línea
print("=== Leer Línea por Línea ===")
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    print("Leyendo línea por línea:")
    linea_numero = 1
    for linea in archivo:
        print(f"Línea {linea_numero}: {linea.strip()}")
        linea_numero += 1

# Leer con readline
print("\n=== Leer con readline() ===")
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    primera_linea = archivo.readline()
    segunda_linea = archivo.readline()
    print(f"Primera línea: {primera_linea.strip()}")
    print(f"Segunda línea: {segunda_linea.strip()}")

# Leer con readlines
print("\n=== Leer con readlines() ===")
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()
    print(f"Total de líneas: {len(lineas)}")
    for i, linea in enumerate(lineas, 1):
        print(f"  {i}. {linea.strip()}")

# Agregar contenido (append)
print("\n=== Agregar Contenido (append) ===")
with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
    archivo.write("Esta línea fue agregada posteriormente.\n")
    archivo.write("Y esta también.\n")

print("Contenido agregado. Archivo actualizado:")
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    print(archivo.read())

# Escribir múltiples líneas con writelines
print("=== Escribir con writelines() ===")
ruta_archivo2 = "archivos_ejemplo/ejemplo2.txt"
lineas = [
    "Primera línea\n",
    "Segunda línea\n",
    "Tercera línea\n",
    "Cuarta línea\n"
]

with open(ruta_archivo2, 'w', encoding='utf-8') as archivo:
    archivo.writelines(lineas)

print(f"Archivo '{ruta_archivo2}' creado con writelines()")

# Trabajar con archivos CSV
print("\n=== Crear Archivo CSV ===")
ruta_csv = "archivos_ejemplo/datos.csv"

with open(ruta_csv, 'w', encoding='utf-8') as archivo:
    archivo.write("nombre,edad,ciudad\n")
    archivo.write("Ana,25,Madrid\n")
    archivo.write("Carlos,30,Barcelona\n")
    archivo.write("María,28,Valencia\n")

print(f"Archivo CSV '{ruta_csv}' creado")

# Leer archivo CSV
print("\n=== Leer Archivo CSV ===")
with open(ruta_csv, 'r', encoding='utf-8') as archivo:
    encabezados = archivo.readline().strip().split(',')
    print(f"Encabezados: {encabezados}")
    print("\nDatos:")
    for linea in archivo:
        datos = linea.strip().split(',')
        print(f"  {encabezados[0]}: {datos[0]}, {encabezados[1]}: {datos[1]}, {encabezados[2]}: {datos[2]}")

# Verificar si existe un archivo
print("\n=== Verificar Existencia de Archivos ===")
archivos_a_verificar = [ruta_archivo, "archivo_inexistente.txt"]

for archivo in archivos_a_verificar:
    if os.path.exists(archivo):
        print(f"✓ '{archivo}' existe")
    else:
        print(f"✗ '{archivo}' no existe")

# Información del archivo
print("\n=== Información del Archivo ===")
if os.path.exists(ruta_archivo):
    tamaño = os.path.getsize(ruta_archivo)
    print(f"Tamaño de '{ruta_archivo}': {tamaño} bytes")

# Trabajar con rutas
print("\n=== Trabajar con Rutas ===")
print(f"Ruta actual: {os.getcwd()}")
print(f"Nombre del archivo: {os.path.basename(ruta_archivo)}")
print(f"Directorio: {os.path.dirname(ruta_archivo)}")
print(f"Ruta absoluta: {os.path.abspath(ruta_archivo)}")

# Listar archivos en directorio
print("\n=== Listar Archivos en Directorio ===")
print("Archivos en 'archivos_ejemplo':")
for archivo in os.listdir("archivos_ejemplo"):
    ruta_completa = os.path.join("archivos_ejemplo", archivo)
    if os.path.isfile(ruta_completa):
        print(f"  - {archivo}")

# Copiar contenido de un archivo a otro
print("\n=== Copiar Archivo ===")
ruta_origen = ruta_archivo
ruta_destino = "archivos_ejemplo/copia.txt"

with open(ruta_origen, 'r', encoding='utf-8') as origen:
    with open(ruta_destino, 'w', encoding='utf-8') as destino:
        contenido = origen.read()
        destino.write(contenido)

print(f"Archivo copiado de '{ruta_origen}' a '{ruta_destino}'")

# Leer archivo binario (ejemplo con texto)
print("\n=== Modo Binario ===")
ruta_binario = "archivos_ejemplo/binario.txt"

# Escribir en modo binario
with open(ruta_binario, 'wb') as archivo:
    archivo.write(b"Contenido en modo binario\n")
    archivo.write(b"Segunda linea\n")

# Leer en modo binario
with open(ruta_binario, 'rb') as archivo:
    contenido_binario = archivo.read()
    print(f"Contenido binario: {contenido_binario}")
    print(f"Decodificado: {contenido_binario.decode('utf-8')}")

print("\n=== Archivos de ejemplo creados ===")
print("Revisa la carpeta 'archivos_ejemplo' para ver los archivos creados")
