import notas_ponderada


print("Programa para calcular as notas de um aluno")
print()

nota1 = float(input("Informe a 1ª nota: "))
nota2 = float(input("Informe a 2ª nota: "))
nota3 = float(input("Informe a 3ª nota: "))

resultado = notas_ponderada.calcular(nota1, nota2, nota3)

print()
print(f"O resultado é {resultado:.2f}") 