#5

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

maior = max(numeros)
impares = [n for n in numeros if n % 2 != 0]
menor_impar = min(impares) if impares else None

soma = sum(numeros)
media = soma / len(numeros)

print("\nResultados:")
print("Maior número:", maior)
if menor_impar is not None:
    print("Menor número ímpar:", menor_impar)
else:
    print("Nenhum número ímpar na lista.")
print("Somatório dos números:", soma)
print("Média dos números:", media)