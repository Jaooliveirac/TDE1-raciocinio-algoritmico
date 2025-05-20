#4
nota = []
qnt_alunos = int(input("Informe a quantidade de alunos: "))
aprovados = 0
reprovados = 0

for i in range(qnt_alunos):
    nota_alunos = int(input(f"Informe a nota dos alunos{i + 1}: "))
    nota.append(nota_alunos)
print("\nAs notas foram: ")
for nota_alunos in nota:
    print(nota_alunos)


if nota_alunos >= 60:
    aprovados += 1 
else:
    reprovados += 1

    print("ALunos aprovados", aprovados,)
    print("alunos reprovados", reprovados,)
