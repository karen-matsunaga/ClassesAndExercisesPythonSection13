# EXERCÍCIO CORRETO - 1/10/24
m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

mat: [[float]] = [[0 for x in range(n)] for x in range(n)]
vet: [float] = [0 for x in range(n)]

for i in range(0, m):
    print(f"Digite os elementos da {i + 1}a. linha: ")
    for j in range(0, n):
        mat[i][j] = float(input())

print("VETOR GERADO: ")
for i in range(0, m):
    for j in range(0, n):
        vet[i] += mat[i][j]
    print(f"{vet[i]:.1f}")