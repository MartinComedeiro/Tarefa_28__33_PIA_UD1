print("Dime tu cantidad de payasos")
payasos = int(input())
print(" ")

print("Dime tu cantidad de muñecas")
munecas = int(input())
print(" ")

def calcularPeso(payasos, munecas):
    return (payasos*0.112) + (munecas*0.075)


print(f"El peso del pedido es: {calcularPeso(payasos, munecas)}Kg")
