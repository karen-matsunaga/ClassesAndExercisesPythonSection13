# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantas pessoas voce vai digitar? "))

nome: [str] = [0 for x in range(n)]
idade: [int] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i+1}a pessoa: ")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))

maior = idade[0]
pos = 0
for i in range(0, n):
    if maior < idade[i]:
        maior = idade[i]
        pos = i
print(f"PESSOA MAIS VELHA: {nome[pos]}")
