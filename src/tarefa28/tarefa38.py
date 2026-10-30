print("Dime tu nombre")
nombre = input()

print("Dime tu edad")
edad = int(input())

print("Dime tu dirección")
direccion = input()

print("Dime tu tel")
tel = input()

datos = {
    "nombre" : nombre,
    "edad" : edad,
    "direccion" : direccion,
    "tel" : tel
}

print(f"{nombre} ten {edad} anos, vive en {direccion} e o seu número de teléfono é {tel}.")