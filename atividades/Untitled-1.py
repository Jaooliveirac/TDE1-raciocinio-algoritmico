n1 = float(input("digite Nota 1: "))
n2 = float(input("digite Nota 2: "))
media = (n1 + n2) / 2

if media >= 7.0:
    print("Aprovado")
elif media >= 5.0:
    print("Recuperação")
else:
    print("Reprovado")  
