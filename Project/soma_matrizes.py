# EXERCÍCIO CORRETO - 1/10/24
m = int(input("Quantas linhas vai ter cada matriz? "))
n = int(input("Quantas colunas vai ter cada matriz? "))

a: [[int]] = [[0 for x in range(n)] for x in range(n)]
b: [[int]] = [[0 for x in range(n)] for x in range(n)]
c: [[int]] = [[0 for x in range(n)] for x in range(n)]

print("Digite os valores da matriz A:")
for i in range(0, m):
    for j in range(0, n):
        a[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Digite os valores da matriz B:")
for i in range(0, m):
    for j in range(0, n):
        b[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("MATRIZ SOMA:")
for i in range(0, m):
    for j in range(0, n):
        c[i][j] = a[i][j] + b[i][j]
        print(f"{c[i][j]}", end=" ")
    print()