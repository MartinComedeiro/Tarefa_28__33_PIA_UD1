monedas = {
    "Euro" : "€",
    "Dollar" : "$",
    "Yen" : "Y"
}

print("Divisa?")
divisa = input()

divisaValida = False

for moneda in monedas.keys():
    if divisa == moneda:
        divisaValida = True
    

if divisaValida:
    print(monedas[divisa])
else:
        print("No trabajamos con esa divisa")