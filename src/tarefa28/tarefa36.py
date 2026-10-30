materias = ["Matemáticas", "Física", "Química", "Historia", "Lingua"]
materiasRepetir = {}
for materia in materias:
    print(f"Que nota has sacado en {materia}?")
    nota = int(input())
    materiasRepetir[materia] = nota

for materia in materias:
    if materiasRepetir[materia] >= 5:
        materiasRepetir.pop(materia)

print(materiasRepetir)

