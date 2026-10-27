print("Dime un numero")
num1 = int(input())
print(" ")

print("Dime un numero")
num2 = int(input())
print(" ")

def cociente(dividendo, divisor):
    return (dividendo, divisor, dividendo/divisor, dividendo%divisor)

resultado = cociente(num1, num2)

print(f"{resultado[0]} entre {resultado[1]} da como resultado un cociente de {resultado[2]} y un resto de {resultado[3]}")