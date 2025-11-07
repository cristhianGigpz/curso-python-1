x = 5
y = 0

# print(x > y)
# print(x < y)

# Operador AND
print((x > y) and (y < x))  # True and True
print((x > y) and (y > x))  # True and False

# Operador OR
print((x > y) or (y > x))   # True or False
print((x < y) or (y > x))   # False or False

# negación
print(not(5 > 3))  # not True -> False
print(not(3 > 5))  # not False -> True

# condicionales

if x > y:
    print("x es mayor que y")
elif x == y:
    print("x es igual a y")   
else:
    print("y es mayor que x")

if x > y or x == y:
    print("x es mayor o igual que y")

dia = 8
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Día no válido")