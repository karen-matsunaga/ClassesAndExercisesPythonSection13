# EXERCÍCIO CORRETO - 1/10/24
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
metro = float(input("Digite o valor do metro quadrado: "))

area = largura * comprimento
preco = area * metro

print(f"Area do terreno = {area:.2f}")
print(f"Preco do terreno = {preco:.2f}")