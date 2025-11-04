"""
Lección 2: Condicionales
Este script demuestra el uso de estructuras condicionales en Python
"""

# Condicional simple (if)
print("=== Condicional Simple (if) ===")
edad = 18

if edad >= 18:
    print(f"Tienes {edad} años, eres mayor de edad")

# Condicional if-else
print("\n=== Condicional if-else ===")
temperatura = 25

if temperatura > 30:
    print(f"Hace calor ({temperatura}°C)")
else:
    print(f"Temperatura agradable ({temperatura}°C)")

# Condicional if-elif-else
print("\n=== Condicional if-elif-else ===")
nota = 85

if nota >= 90:
    print(f"Excelente! Nota: {nota}")
elif nota >= 80:
    print(f"Muy bien! Nota: {nota}")
elif nota >= 70:
    print(f"Bien. Nota: {nota}")
elif nota >= 60:
    print(f"Aprobado. Nota: {nota}")
else:
    print(f"Reprobado. Nota: {nota}")

# Condicionales anidados
print("\n=== Condicionales Anidados ===")
edad = 20
tiene_licencia = True

if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("Eres mayor de edad pero necesitas licencia")
else:
    print("Eres menor de edad, no puedes conducir")

# Operador ternario
print("\n=== Operador Ternario ===")
edad = 15
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(f"Edad: {edad} - {mensaje}")

# Múltiples condiciones
print("\n=== Múltiples Condiciones ===")
hora = 14
dia = "lunes"

if hora >= 9 and hora <= 18 and dia != "domingo":
    print("La tienda está abierta")
else:
    print("La tienda está cerrada")

# Verificar pertenencia
print("\n=== Verificar Pertenencia (in) ===")
frutas = ["manzana", "banana", "naranja"]
fruta_buscar = "banana"

if fruta_buscar in frutas:
    print(f"{fruta_buscar} está en la lista")
else:
    print(f"{fruta_buscar} no está en la lista")

# Verificar valores None
print("\n=== Verificar None ===")
valor = None

if valor is None:
    print("El valor es None (nulo)")
else:
    print(f"El valor es: {valor}")

# Comparación de strings
print("\n=== Comparación de Strings ===")
password = "python123"
password_ingresada = "python123"

if password == password_ingresada:
    print("Contraseña correcta!")
else:
    print("Contraseña incorrecta")
