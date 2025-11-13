def mi_funcion():
    return "¡Hola desde mi_funcion!"

print(mi_funcion())

# funcion con parametros
# def saludar(nombre):
#     return f"¡Hola, {nombre}!"

# print(saludar("Carlos"))

# funcion con parametros y valor por defecto
def saludar_con_saludo(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar_con_saludo("Ana"))
print(saludar_con_saludo("Cristhian", saludo="Buenos días"))

def sumar(a, b):
    return a + b    

la_suma = sumar(3, 5)
print("La suma es:", la_suma)

# funcion lambda
multiplicar = lambda x, y: x * y
resultado = multiplicar(4, 6)
print("El resultado de la multiplicación es:", resultado)

# fabrica de funciones
def fabrica_de_potencias(exponente):        
    return lambda base: base ** exponente

elevar_al_cubo = fabrica_de_potencias(3)
elevar_al_cuadrado = fabrica_de_potencias(2)
print("5 elevado al cubo es:", elevar_al_cubo(5))
print("4 elevado al cuadrado es:", elevar_al_cuadrado(4))