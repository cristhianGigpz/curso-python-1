contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador += 1

i = 0
while i <= 10:
    print("El valor de i es:", i)
    if i == 5:
        print("Se encontró el número 5, saliendo del bucle.")
        break
    i = i + 1


i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print("El valor de i es:", i)


palabra = "Python es genial"
for letra in palabra:
    print("La letra actual es:", letra)


frutas = ["manzana", "banana", "cereza"]
# for fruta in frutas:
#     print("La fruta actual es:", fruta)

for fruta in frutas:
    if fruta == "banana":
        print("Se encontró la banana, saliendo del bucle.")
        break
    print("La fruta actual es:", fruta)

for fruta in frutas:
    if fruta == "banana":
        #print("Se encontró la banana, saltando a la siguiente fruta.")
        continue
    print("La fruta actual es:", fruta)


for numero in range(5):
    print("El número es:", numero)

for numero in range(1, 11):
    print("El número es:", numero)

for numero in range(0, 10, 2):
    print("El número par es:", numero)


adjetivos = ["rápido", "fuerte", "inteligente"]
for adjetivo in adjetivos:
    for fruta in frutas:
        print(f"La fruta {fruta} es {adjetivo}.")


