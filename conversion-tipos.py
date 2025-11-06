# lista = [1, 2, 3, 4, 5]
# tupla = (10, 20, 30)
# conjunto = {100, 200, 300}
# diccionario = {"clave1": "valor1", "clave2": "valor2"}

# print("Lista:", lista)
# print("Tupla:", tupla)
# print("Conjunto:", conjunto)
# print("Diccionario:", diccionario)

# Conversiones de tipos de datos
entero = 42
print("Entero:", entero)
decimal = 3.6
print("Decimal:", decimal)
valor = "123"
print(entero + int(valor))
print("decimal a entero:", int(decimal))

valor_flotante = float(entero)
print("Entero a decimal:", valor_flotante)

complejo = 3j
print("Número complejo:", complejo)

print("de entero a complejo:", complex(entero))
print("de decimal a complejo:", complex(decimal))

# conversiones de complejo a numero real no es posible directamente
# print("de complejo a entero:", int(complejo))  # Esto generaría un error
# print("de complejo a decimal:", float(complejo))  # Esto generaría un error

print(int(complejo.real))

