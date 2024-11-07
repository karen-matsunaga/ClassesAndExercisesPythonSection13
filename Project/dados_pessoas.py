# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantas pessoas serao digitadas? "))

altura: [float] = [0 for x in range(n)]
genero: [str] = [0 for x in range(n)]

for i in range(0, n):
    altura[i] = float(input(f"Altura da {i+1}a pessoa: "))
    genero[i] = input(f"Genero da {i+1}a pessoa: ")

menor, maior = altura[i], altura[i]
soma = 0
for i in range(0, n):
    if menor > altura[i]:
        menor = altura[i]
    elif maior < altura[i]:
        maior = altura[i]

print(f"Menor altura = {menor:.2f}")
print(f"Maior altura = {maior:.2f}")

sm, m = 0, 0
for i in range(0, n):
    if genero[i] == 'F':
        sm += altura[i]
        m += 1

med = sm / m
print(f"Media das alturas das mulheres = {med:.2f}")

h = n - m
print(f"Numero de homens = {h}")