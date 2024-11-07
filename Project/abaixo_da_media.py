# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantos elementos vai ter o vetor? "))

vet: [float] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

soma = 0
for i in range(0, n):
    soma += vet[i]

med = soma / n
print(f"\nMEDIA DO VETOR = {med:.3f}")

print("ELEMENTOS ABAIXO DA MEDIA:")
for i in range(0, n):
    if med > vet[i]:
        print(f"{vet[i]:.1f}")
