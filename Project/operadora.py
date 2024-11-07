# EXERCÍCIO CORRETO - 1/10/24
min = int(input("Digite a quantidade de minutos: "))
valor = 50.00
if min > 100:
    valor = valor + 2 * (min - 100)
    print(f"Valor a pagar: R$ {valor:.2f}")
else:
    print(f"Valor a pagar: R$ {valor:.2f}")