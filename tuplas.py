# coleccion ordenada e inmutable
import sys
tecnologias = ("Python", "Java", "C++", "JavaScript")
print("Tupla original de tecnologías:", tecnologias)
print(type(tecnologias))
print(len(tecnologias))

tupla = ("Hola", 42, 3.14, True)
print("Tupla mixta:", tupla)
print(len(tupla))

if "Java" in tecnologias:
    print("Java está en la tupla de tecnologías")

a, b, c, d = tecnologias
print(a)
print(b)
print(c)
print(d)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_combinada = tupla1 + tupla2
print("Tupla combinada:", tupla_combinada)

#listar elementos
print("Primer tecnología:", tecnologias[0])
print("Segunda tecnología:", tecnologias[1])

for tech in tecnologias:
    print("Tecnología:", tech)

#tecnologias[0] = "Ruby"  # Esto generará un error porque las tuplas son inmutables

# convirtir tupla a lista para modificar
lista_tecnologias = list(tecnologias)
lista_tecnologias.append("Ruby")
tupla_modificada = tuple(lista_tecnologias)
print("Lista de tecnologías modificada:", lista_tecnologias)
print("Tupla modificada:", tupla_modificada)

print("Tamaño de la tupla original en bytes:", sys.getsizeof(tecnologias))
print("Tamaño de la lista convertida en bytes:", sys.getsizeof(lista_tecnologias))


