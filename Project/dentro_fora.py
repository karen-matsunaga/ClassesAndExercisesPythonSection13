# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantos numeros voce vai digitar? "))

dentro, fora = 0, 0
for i in range(0, n):
    x = int(input("Digite um numero: "))
    if x < 10 or x > 20:
        fora += 1
    else:
        dentro += 1
print(f"{dentro} DENTRO\n{fora} FORA")