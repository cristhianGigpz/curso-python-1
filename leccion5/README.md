# Lección 5: Manejo de Archivos

## Trabajar con Archivos

Python permite leer y escribir archivos de forma sencilla.

### Modos de Apertura

- `'r'`: Lectura (read) - por defecto
- `'w'`: Escritura (write) - sobrescribe el archivo
- `'a'`: Agregar (append) - añade al final
- `'x'`: Crear - falla si el archivo existe
- `'b'`: Modo binario
- `'t'`: Modo texto - por defecto
- `'+'`: Lectura y escritura

### Sintaxis Básica

```python
# Forma tradicional
archivo = open('archivo.txt', 'r')
contenido = archivo.read()
archivo.close()

# Forma recomendada (with)
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
```

## Métodos de Lectura

- `read()`: Lee todo el archivo
- `readline()`: Lee una línea
- `readlines()`: Lee todas las líneas en una lista

## Métodos de Escritura

- `write()`: Escribe una cadena
- `writelines()`: Escribe una lista de cadenas

## Manejo de Excepciones

Es importante manejar errores al trabajar con archivos:

```python
try:
    with open('archivo.txt', 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
```

## Ejercicios

Practica con los ejemplos en `archivos.py` y `excepciones.py`
