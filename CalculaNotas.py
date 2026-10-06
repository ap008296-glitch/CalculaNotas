print("Programa para calcular as notas de um aluno")
print()

nota1 = float(input("Informe a 1ª nota: "))
nota2 = float(input("Informe a 2ª nota: "))
nota3 = float(input("Informe a 3ª nota: "))

resultado = (nota1 * 2) + (nota2 * 3) + (nota3 * 5) / 10

print()
print(f"O resultado é {resultado:.2f}")