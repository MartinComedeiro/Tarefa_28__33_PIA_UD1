print("Dime tu cantidad")
cantidad = int(input())
print(" ")

print("Dime tu porcentaje de IVE (enter para 21%)")
ive = input()
print("")

def IVE(cantidad, ive = 21):
    return cantidad *((100-ive)*0.01)

if ive == "":
    resultado = IVE(cantidad)
else:
    resultado = IVE(cantidad, int(ive))


print(f"La cantidad des pués del IVE es: {resultado}")


