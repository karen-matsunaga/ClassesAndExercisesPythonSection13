# EXERCÍCIO CORRETO - 1/10/24
cod = int(input("Codigo do produto comprado: "))
qtd = int(input("Quantidade comprada: "))

valor = qtd

if cod == 1:
    valor = 5.00 * valor
elif cod == 2:
    valor = 3.50 * valor
elif cod == 3:
    valor = 4.80 * valor
elif cod == 4:
    valor = 8.90 * valor
elif cod == 5:
    valor = 7.32 * valor

print(f"Valor a pagar: R$ {valor:.2f}")