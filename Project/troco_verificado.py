# EXERCÍCIO CORRETO - 1/10/24
preco = float(input("Preco unitario do produto: "))
qtd = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

troco = preco * qtd

if dinheiro < troco:
    troco = troco - dinheiro
    print(f"DINHEIRO INSUFICIENTE. FALTAM {troco:.2f} REAIS")
else:
    troco = dinheiro - troco
    print(f"TROCO = {troco:.2f}")