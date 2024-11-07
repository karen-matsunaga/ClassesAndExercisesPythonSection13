# EXERCÍCIO CORRETO - 1/10/24
n= int(input("Serao digitados dados de quantos produtos? "))

nome: [str] = [0 for x in range(n)]
compra: [float] = [0 for x in range(n)]
venda: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Produto {i+1}:")
    nome[i] = input("Nome: ")
    compra[i] = float(input("Preco de compra: "))
    venda[i] = float(input("Preco de venda: "))

ab, e, ac = 0, 0, 0
for i in range(0, n):
    por = (venda[i] - compra[i]) / compra[i] * 100

    if por < 10.0:
        ab += 1
    elif por <= 20.0:
        e += 1
    else:
        ac += 1

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {ab}")
print(f"Lucro entre 10% e 20%: {e}")
print(f"Lucro acima de 20%: {ac}")

tc, tv = 0, 0
for i in range(0, n):
    tc += compra[i]
    tv += venda[i]

tl = tv - tc
print(f"Valor total de compra: {tc:.2f}")
print(f"Valor total de venda: {tv:.2f}")
print(f"Lucro total: {tl:.2f}")