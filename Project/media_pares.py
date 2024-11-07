# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantos elementos vai ter o vetor? "))

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input("Digite um numero: "))

soma, par = 0, 0
for i in range(0, n):
    if vet[i] % 2 == 0:
        soma += vet[i]
        par += 1

if par == 0:
    print("NENHUM NUMERO PAR")
else:
    med = soma / par
    print(f"MEDIA DOS PARES = {med:.1f}")