# EXERCÍCIO CORRETO - 1/10/24
salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000.0:
    por = 20
elif salario <= 3000.0:
    por = 15
elif salario <= 8000.0:
    por = 10
else:
    por = 5

aumento = salario * (por / 100.0)
novo = salario + aumento

print(f"Novo salario = R$ {novo:.2f}")
print(f"Aumento = R$ {aumento:.2f}")
print(f"Porcentagem = {por} %")
