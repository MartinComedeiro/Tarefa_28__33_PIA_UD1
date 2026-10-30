frutas = {
    "Plátano" : 1.35,
    "Mazá" : 0.8,
    "Pera" : 0.85,
    "Laranxa" : 0.7
}

print("Dime una fruta")
fruta = input()

print("Dime kilos")
kilos = int(input())

if frutas.get(fruta):
    print(f"{fruta} {kilos}Kg son {kilos*frutas[fruta]}")
else:
    print(f"No existe esa fruta")
