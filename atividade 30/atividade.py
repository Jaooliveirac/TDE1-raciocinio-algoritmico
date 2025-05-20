# Lista para armazenar os nomes dos alunos
nomes_alunos = []

# Loop para ler o nome de 3 alunos 
for i in range(3):
    nome = input(f"Digite o nome do aluno{i + 1}:")
    nomes_alunos.append(nome)

# Exibindo os nomes registrados 
print("\nNomes dos alunos registrados:")
for nome in nomes_alunos:
    print("\nSegundo nome da lista:",nomes_alunos[1])