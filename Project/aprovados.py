# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantos alunos serao digitados? "))

nome: [str] = [0 for x in range(n)]
n1: [float] = [0 for x in range(n)]
n2: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Digite nome, primeira e segunda nota do {i+1}o aluno: ")
    nome[i] = input()
    n1[i] = float(input())
    n2[i] = float(input())

print("Alunos aprovados:")
for i in range(0, n):
    med = (n1[i] + n2[i]) / 2
    if med >= 6.0:
        print(nome[i])