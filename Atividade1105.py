#1
import os

loop = True
alunos = {}
menu = 0

def media_aluno(lista):
    media = 0
    for i in lista:
        media = media + i
    media = media/3
    return media

while loop:

    menu = int(input("Oque deseja fazer:\n" \
    " 01 - Cadastrar aluno\n" \
    " 02 - Alunos aprovados\n" \
    " 03 - Buscar alunos\n" \
    " 04 - Sair"))
    match menu:
        case 1:
            nome = input("Bota o nome do aluno ae: ")
            notas = []
            for i in range(3):
                nota = int(input(f"Coloca a nota {i+1}: "))
                notas.append(nota)
    
            alunos[nome] = notas
        case 2:
            for nome, notas in alunos.items():
                if (media_aluno(notas)) >= 7:
                    print(f"Aluno {nome} passou!")
            os.system('pause')
                

        case 3:
            busca = input("Insira o nome do aluno: ")
            for nome, notas in alunos.items():
                if nome.lower() == busca.lower():
                    if (media_aluno(notas)) >= 7:
                        situ = "Aprovado"
                    elif (media_aluno(notas)) >= 4:
                        situ = "Recuperação"
                    else:
                        situ = "Reprovado"
                    print(f"O aluno {nome} que possui {media_aluno(notas):.2f} e está {situ}")
            os.system('pause')
        case 4:
            loop = False
            
    os.system('cls')
   
#2

loop = True
produtos = {}
menu = 0

while loop:

    menu = int(input("Escolha uma opção:\n" \
    " 01 - Cadastrar produto\n" \
    " 02 - Consultar produto\n" \
    " 03 - Comprar produto\n" \
    " 04 - Sair"))
    match menu:
        case 1:
            nome = input("Nome do produto: ").lower()
            quant = int(input("Insira a quantidade: "))

            produtos[nome] = quant
        case 2:
            busca = input("Insira o nome do produto: ")
            for nome, quant in produtos.items():
                if nome.lower() == busca.lower():
                    print(f"O produto {nome} tem {quant} unidades disponíveis")
            os.system('pause')         
        case 3:
            nome_compra = input("Digite o nome do produto que deseja comprar: ").lower()
            quant_compra = int(input("Insira a quantidade do produto que deseja comprar: "))
            produtos[nome] = quant - quant_compra
            if  produtos[nome] < 0:
                produtos[nome] = 0
        case 4:
            loop = False

    os.system('cls')

#3
frase = input("Digite uma frase: ").lower()
frequencia = {}

for char in frase:
    if char != " ":
        if char in frequencia:
            frequencia[char] += 1
        else:
            frequencia[char] = 1

print("Frequencia de carcteres:", frequencia)

#4

candidatos = {"Sergio": 0,"Fabricio":0,"Marcos":0}

while True:
    print("Escolha um candidato para votar:")
    for nome in candidatos:
        print(nome)

    voto = input("")
    if voto == "fim":
        break
    candidatos[voto] += 1
    os.system('cls')

print(f"O vencedor é o candidato: {max(candidatos, key=candidatos.get)}")

#5
contatos = {}

while True:
    menu = int(input("escolha uma opção:\n" \
    " 01 - Cadastrar contato\n" \
    " 02 - Buscar contato\n" \
    " 03 - Excluir contato\n" \
    " 04 - Sair e listar contatos"))
    match menu:
        case 1:
            nome = input("Nome do contato: ").lower()
            num = int(input("Insira o numero de telefone: "))

            contatos[nome] = num
        case 2:
            busca = input("Insira o nome do contato: ")
            for nome, num in contatos.items():
                if nome.lower() == busca.lower():
                    print(f"Nome: {nome.capitalize()}\nNumero: {num}")
            os.system('pause')   
        case 3:
            excluir = input("Qual contato deseja excluir: ").lower()
            contatos.pop(excluir, None)
            print(f"O contato {excluir.capitalize()} foi excluido!")
            os.system('pause') 
        case 4:
            for nome, num in contatos.items():
                print(f"Nome: {nome.capitalize()}\nNumero: {num}\n")
            break
    os.system('cls')
    


