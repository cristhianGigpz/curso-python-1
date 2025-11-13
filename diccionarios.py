auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "colores_disponibles": ["Rojo", "Azul", "Blanco"],
    "es_electrico": False
}

# print("Diccionario original del auto:", auto)
# print(type(auto))
# print("Número de elementos en el diccionario:", len(auto))

# acceder a elementos
print("Marca del auto:", auto["marca"])
print("Modelo del auto:", auto.get("modelo"))

# print(auto.keys())
# print(auto.values())

# for clave in auto:
#     print(f"{clave}: {auto[clave]}")

if "marca" in auto:
    print("La clave 'marca' está en el diccionario")

# modificar elementos
auto["año"] = 2025
print(auto)

# agregar elementos
auto["precio"] = 25000
print(auto)

auto.update({"color_interior": "Negro", "transmision": "Automática"})
print(auto)

# eliminar elementos
del auto["color_interior"]
print(auto)

auto.pop("transmision")
print(auto)

auto.popitem()  # elimina el último elemento agregado
print(auto)

# limpiar el diccionario
# auto.clear()
# print("Diccionario después de clear():", auto)

# for k in auto.keys():
#     print("Clave:", k) 

# for v in auto.values():
#     print("Valor:", v)


for clave, valor in auto.items():
    print(f"{clave}: {valor}")


alumnos = {
    101: {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería"},
    102: {"nombre": "Luis", "edad": 22, "carrera": "Medicina"},
    103: {"nombre": "Marta", "edad": 21, "carrera": "Derecho"}
}

#print(alumnos)
print("Datos del alumno con ID 102:", alumnos[102])
print("Nombre del alumno con ID 103:", alumnos[103]["nombre"])
