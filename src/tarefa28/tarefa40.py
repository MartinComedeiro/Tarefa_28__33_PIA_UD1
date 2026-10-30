print(f"Artículo y precio (espacio para salir)")

articulos = {}

while True:
    articulo,precio = input(),input()

    if articulo == " " or precio == " ":
        break

    precio = int(precio)

    articulos[articulo] = precio
    print("Añadido")

suma = 0
print("Lista de la compra")
for articulo in articulos.keys():
    print(f"{articulo}: {articulos[articulo]}")
    suma += articulos[articulo]

print(f"Total   {suma}")