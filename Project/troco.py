# EXERCÍCIO CORRETO - 1/10/24
preco = float(input("Preco unitario do produto: "))
qtd = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))
troco = dinheiro - (preco * qtd)
print(f"TROCO = {troco:.2f}")