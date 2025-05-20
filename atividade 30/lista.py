nomes_alunos = []
num_alunos = int(input("Digite o número de alunos: "))

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno{i + 1}: ")
    nomes_alunos.append(nome)

print("\nNomescdos alunos registrado")
for nome in nomes_alunos:
    print(nome)