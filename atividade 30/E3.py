#3
Lista_a = []

for i in range(10):
    num_int = int(input(f"digite um número inteiro{i + 1}: "))
    Lista_a.append(num_int)

print(f"O menor número da lista é:{min (Lista_a)}")
print(f"O maior número da lista é:{max(Lista_a)}")
