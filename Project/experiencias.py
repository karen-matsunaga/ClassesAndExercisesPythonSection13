# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Quantos casos de teste serao digitados? "))

c, r, s = 0, 0, 0

for i in range(0, n):
    cob = int(input("Quantidade de cobaias: "))
    tip = input("Tipo de cobaia: ")
    if tip == 'C':
        c += cob
    elif tip == 'R':
        r += cob
    elif tip == 'S':
        s += cob

t = c + r + s
pc = c / t * 100
pr = r / t * 100
ps = s / t * 100

print("\nRELATORIO FINAL:")
print(f"Total: {t} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {pc:.2f}")
print(f"Percentual de ratos: {pr:.2f}")
print(f"Percentual de sapos: {ps:.2f}")