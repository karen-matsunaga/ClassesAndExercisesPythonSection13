# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantos casos voce vai digitar? "))

for i in range(0, n):
    n = int(input("Entre com o numerador: "))
    d = int(input("Entre com o denominador: "))
    if d == 0:
        print("DIVISAO IMPOSSIVEL")
    else:
        div = n / d
        print(f"DIVISAO = {div:.2f}")