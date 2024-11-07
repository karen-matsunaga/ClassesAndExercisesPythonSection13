# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantos numeros voce vai digitar? "))

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input("Digite um numero: "))

cont = 0
print("\nNUMEROS PARES:")
for i in range(0, n):
    if vet[i] % 2 == 0:
        print(f"{vet[i]} ", end="")
        cont += 1

print(f"\n\nQUANTIDADE DE PARES = {cont}")