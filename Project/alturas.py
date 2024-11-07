# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantas pessoas serao digitadas? "))

nome: [str] = [0 for x in range(n)]
idade: [int] = [0 for x in range(n)]
altura: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i+1}a pessoa: ")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))
    altura[i] = float(input("Altura: "))

soma = 0
for i in range(0, n):
    soma = soma + altura[i]

med = soma / n
print(f"\nAltura media: {med:.2f}")

menor, menores = 0, 0
for i in range(0, n):
    if idade[i] < 16:
        menores += 1

menor = menores / n * 100
print(f"Pessoas com menos de 16 anos: {menor:.1f}%")

for i in range(0, n):
    if idade[i] < 16:
        print(nome[i])
