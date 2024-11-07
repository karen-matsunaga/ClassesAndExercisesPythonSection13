# EXERCÍCIO CORRETO - 1/10/24
x = int(input("Digite um numero inteiro: "))

while x != 0:
    if x % 2 != 0:
        x += 1
    pares = 5 * x + 20
    print(f"SOMA = {pares}")
    x = int(input("Digite um numero inteiro: "))
