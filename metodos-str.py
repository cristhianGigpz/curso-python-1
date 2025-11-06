texto = "Hola Mundo, ¿cómo estás? Espero que todo vaya bien."
print(texto)
#longitud del texto
print("Longitud del texto:", len(texto))
cadena = texto.find("Mundo")
print("Posición de 'Mundo':", cadena)
# mayusculas y minusculas
print("Texto en mayúsculas:", texto.upper())
print("Texto en minúsculas:", texto.lower())

# reemplazar palabras
nuevo_texto = texto.replace("Mundo", "Universo")
print(nuevo_texto)

# dividir el texto en palabras
palabras = texto.split(" ")
print(palabras)

#slicing
subcadena = texto[5:10]
subcadena2 = texto[-5:]
print("subcadena:", subcadena)
print("subcadena2:", subcadena2)

# eliminar espacios en blanco al inicio y al final
texto_espacios = "   Espacios en blanco   "
print(texto_espacios.strip())

estaIncluido = "Mundo" in texto  
print("¿'Mundo' está en el texto?", estaIncluido)
