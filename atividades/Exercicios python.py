# Aprovado, reprovado ou recuperação
n1 = float(input("digite Nota 1: "))
n2 = float(input("digite Nota 2: "))
media = (n1 + n2) / 2

if media >= 7.0:
    print("Aprovado")
elif media >= 5.0:
    print("Recuperação")
else:
    print("Reprovado")  

# Número par ou ímpar
n1 = int(input("digite algum numero: "))
if n1 / 2 == 0:
    print("esse numero é par")
else:    
    print("esse numero é impar")

# Número positivo, negativo ou zero
n1 = int(input("Esse número é positivo, negativo ou zero? "))
if n1 > 0:
    print("Esse número é positivo")
elif n1 == 0:
    print("Esse número é zero")
else:
    print("Esse número é negativo")

# Letra vogal ou consoante
Letra1 = (input("Digite alguma letra: "))
if Letra1 == ("a" or "e" or "i" or "o" or "u"):
    print("Essa letra é uma vogal")
else:
    print("Essa letra é uma consante") 

#4. Triângulo
Lado1 = float(input("Digite o lado 1: "))
Lado2 = float(input("Digite o lado 2: "))
Lado3 = float(input("Digite o lado 3: "))
if Lado1 == Lado2 == Lado3:
    print("Os lados formam um triângulo equilátero")
elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
    print("Os lados formam um triângulo isósceles")
elif Lado1 != Lado2 != Lado3:
    print("Os lados formam um triângulo escaleno")

#5. Salário e tempo de serviço
Salário = float(input("Digite o salário: "))
Tempo = int(input("Digite o tempo de serviço: "))
if Tempo >= 5:
   Bonûs = Salário * 0.05
   print("O bônus é de: ", Bonûs)  
elif Tempo < 5:
    print("O bônus é de: 0")

#6. Compra e desconto
compra = float(input("Digite o valor da compra: "))
if compra >= 100:
    desconto = compra * 0.10
    print("O desconto é de: ", desconto)
elif compra < 100:
    print("O desconto é de: 0")

#7. Idade e categoria
idade = int(input("digite sua idade "))
if idade < 12 :
    print("Você é uma criança")
elif idade < 17:
    print("você é um adolescente")
elif idade < 59:
    print("Você é um adulto")
elif idade >= 60:
    print("Você é um idoso")

#8. Nota 
nota = float(input("digite sua nota: "))
if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >= 5:
    print("C")
elif nota < 5:
    print("D")

#9  salário e imposto
salário = float(input("Digite o salário: "))
if salário >= 20000:
    print("Você está isento de imposto")
elif salário <=50000:
    imposto = salário * 0.15
    print("O imposto é de: ", imposto)
elif salário > 50000:
    imposto = salário * 0.25   
    print("O imposto é de: ", imposto)

#10. idade 
idade = int(input("digite sua idade "))
if idade >= 18:
    print("Você tem permissão de obter a CNH")
elif idade < 18:
    print("Você não tem permissão de obter a CNH")

#11. temperatura celsius para fahrenheit
Celsius =  float(input("digite a temperatura em Celsius: "))
temperatura = (Celsius * 9/5) + 32
print("A temperatura em Fahrenheit é: ", temperatura)

#12. peso, altura e IMC
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * 2)
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("peso normal")
elif imc < 30: 
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade")


#13. tabuada
n1 = int(input("Digite um número: "))
for i in range(1, 11):
    n2 = n1 * i
    print("{} X {} = {}".format(n1, i, n2))
    
