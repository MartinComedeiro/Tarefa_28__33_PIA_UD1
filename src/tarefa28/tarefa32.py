materias = ["Matemáticas", "Física", "Química", "Historia", "Lingua"]

materiaNotas = dict()

for materia in materias:
    print(f"Que sacaches en {materia}?")
    materiaNotas[materia] = int(input())

for materia in materiaNotas.keys():
    print(f"En {materia} saquei un {materiaNotas[materia]}")